from asyncio.tasks import sleep
import discord,aiohttp,aiofiles,uuid,os
from discord import message
from discord import file
from discord.ext import commands
from discord import File

description = 'A bot for using decompyle to dissasemble python.'
bot = commands.Bot(command_prefix='>>', description=description)

@bot.event
async def on_ready():
    print('Logging in as {}'.format(bot.user.name))
    print('Bot ID is {}'.format(bot.user.id))
    print('=============================================')
    await bot.change_presence(activity=discord.Game('with .pyc files'))

@bot.command(name = 'Disassemble',description='Disassemble a .pyc file')
async def Disassemble(ctx):
    try:
        if isinstance(ctx.channel, discord.channel.DMChannel):
            if ctx.message.attachments:
                attachment = ctx.message.attachments[0]
                if '.pyc' in str(attachment):
                    await ctx.author.send('Processing...')
                    ID = str(uuid.uuid4())
                    session = aiohttp.ClientSession()
                    file = await session.get(attachment.url)
                    f = await aiofiles.open(ID + '.pyc', mode='wb')
                    await f.write(await file.read())
                    await f.close()
                    await session.close()
                    os.system("pycdas.exe " + ID + ".pyc" +">"+ID + ".txt")
                    await ctx.author.send('Finished Processing. Here is your result.')
                    await ctx.author.send(file=discord.File(ID + '.txt'))
                    os.remove(ID + '.pyc')
                    os.remove(ID + '.txt')
                else:
                    await ctx.author.send('Not a valid file type! Please use .pyc files!')
            else:
                await ctx.author.send('No Attachment found!')
        else:
            await ctx.send("Please use this command in DM's")
    except Exception as ex:
        print(ex)

@bot.command(name = 'Decompile',description='Decompiles a .pyc file')
async def Decompile(ctx):
    try:
        if isinstance(ctx.channel, discord.channel.DMChannel):
            if ctx.message.attachments:
                attachment = ctx.message.attachments[0]
                if '.pyc' in str(attachment):
                    await ctx.author.send('Processing...')
                    ID = str(uuid.uuid4())
                    session = aiohttp.ClientSession()
                    file = await session.get(attachment.url)
                    f = await aiofiles.open(ID + '.pyc', mode='wb')
                    await f.write(await file.read())
                    await f.close()
                    await session.close()
                    os.system("pycdc.exe " + ID + ".pyc" +">"+ID + ".txt")
                    await ctx.author.send('Finished Processing. Here is your result.')
                    await ctx.author.send(file=discord.File(ID + '.txt'))
                    os.remove(ID + '.pyc')
                    os.remove(ID + '.txt')
                else:
                    await ctx.author.send('Not a valid file type! Please use .pyc files!')
            else:
                await ctx.author.send('No Attachment found!')
        else:
            await ctx.send("Please use this command in DM's")
    except Exception as ex:
        print(ex)

bot.run('')