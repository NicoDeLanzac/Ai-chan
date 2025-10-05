import os
import discord
from datetime import datetime
from pathlib import Path


intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_voice_state_update(member, before, after):
    dt = datetime.now()
    str_date_time = dt.strftime("%d-%m-%Y, %H:%M:%S")
    channel = client.get_channel(1424179449795969086)
    if after.channel is None and before.channel is not None:
        await channel.send("`" + str_date_time + " " + member.name + " verliess den Channel " + before.channel.name + "`")
    if before.channel is None and after.channel is not None:
        await channel.send("`" + str_date_time + " " + member.name + " betrat den Channel " + after.channel.name + "`")    
    if before.channel is not None and after.channel is not None:
        if after.channel.name != before.channel.name:
            await channel.send("`" + str_date_time + " " + member.name + " ging von " + before.channel.name + " nach " + after.channel.name + "`")
 

bot_token = os.getenv("DISCORD_TOKEN")

client.run(bot_token)
