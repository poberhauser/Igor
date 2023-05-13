from lib2to3.pgen2 import token
import discord
import os
import markovify

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv('.env')
TOKEN = os.getenv('DISCORD_TOKEN') 
GUILD = os.getenv('DISCORD_GUILD')

prefix = '!'

needed_intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=needed_intents)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.event
async def on_message(message: str):
    if not message.author.bot:
        for mention in message.mentions:
            if mention.bot:
                channel = message.channel
                with open("logs.txt", 'rb') as f:
                    text = f.read()
                    print(message.content)
                text_model = markovify.Text(text)
            await channel.send(text_model.make_sentence(tries=100000000))

    with open("logs.txt", "a") as text_file:
        print(message.content)
        if " " or "<@" not in message.content:
            text_file.write(message.content + ", ")

bot.run(TOKEN)
