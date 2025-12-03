# Import Discord.py (https://github.com/Rapptz/discord.py)
import discord
from discord.ext import commands
# Import os
import os
#import custom modules
import logger # For logging
import treater # For treating :3

# Initialize Logger
logger = logger.Logger('.trainer.log')
logger.create_entry("APP", "Application Started")

# Initialize Treater
treatobj=treater.Treater()

# Read API key
with open(".token", "r") as file:
    token = file.read()
    # Ellie pls add error handling

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='~', intents=intents)

@bot.command()
async def treat(ctx, *args):
    caller = ctx.author # Gather command sender

    # Determine Reason, if any
    if len(args) == 0:
        reason = None
    else:
        reason = str(', '.join(args))

    response = treatobj.treat(reason) # Send a treat via the treater object
    await ctx.send(response) # Send a response via discord
    logger.create_entry(caller, response) # Create a log entry
    

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