"""I like Pete Davidson, you like Pete Davidson so I made a bot, okay?
Okay.
"""

import os
import random

import discord
from discord.ext import commands


description = "Gives you Pete Davidson gifs, okay?"
bot = commands.Bot(command_prefix="/", description=description)

okays = [
    "https://media.giphy.com/media/xT9IgrlyzJlE6ljtS0/giphy.gif",
    "https://thumbs.gfycat.com/ForcefulHopefulJapanesebeetle-max-1mb.gif",
    "https://tenor.com/MWVF.gif",
    "https://tenor.com/TKX1.gif",
    "https://tenor.com/7geU.gif",
    "https://tenor.com/GS73.gif",
]

morepete = [
    "https://media.giphy.com/media/3o7aDaYBtNbdNv1eWQ/giphy.gif",
    "https://thumbs.gfycat.com/UltimateGorgeousIberianmole-max-1mb.gif",
    "https://media.giphy.com/media/3o7TKu6WJxtZvbqKv6/giphy.gif",
    "https://media0.giphy.com/media/xUOwG0QGuvAbBcOhyM/source.gif",
    "https://media2.giphy.com/media/8jBExrz7Axgha/giphy.gif",
    "https://media0.giphy.com/media/1xmXet0VtamgfrFLbd/source.gif",
    "https://media2.giphy.com/media/NQUuOKTR6aHCmbwBRm/source.gif",
    "https://media1.giphy.com/media/djVuHoknhk89y/source.gif",
    "https://media2.giphy.com/media/3j1cVdG8uWR82e8OJG/source.gif",
    "https://media2.giphy.com/media/9S1yaD4TfqLueDAtRL/source.gif",
    "https://media.tenor.com/images/020e9694a25eed2b90b881678e263981/tenor.gif",
]

others = [
    "https://media1.giphy.com/media/l0NgRiyoFdg6uspoc/source.gif",
    "https://media.giphy.com/media/Bo1lBI2y1vT0mQ0Ttv/giphy.gif",
    "https://media.giphy.com/media/3o6Mb7fSXeAWwGV7Hy/giphy.gif",
    "https://media.giphy.com/media/3o7TKy3KWDYOA7OUSI/giphy.gif",
    "https://media1.tenor.com/images/9950127c0d9d4be1f6f56ee59ecf99e1/tenor.gif?itemid=7545767",
    "http://gif-finder.com/wp-content/uploads/2016/01/Maya-Rudolph-Okay.gif",
    "https://tenor.com/view/okay-question-confused-gif-11384829",
]


@bot.event
async def on_ready():
    print("Logged in.")


@bot.command(description='Returns a random "okay" gif of Pete Davidson.')
async def okay(ctx):
    print("okay")
    await ctx.send(random.choice(okays))


@bot.command(description="Returns a random gif of Pete Davidson.")
async def notokay(ctx):
    print("not okay")
    await ctx.send(random.choice(morepete))


@bot.command(description="Returns a random gif that does NOT contain Pete Davidson.")
async def notpete(ctx):
    print("not Pete")
    await ctx.send(random.choice(others))


@bot.command(description="Returns a gif explaining you're a dick.")
async def dick(ctx):
    print("Someone was a dick.")
    await ctx.send("https://media1.giphy.com/media/7JgyqZYNM4T3T59Q3H/source.gif")


@bot.command(description="Returns a gif about China.")
async def dick(ctx):
    print("Someone really loves China.")
    await ctx.send("https://video.twimg.com/tweet_video/D8nWX9sW4AAdWTY.mp4")


# DISCORDTOKEN ENV VAR MUST BE SET OR SERVER WILL NOT RUN
# EXPORT DISCORDTOKEN=XXXXXXXXXXXXXXX
bot.run(os.environ.get("DISCORDTOKEN"))
