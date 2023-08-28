import os
import random
import discord
import discord.ext
from dotenv import load_dotenv

print ("Starting......")

bot = discord.Bot()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('GUILD_ID')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to discord!')

@bot.slash_command(name = 'roll', description = 'Usage: /roll type:<dice/coin> number:<1/2>, Initiate !roll on dice or coin')
async def roll(ctx, type, amount: int):
    if (type == 'dice'):
        if(amount==1):
            x = range (1,6)
            y = random.choice(x)
            await ctx.respond(f'Dice roll result is: {y}')
            return
        if (amount == 2):
            x = range (1,6)
            y = random.choice(x)
            z = random.choice(x)
            await ctx.respond(f'Two dices roll result is: {y} and {z}')
            return
        else: 
            await ctx.respond('bruh')
            return
    if (type == 'coin'):
        if (amount == 1):
            x = ['head', 'number']
            y = random.choice(x)
            await ctx.respond(f'Coin flip result is: {y}')
            return
        if (amount == 2):
            x = ['head', 'number']
            y = random.choice(x)
            z = random.choice(x)
            await ctx.respond(f'Coin flip result is: {y} and {z}')
            return
        else:
            await ctx.respond('bruh')
            return
    else:
        await ctx.respond('bruh')
        return
    
@bot.slash_command(name = 'spin', description = 'selot gacor')
async def spin(ctx, arg):
    if (arg == 'lottery'):
        x = ['7', 'Cherry', 'Diamond', 'Sphinx', 'Coin', 'Banana', 'Grape', 'Watermelon']
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
    else:
        await ctx.respond('bruh')
        
        
bot.run(TOKEN)