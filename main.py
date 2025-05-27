import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Definindo prefixo dos comandos
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong! 🏓')

@bot.command(name='oi')
async def oi(ctx):
    await ctx.send(f'Olá, {ctx.author.mention}! 👋')

bot.run(TOKEN)
