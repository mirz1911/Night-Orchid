import os
import asyncio
import random
import discord
import discord.ext
from dotenv import load_dotenv
from scanner import program
from ping import doping

print ("Starting......")

bot = discord.Bot()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('GUILD_ID')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to discord!')
    nem = ['/spin', '/roll', '/flip']
    val = True
    while (val):
        nems = random.choice(nem)        
        await bot.change_presence(activity=discord.Game(name=nems))
        
    

@bot.slash_command(name = 'roll', description = 'Usage: /roll dice amount:<1/2>, Initiate !roll on dice')
async def roll(ctx, amount: int):
    if(amount == 1):
        x = range (1,6)
        y = random.choice(x)
        await ctx.respond(f':game_die: Dice roll result is: {y}')
        return
    if (amount == 2):
        x = range (2,6)
        y = random.choice(x)
        z = random.choice(x)
        await ctx.respond(f':game_die: :game_die: Two dices roll result is: {y} and {z}')
        return
    else: 
        await ctx.respond('bruh')
        return
    
@bot.slash_command(name = 'flip', description = 'flip coin')
async def flip(ctx):
    x = ['head', 'number']
    y = random.choice(x)
    await ctx.respond(f'Coin flip result is: {y}')
    return
    
@bot.slash_command(name = 'spin', description = 'selot gacor')
async def spin(ctx):
    x = [' :seven: ', ' :cherries: ', ' :gem: ', ' :skull: ', ' :bell: ', ' :lemon: ', ' :coin: ', ' :moyai: ']
    a = random.choice(x)
    b = random.choice(x)
    c = random.choice(x)
    await ctx.respond(f'result: [{a}|{b}|{c}]')
    if a == b == c:
        await ctx.send(f'GACOR!')
        return
    else: 
        await ctx.send(f'Nice Try')
        return
        
@bot.slash_command(name = 'scan', description = 'provide ip address scan results')
async def scan(ctx, ip):
    answer = program(ip)
    x = ['Talking with Katheryne...', 'Searching Mondstatd library...', 'Talking with Ella Musk...', 'Searching the Akasha terminal...', 'Gathering info from the Fatui...']
    a = random.choice(x)
    await ctx.respond(f'Accessing Qixing database...')
    await ctx.send(f'...')
    asyncio.sleep(2)
    await ctx.send(a)
    await ctx.send(f'...')
    asyncio.sleep(2)
    await ctx.send(f'Gathering information Dump...')
    await ctx.send(f'Sending...')
    await ctx.send(answer)

@bot.slash_command(name = 'ping', description = 'initiate a ping request')
async def ping(ctx, host):
    answer = doping(host)
    await ctx.respond(f'Pinging...')
    await ctx.send(answer)

@bot.slash_command(name = 'post', description = 'post your original content')
async def post(ctx, file: discord.Attachment, title):
    await ctx.respond(f'{file}')
    message= await ctx.send(f'{title} by: {ctx.author.mention}')
    await message.add_reaction("👍")


bot.run(TOKEN)