# Import Discord.py (https://github.com/Rapptz/discord.py)
import discord
from discord.ext import commands
# Import os
import os
#import custom modules

# Read API key
with open(".token", "r") as file:
    token = file.read()
    # Ellie pls add error handling

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='~', intents=intents)

@bot.command()
async def treat(ctx):
    await ctx.send('Good Kitty!')

@bot.command()
async def warn(ctx):
    await ctx.send("Kitty...")

@bot.command()
async def punish(ctx):
    await ctx.send("Bad Kitty!")

bot.run(token)