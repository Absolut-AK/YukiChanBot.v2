from code import interact
from msilib.schema import Component
from sre_constants import SUCCESS
import time
import os, discord, asyncio, random
from tkinter import E
from discord.ext import commands
from discord_components import *
from casino.blackjack import BlackJack
from util.data_base import DataBase
from combat.fighting_system import Fight
from combat.abilities import Abilities
from combat.user_stats import UserStats

from gui.help_text import helps

d = DataBase()

#discord connection
client = discord.Client()
client = commands.Bot(command_prefix='-')
client.remove_command('help')

#commands
@client.event
async def on_ready():
    DiscordComponents(client)
    await client.change_presence(activity=discord.Game(name="-help for information"))

@client.command()
async def start(ctx):
    print("works")
    id = ctx.message.author.id
    d.insert(id)
    d.dataRequest(f'''INSERT INTO users(id, coin, class, casino_pass) VALUES({id}, 500, "Starter", 0)''')
    d.dataRequest(f'''INSERT INTO weapon(id, name, power, attack, speed, critchance, critdamage) VALUES({id}, "Training Sword", 10, 10, 10, 10, 10)''')
    #test
    d.dataRequest(f'''UPDATE enemy1 SET health = 100, power = 10, attack = 10, speed = 10 WHERE id={id}''')
    d.dataRequest(f'''UPDATE stats SET health = 10, power = 10, attack = 10, speed = 10 WHERE id={id}''')
    try:
        pass
        await ctx.send("Inserting...")
    except Exception:
        await ctx.send("Already Inserted to DB")


@client.command()
async def bj(ctx):
    id = ctx.message.author.id
    b = BlackJack()
    hand = b.hand()

    async def hitOrStand():
        await ctx.send("Hit or stand (h/s)")
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
            else:
                await hitOrStand()
        else:
            await ctx.send(f"Dealer has {b.dealerHand[0]} and {b.dealerHand[1]}")
            outcome = b.stand()
            for i, j in enumerate(b.dealerHand):
                if i >= 2:
                    await ctx.send(f"Dealer Hit:{j}")
                    await asyncio.sleep(0.5)
            await asyncio.sleep(1)
            await ctx.send(outcome)
            return

    await ctx.send(f"{hand}")
    await hitOrStand()

@client.command()
async def test(ctx):
    id = ctx.message.author.id
    async def testFunc():
        await ctx.send("Hmmm")
    buttons = [
        ActionRow(
            Button(style=ButtonStyle.blue, label= 'Ability1'),
            Button(style=ButtonStyle.blue, label= 'Ability2'),
            Button(style=ButtonStyle.blue, label= 'Ability3'),
            Button(style=ButtonStyle.blue, label= 'Ability4')
        ),
        ActionRow(
            Button(style=2, label= 'Ability6'),
            Button(style=2, label= 'Ability7'),
            Button(style=2, label= 'Ability8'),
            Button(style=2, label= 'Ability5')
        ),
        ActionRow(
            Button(style=3, label= 'Done'),
            Button(style=4, label= 'Exit'),
            Button(style=5, label= 'GitHub', url='https://github.com/Absolut-AK/YukiChanBot.v2'),
        )
    ]
    await ctx.send("This is a test", components=buttons)
    t = time.time()
    t2 = int(time.time() - t)
    while t2 < 60:
        t2 = int(time.time() - t)
        res = await client.wait_for("button_click")
        await res.respond(type=6)
        if res.component.label == "Ability1":
            await ctx.send("A1")
        elif res.component.label == "Ability2":
            await ctx.send("A2")


@client.command()
async def help(ctx):
    text = helps()
    embed = discord.Embed(title="Tutorial for Yuki's DiscordBot", description=text)
    embed.set_footer(text="This is yuki's beta version of the game, there are a lot missed future, it took 3 weeks, I think, I forgot... well have fun ig")
    await ctx.send(embed=embed)

@client.command()
async def starter(ctx):
    id = ctx.message.author.id

@client.command()
async def proto(ctx):
    id = ctx.message.author.id
    a = Abilities()
    u = UserStats()
    user = u.statCalculation(d.dicPull(id, 'stats'), d.dicPull(id, 'weapon'), d.dicPull(id, 'helmet'), d.dicPull(id, 'chest'), d.dicPull(id, 'pants'), d.dicPull(id, 'boots'))
    f = Fight(user, n1=d.dicPull(id, 'enemy1'), n2=d.dicPull(id, 'enemy2'), n3=d.dicPull(id, 'enemy3'), n4=d.dicPull(id, 'enemy4'), n5=d.dicPull(id, 'enemy5'), n6=d.dicPull(id, 'enemy6'))

    buttons = [
        [
            Button(style=ButtonStyle.blue, label= 'Enemy1'),
            Button(style=ButtonStyle.blue, label= 'Enemy2'),
            Button(style=ButtonStyle.blue, label= 'Enemy3'),
            Button(style=ButtonStyle.blue, label= 'Enemy4'),
        ],
        [
            Button(style=2, label= 'Ability1'),
            Button(style=2, label= 'Ability2'),
            Button(style=2, label= 'Ability3'),
            Button(style=2, label= 'Ability4')
        ],
        [
            Button(style=3, label= 'Done'),
            Button(style=4, label= 'Exit')
        ]
    ]
    
    

    async def attacks():
        text = "Pick a Enemy and Ability:"
        
        embed = discord.Embed(title="Fighting Prototype", description=text)
        await ctx.send(embed=embed, components=buttons)
        t = time.time()
        t2 = int(time.time() - t)
        enemy = None
        ability = None
        done = None
        while t2 < 60 and done == None:
            t2 = int(time.time() - t)
            res = await client.wait_for("button_click")
            await res.respond(type=6)
            if res.component.label == "Enemy1":
                await ctx.send("E1")
                enemy = 1
            elif res.component.label == "Ability1":
                await ctx.send("A1")
                ability = 1
            elif res.component.label == "Done":
                if enemy != None and ability != None:
                    await ctx.send("Done")
                    f = discord.Embed(title="Fighting Prototype", description=text)
                    await res.respond(content= '', embed=f, components= [])
                    break
                else:
                    await ctx.send("You haven't picked Enemy or Ability")
            

    await attacks()
#path to YukiChanBot's token and executes it
path = "..\\YukiChanToken"
os.chdir(path)
with open('token.txt', 'r') as f:
    token = f.read()
    client.run(token)