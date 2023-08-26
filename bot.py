import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

print ("Starting......")

load_dotenv()
TOKEN = os.dotenv('DISCORD_TOKEN')

client = discord.Client()
bot = commands.Bot(command_prefix="/")

@client.event
async def on_ready():
    print(f'(client.user) has connected to discord!')

client.run(TOKEN)