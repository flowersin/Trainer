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
async def treat(ctx, arg):
    caller = ctx.author # Gather command sender
    match str(arg).lower():
        case "small":
            reason = "small"
        case "medium":
            reason = "small"
        case "large":
            reason = "large"
        case _:
            reason = "small"

    response = treatobj.treat(reason) # Send a treat via the treater object
    await ctx.send("@flowersin @" + caller + " " + response) # Send a response via discord
    logger.create_entry(caller, response) # Create a log entry

bot.run(token)