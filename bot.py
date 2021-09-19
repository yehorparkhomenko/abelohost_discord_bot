import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.', description="My bot", intents=discord.Intents.all(), help_command=None)
