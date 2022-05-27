import discord
from datetime import datetime

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('!'):
        if message.author == client.user:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello!')


@client.event
async def on_voice_state_update(member, before, after):
    dt = datetime.now()
    str_date_time = dt.strftime("%d-%m-%Y, %H:%M:%S")
    channel = client.get_channel(962432876475998298)
    if after.channel is None and before.channel is not None:
        await channel.send(str_date_time + " " + member.name + " verliess den Channel " + before.channel.name)
    if before.channel is None and after.channel is not None:
        await channel.send(str_date_time + " " + member.name + " betrat den Channel " + after.channel.name)    
    if before.channel is not None and after.channel is not None:
        if after.channel.name != before.channel.name:
            await channel.send(str_date_time + " " + member.name + " ging von " + before.channel.name + " nach " + after.channel.name)
 

from pathlib import Path
bot_token = Path('./token.txt').read_text()

client.run(bot_token)