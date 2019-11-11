import os
from bookscrape import check_zong
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')


client = discord.Client()

print(discord.version_info)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
   
    channel = client.get_channel(642419768753782787)
    await channel.send('hello')


async def check_raw():
    channel = client.get_channel(642419768753782787)
    await channel.send(check_zong("http://book.zongheng.com/book/408586.html"))

   

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == '!raw' :
        await message.channel.send(check_zong("http://book.zongheng.com/book/408586.html"))

    if message.content == '!start' :
        var = 1
        while (var == 1 ) :
            await check_raw()
            time.sleep(300)
       
client.run(token)
