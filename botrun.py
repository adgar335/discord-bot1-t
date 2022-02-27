import discord
from discord.ext import commands
import os
import smtplib

bot = commands.Bot(command_prefix='*', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Я готов сэр!!!')

@bot.command()
async def тест(ctx):
    await ctx.send('Всё ок')

bot.run(os.getenv('TOKEN'))