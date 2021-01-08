import discord
import os
from keep_alive import keep_alive

client = discord.Client()


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author != client.user:
    await message.send('The staff team will get back to you as soon as possible.')
  

keep_alive()
token = os.environ.get("TOKEN")
client.run(token)