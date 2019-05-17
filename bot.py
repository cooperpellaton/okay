"""I like Pete Davidson, you like Pete Davidson so I made a bot, okay?
Okay.
"""

import os
import random

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="?", description=description)

okays = [
    "https://media.giphy.com/media/xT9IgrlyzJlE6ljtS0/giphy.gif",
    "https://thumbs.gfycat.com/ForcefulHopefulJapanesebeetle-max-1mb.gif"
    "https://tenor.com/MWVF.gif",
    "https://tenor.com/TKX1.gif",
    "https://tenor.com/7geU.gif",
    "https://tenor.com/GS73.gif",
]

others = [
    "https://media.giphy.com/media/3o7aDaYBtNbdNv1eWQ/giphy.gif",
    "https://thumbs.gfycat.com/UltimateGorgeousIberianmole-max-1mb.gif",
    "https://media.giphy.com/media/3o7TKu6WJxtZvbqKv6/giphy.gif",
]

@bot.event
async def on_ready():
    print("Logged in.")


@bot.command(description='Returns a random "okay" gif of Pete Davidson.')
async def okay(ctx):
    print("okay")
    await ctx.send(random.choice(okays))


@bot.command(description='Returns a random gif of Pete Davidson.')
async def notokay(ctx):
    print("not okay")
    await ctx.send(random.choice(others))


# DISCORDTOKEN ENV VAR MUST BE SET OR SERVER WILL NOT RUN
# EXPORT DISCORDTOKEN=XXXXXXXXXXXXXXX
bot.run(os.environ.get("DISCORDTOKEN"))
