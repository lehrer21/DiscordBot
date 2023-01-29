import discord
import os
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents(messages=True, guilds=True, message_content=True,)

client = discord.Client(intents=intents)
# token = os.getenv('DISCORD_TOKEN')
token = os.getenv("DISCORD_TOKEN")
print(token)


@client.event
async def on_ready():
    print(f"{client.user} has logged in as a bot!")


@client.event
async def on_message(message):
    # Ignore messages from the bot itself.
    if message.author == client.user:
        return
    # Respond to hello.
    if message.content.startswith("$hello"):
        await message.channel.send(f"Hi, there, {message.author.display_name}!")
    # if message.content.startswith("$weather"):
    #     await message.channel.send("How should I know?")
    if message.content.starts


client.run(token)
