#!/usr/bin/env python3
import discord
import json
import os

MAX_MESSAGE_LENGTH = 2000

config = json.load(open("config.json"))

token = os.getenv("DISCORD_BOT_TOKEN")


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def get_split_contents(filename):
    with open(filename, "r") as f:
        messages = []
        chunks = f.read().split("\n\n")
        while len(chunks) > 0:
            message = ""
            while len(chunks) > 0 and len(message + "\n\n" + chunks[0]) < MAX_MESSAGE_LENGTH:
                message += "\n\n" + chunks.pop(0)
            messages.append(message)
        return messages


@client.event
async def on_ready():
    for channel_config in config:
        guild = client.get_guild(channel_config["guild_id"])
        if guild is None:
            print(f"Guild {channel_config['guild_id']} not found")
            exit(1)
        channel = guild.get_channel(channel_config["channel_id"])
        if channel is None:
            print(f"Channel {channel_config['channel_id']} not found")
            exit(1)

        # delete all messages sent by this bot
        async for message in channel.history(limit = 100):
            if message.author == client.user:
                print(f"Deleting message sent by me...")
                await message.delete()

        # Send new messages from the file
        for m in get_split_contents(channel_config["file"]):
            await channel.send(m,
                               # No link previews
                               suppress_embeds=True,
                               # Don't send any notifications
                               silent=True)
            print(f"Sent message to {channel.name} on {guild.name}")

    await client.close()

client.run(token)