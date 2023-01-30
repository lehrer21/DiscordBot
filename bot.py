import discord
import os
from dotenv import load_dotenv
import requests
import json
import logging


load_dotenv()
intents = discord.Intents(messages=True, guilds=True, message_content=True, )

client = discord.Client(intents=intents)
# token = os.getenv('DISCORD_TOKEN')
token = os.getenv("DISCORD_TOKEN")
print(token)

api_key = os.getenv("API_KEY")


def get_weather(city):
    try:
        base_url = "http://api.weatherapi.com/v1"
        complete_url = base_url + f"/current.json?key={api_key}" + "&q=" + city + "&aqi=no"
        response = requests.get(complete_url)
        result = response.json()

        city = result['location']['name']
        country = result['location']['country']
        time = result['location']['localtime']
        wcond = result['current']['condition']['text']
        celsius = result['current']['temp_c']
        fahrenheit = result['current']['temp_f']
        fclike = result['current']['feelslike_c']
        fflike = result['current']['feelslike_f']

        embed = discord.Embed(title=f"{city}"' Weather', description=f"{country}", color=0x14aaeb)
        embed.add_field(name="Temperature C°", value=f"{celsius}", inline=True)
        embed.add_field(name="Temperature F°", value=f"{fahrenheit}", inline=True)
        embed.add_field(name="Wind Condition", value=f"{wcond}", inline=False)
        embed.add_field(name="Feels Like F°", value=f"{fflike}", inline=True)
        embed.add_field(name="Feels Like C°", value=f"{fclike}", inline=True)
        embed.set_footer(text='Time: 'f"{time}")

        return embed
    except:
        embed = discord.Embed(title="No response", color=0x14aaeb)
        embed.add_field(name="Error", value="Oops!! Please enter a city name", inline=True)
        return embed


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
    if message.content.lower().startswith("$weather"):
        city = message.content[slice(9, len(message.content))].lower()
        result = get_weather(city)
        await message.channel.send(embed=result)


client.run(token)
