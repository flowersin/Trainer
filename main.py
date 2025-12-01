# Import Discord.py (https://github.com/Rapptz/discord.py)
import discord
from discord.ext import commands
# Import os
import os
#import custom modules
import logger # For logging

logger = logger.Logger('.trainer.log')
logger.create_entry("APP", "Application Started")

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
    caller = ctx.author
    logger.create_entry(caller, "Treated")

@bot.command()
async def warn(ctx):
    await ctx.send("Kitty...")
    caller = ctx.author
    logger.create_entry(caller, "Warned")

@bot.command()
async def punish(ctx):
    await ctx.send("Bad Kitty!")
    caller = ctx.author
    logger.create_entry(caller, "Punished")

bot.run(token)