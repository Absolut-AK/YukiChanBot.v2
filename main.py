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
    print("ready")
    DiscordComponents(client)
    await client.change_presence(activity=discord.Game(name="-help for information"))

@client.command()
async def start(ctx):
    id = ctx.message.author.id
    d.insert(id)
    d.dataRequest(f'''INSERT INTO users(id, coin, class, casino_pass) VALUES({id}, 500, "Starter", 0)''')
    d.dataRequest(f'''INSERT INTO weapon(id, name, power, attack, speed, critchance, critdamage) VALUES({id}, "Training Sword", 10, 10, 10, 10, 10)''')
    #test
    d.dataRequest(f'''UPDATE enemy1 SET health = 100, power = 10, attack = 10, speed = 10 WHERE id={id}''')
    d.dataRequest(f'''UPDATE stats SET health = 10, power = 10, attack = 10, speed = 10, abilityslot1 = "FireBall" WHERE id={id}''')
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
            Button(style=ButtonStyle.blue, id= 'Ability1'),
            Button(style=ButtonStyle.blue, id= 'Ability2'),
            Button(style=ButtonStyle.blue, id= 'Ability3'),
            Button(style=ButtonStyle.blue, id= 'Ability4')
        ),
        ActionRow(
            Button(style=2, id= 'Ability6'),
            Button(style=2, id= 'Ability7'),
            Button(style=2, id= 'Ability8'),
            Button(style=2, id= 'Ability5')
        ),
        ActionRow(
            Button(style=3, id= 'Done'),
            Button(style=4, id= 'Exit'),
            Button(style=5, id= 'GitHub', url='https://github.com/Absolut-AK/YukiChanBot.v2'),
        )
    ]
    await ctx.send("This is a test", components=buttons)
    t = time.time()
    t2 = int(time.time() - t)
    while t2 < 60:
        t2 = int(time.time() - t)
        res = await client.wait_for("button_click")
        await res.respond(type=6)
        if res.component.id == "Ability1":
            await ctx.send("A1")
        elif res.component.id == "Ability2":
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
async def p(ctx):
    message = ctx.message
    await asyncio.sleep(0.5)
    await message.delete()
    id = ctx.message.author.id
    a = Abilities()
    u = UserStats()
    user = u.statCalculation(d.dicPull(id, 'stats'), d.dicPull(id, 'weapon'), d.dicPull(id, 'helmet'), d.dicPull(id, 'chest'), d.dicPull(id, 'pants'), d.dicPull(id, 'boots'))
    f = Fight(user, n1=d.dicPull(id, 'enemy1'), n2=d.dicPull(id, 'enemy2'), n3=d.dicPull(id, 'enemy3'), n4=d.dicPull(id, 'enemy4'), n5=d.dicPull(id, 'enemy5'), n6=d.dicPull(id, 'enemy6'))

    a1, a1tf = d.dataPull(id, 'abilityslot1', 'stats')
    a2, a2tf = d.dataPull(id, 'abilityslot2', 'stats')
    a3, a3tf = d.dataPull(id, 'abilityslot3', 'stats')
    a4, a4tf = d.dataPull(id, 'abilityslot4', 'stats')
    a5, a5tf = d.dataPull(id, 'abilityslot5', 'stats')
    e1tf = d.noneToTrue(d.dicPull(id, 'enemy1').get('health'))
    e2tf = d.noneToTrue(d.dicPull(id, 'enemy2').get('health'))
    e3tf = d.noneToTrue(d.dicPull(id, 'enemy3').get('health'))
    e4tf = d.noneToTrue(d.dicPull(id, 'enemy4').get('health'))
    e5tf = d.noneToTrue(d.dicPull(id, 'enemy5').get('health'))
    e6tf = d.noneToTrue(d.dicPull(id, 'enemy6').get('health'))
    buttons = [
        [
            Button(style=ButtonStyle.blue, label= 'Enemy1', id= 'Enemy1', disabled= e1tf),
            Button(style=ButtonStyle.blue, label= 'Enemy2', id= 'Enemy2', disabled= e2tf),
            Button(style=ButtonStyle.blue, label= 'Enemy3', id= 'Enemy3', disabled= e3tf)
        ],
        [
            Button(style=ButtonStyle.blue, label= 'Enemy4', id= 'Enemy4', disabled= e4tf),
            Button(style=ButtonStyle.blue, label= 'Enemy5', id= 'Enemy5', disabled= e5tf),
            Button(style=ButtonStyle.blue, label= 'Enemy6', id= 'Enemy6', disabled= e6tf),
        ],
        [
            Button(style=4, label= 'Attack', id= 'Attack'),
            Button(style=2, label= a1, id= 'Ability1', disabled= a1tf),
            Button(style=2, label= a2, id= 'Ability2', disabled= a2tf)
        ],
        [
            Button(style=2, label= a3, id= 'Ability3', disabled= a3tf),
            Button(style=2, label= a4, id= 'Ability4', disabled= a4tf),
            Button(style=2, label= a5, id= 'Ability5', disabled= a5tf)
        ],
        [
            Button(style=3, label= 'Done'),
            Button(style=4, label= 'Exit')
        ]
    ]
    
    fightText = f.fightingLog()
    text = "Pick a Enemy and Ability: \n" + fightText
    
    embed = discord.Embed(title="Fighting Prototype", description=text)
    msg = await ctx.send(embed=embed, components=buttons)
    t = time.time()
    t2 = int(time.time() - t)
    enemy = None
    ability = None
    done = None
    u = f.user.get('health')

    while t2 < 60 and done == None and u > 0:
        t2 = int(time.time() - t)
        res = await client.wait_for("button_click")
        await res.respond(type=6)

        match res.component.id:
            case n if n == "Enemy1":
                enemy = 1
            case n if n == "Enemy2":
                enemy = 2
            case n if n == "Enemy3":
                enemy = 3
            case n if n == "Enemy4":
                enemy = 4
            case n if n == "Enemy5":
                enemy = 5
            case n if n == "Enemy6":
                enemy = 6
            case n if n == "Attack":
                ability = 1
            case n if n == "Ability1":
                ability = 2
            case n if n == "Ability2":
                ability = 3
            case n if n == "Ability3":
                ability = 4
            case n if n == "Ability4":
                ability = 5
            case n if n == "Ability5":
                ability = 6

        if res.component.label == "Done":
            if enemy != None and ability != None:
                e, u = f.fightingSytem(enemy, ability)
                if u > 0 and e <=0:
                    await ctx.send("You killed one")
                elif u <= 0:
                    await ctx.send("You died")
                fightText = f.fightingLog()

                text = "Pick a Enemy and Ability: \n" + fightText
                em = discord.Embed(title="Fighting Prototype", description=text)
                await res.respond(content= '', embed=em, components= buttons)
            else:
                await ctx.send("You haven't picked Enemy or Ability")
        elif res.component.label == "Exit":
            await msg.delete()
            await ctx.send("Running Away")
            break
    
    if u <= 0:
        await msg.delete()
#path to YukiChanBot's token and executes it
path = "..\\YukiChanToken"
os.chdir(path)
with open('token.txt', 'r') as f:
    token = f.read()
    client.run(token)