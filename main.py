import os
import discord
from discord.ext import commands
from dataBase import *

from gui.helpText import helps

#discord connection
client = discord.Client()
client = commands.Bot(command_prefix='-')
client.remove_command('help')

#commands
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="-help for information"))
    dataRequest('''CREATE TABLE IF NOT EXISTS users(
        id INTEGER, 
        coin INTEGER,
        class TEXT 
        stats BLOB,
        inventory BLOB,
        equipment BLOB)

        ''')
    dataRequest('INSERT INTO users(id) VALUES(2)')

@client.command()
async def coinflip(ctx, ammount=0, HorT=None):
    id = ctx.message.author.id
    # if coin >= 10 and  coin >= ammount:
    #     if HorT != None:
    #         HorT = HorT.lower()
    #     if ammount < 10  or ammount > 100 or HorT == None:
    #         await ctx.send("Choose your bet(min 10, max 100) and guessing side(-coinflip 10 tails or heads)")
    #     elif HorT == 'heads' or HorT == 'tails':
    #         await ctx.send(coinFlip(ammount, HorT, id))
    #     else:
    #         await ctx.send("Choose your bet(min 10, max 100) and guessing side(-coinflip 10 tails or heads)")
    # else:
    #     await ctx.send("You don't have enough coins. <(￣︶￣)>")

@client.command()
async def help(ctx):
    text = helps()
    embed = discord.Embed(title="Tutorial for Yuki's DiscordBot", description=text)
    embed.set_footer(text="This is yuki's beta version of the game, there are a lot missed future, it took 3 weeks, I think, I forgot... well have fun ig")
    await ctx.send(embed=embed)

@client.command()
async def starter(ctx):
    id = ctx.message.author.id

#path to YukiChanBot's token and executes it
path = "..\\YukiChanToken"
os.chdir(path)
with open('token.txt', 'r') as f:
    token = f.read()
    client.run(token)