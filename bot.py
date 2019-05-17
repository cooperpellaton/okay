import discord
import os
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='?', description=description)

okays = ["https://media.giphy.com/media/xT9IgrlyzJlE6ljtS0/giphy.gif", "https://tenor.com/MWVF.gif", "https://tenor.com/TKX1.gif", "https://tenor.com/7geU.gif", "https://tenor.com/GS73.gif"]

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)

@bot.command(description='Returns a random "okay" gif of Pete Davidson.')
async def okay(ctx):
    await ctx.send(random.choice())


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot(ctx):
    await ctx.send('okay.')

# DISCORDTOKEN ENV VAR MUST BE SET OR SERVER WILL NOT RUN
# IE EXPORT DISCORDTOKEN=XXXXXXXXXXXXXXX
bot.run(os.environ.get('DISCORDTOKEN'))