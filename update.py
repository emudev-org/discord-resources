#!/usr/bin/env python3
import discord
import json
import os

MAX_MESSAGE_LENGTH = 2000

config_path = "config.dev.json" if os.path.exists("config.dev.json") else "config.json"

config = json.load(open(config_path))

token = os.getenv("DISCORD_BOT_TOKEN")
if token is None:
    with open("discord_token", "r") as f:
        token = f.read().strip()
if token is None or token == "":
    print("No token found")
    exit(1)

def chunk_str(s, split_on, backup_split_on):
    messages = []

    chunks = s.split(split_on)
    while len(chunks) > 0:
        if len(chunks[0]) > MAX_MESSAGE_LENGTH:
            if backup_split_on is None:
                print(f"Message too long to split: {len(chunks[0])}")
                print(f"Bad message:\n\n{chunks[0]}")
                exit(1)

            messages += chunk_str(chunks.pop(0), backup_split_on, None)
            continue

        message = chunks.pop(0)

        while len(chunks) > 0 and len(message + split_on + chunks[0]) < MAX_MESSAGE_LENGTH:
            message += split_on + chunks.pop(0)

        messages.append(message)
        print(f"Message of size {len(message)} added")

    return messages

def get_split_contents(filename, split_on="\n\n", backup_split_on="\n"):
    print(f"Processing file {filename}")
    with open(filename, "r") as f:
        return chunk_str(f.read(), split_on, backup_split_on)

# Load and process each file
for channel_config in config:
    channel_config["messages"] = get_split_contents(channel_config["file"])

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

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

        print(f"Updating channel {channel.name} in {guild.name}...")

        # delete all messages sent by this bot
        async for message in channel.history(limit = 100):
            if message.author == client.user:
                print(f"Deleting message sent by me...")
                await message.delete()

        # Send new messages from the file
        for message in channel_config["messages"]:
            await channel.send(message,
                               # No link previews
                               suppress_embeds=True,
                               # Don't send any notifications
                               silent=True)
            print(f"Sent message to {channel.name} on {guild.name}")

    await client.close()

client.run(token)