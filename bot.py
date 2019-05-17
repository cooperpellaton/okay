import discord
import os
from discord.ext import commands
import random

description = """I like Pete Davidson, you like Pete Davidson so I made a bot, okay?
Okay.
"""

bot = commands.Bot(command_prefix="?", description=description)

okays = [
    "https://media.giphy.com/media/xT9IgrlyzJlE6ljtS0/giphy.gif",
    "https://tenor.com/MWVF.gif",
    "https://tenor.com/TKX1.gif",
    "https://tenor.com/7geU.gif",
    "https://tenor.com/GS73.gif",
]


@bot.event
async def on_ready():
    print("Logged in.")


@bot.command(description='Returns a random "okay" gif of Pete Davidson.')
async def okay(ctx):
    print("okay")
    await ctx.send(random.choice())


# DISCORDTOKEN ENV VAR MUST BE SET OR SERVER WILL NOT RUN
# IE EXPORT DISCORDTOKEN=XXXXXXXXXXXXXXX
bot.run(os.environ.get("DISCORDTOKEN"))
