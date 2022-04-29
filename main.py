import os, discord, asyncio, random
from discord.ext import commands
from dataBase import *
from casino.DiscordBlackJack import BlackJack

from gui.helpText import helps

#discord connection
client = discord.Client()
client = commands.Bot(command_prefix='-')
client.remove_command('help')

#commands
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="-help for information"))

    #user table
    dataRequest('''CREATE TABLE IF NOT EXISTS users(
        id INTEGER, 
        coin INTEGER,
        class TEXT)
        ''')
    #inventory table
    dataRequest('''CREATE TABLE IF NOT EXISTS inventory(
                id INTEGER)''')

    #equipments
    dataRequest('''CREATE TABLE IF NOT EXISTS weapon(
                id INTEGER
                power INTEGER
                speed INTEGER
                attack INTEGER
                critchance INTEGER
                critdamage INTEGER)
                ''')

    dataRequest('''CREATE TABLE IF NOT EXISTS helmet(
                id INTEGER
                power INTEGER
                attack INTEGER
                speed INTEGER
                endurance INTEGER
                agility INTEGER
                stamina INTEGER
                critchance INTEGER
                critdamage INTEGER)
                ''')

    dataRequest('''CREATE TABLE IF NOT EXISTS chest(
                id INTEGER
                power INTEGER
                speed INTEGER
                endurance INTEGER
                agility INTEGER
                stamina INTEGER
                critchance INTEGER
                critdamage INTEGER)
                ''')

    dataRequest('''CREATE TABLE IF NOT EXISTS pants(
                id INTEGER
                power INTEGER
                speed INTEGER
                endurance INTEGER
                agility INTEGER
                stamina INTEGER
                critchance INTEGER
                critdamage INTEGER)
                ''')

    dataRequest('''CREATE TABLE IF NOT EXISTS boots(
                id INTEGER
                power INTEGER
                speed INTEGER
                endurance INTEGER
                agility INTEGER
                stamina INTEGER
                critchance INTEGER
                critdamage INTEGER)
                ''')
    
    dataRequest('''CREATE TABLE IF NOT EXISTS redGem(
                id INTEGER
                power INTEGER
                attack INTEGER
                critchance INTEGER
                critdamage INTEGER)
                ''')

    dataRequest('''CREATE TABLE IF NOT EXISTS blueGem(
                id INTEGER
                mana INTEGER
                stamina INTEGER)
                ''')

    dataRequest('''CREATE TABLE IF NOT EXISTS greenGem(
                id INTEGER
                agility INTEGER
                endurance INTEGER)
                ''')

@client.command()
async def bj(ctx):
    id = ctx.message.author.id
    b = BlackJack()
    hand = b.hand()

    async def hitOrStand():
        try:
            msg = await client.wait_for("message", timeout=30, check=lambda message: message.author == ctx.author and 
            message.channel == ctx.channel)
        except asyncio.TimeoutError:
            await ctx.send("You took to long")

        if msg.content == 'h':
            c = b.hit()
            await ctx.send(f"you got a {c}.")
            userSum = b.cal(b.userHand)
            if userSum > 21:
                await ctx.send("Bust")

            await hitOrStand()
        elif msg.content == "s":
            await ctx.send(f"Dealer has {b.dealerHand[0]} and {b.dealerHand[1]}")
            await ctx.send(b.stand())
            await ctx.send(f"Dealer hand is {b.dealerHand}")
        else:
            await ctx.send("I guess stand...")
            await ctx.send(f"Dealer has {b.dealerHand[0]} and {b.dealerHand[1]}")
            await ctx.send(b.stand())
            await ctx.send(f"Dealer hand is {b.dealerHand}")

    await ctx.send(f"{hand}\n Hit or stand (h/s)")
    await hitOrStand()



    


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