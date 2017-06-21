import discord
from discord.ext import commands
import random

description = '''EthanAddict's first bot written in Python with discord.py

and it is glorious'''
bot = commands.Bot(command_prefix='ebot!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def magic8ball():
	"""Think of something and type this command to get an answer"""
	answers = ["Yes", "No", "My sources say yes", "My sources say no", "Ask again later", "Definitely", "I bet you don't want to know", "Not now", "No for sure", "Concentrate and ask again", "Maybe", "Probably not"]
	await bot.say(answers[random.randint(0, 11)])	

@bot.command()
async def f():
	"""To pay respects"""
	await bot.say("Respects have been paid")

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')

bot.run('MzI3MDEzNTUxMzA0NzM2NzY4.DCvKsw.4_V_SlVFXIqKOcqR4oeyp7ZmSHY')
