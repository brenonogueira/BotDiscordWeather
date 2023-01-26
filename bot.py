# bot.py
import os
import random
import discord
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN_WEATHER = os.getenv('OPEN_WEATHER_TOKEN')

intents = discord.Intents.all()

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    response_pvh = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=porto velho&appid={TOKEN_WEATHER}&units=metric')
    response_pg = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=ponta grossa&appid={TOKEN_WEATHER}&units=metric')
    response_campinas = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=campinas&appid={TOKEN_WEATHER}&units=metric')
    response_niteroi = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=niteroi&appid={TOKEN_WEATHER}&units=metric')
    response_nv = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=nova venecia&appid={TOKEN_WEATHER}&units=metric')

    pvh_weather = int(response_pvh.json()['main']['temp'])
    pg_weather = int(response_pg.json()['main']['temp'])
    campinas_weather = int(response_campinas.json()['main']['temp'])
    niteroi_weather = int(response_niteroi.json()['main']['temp'])
    nv_weather = int(response_nv.json()['main']['temp'])

    response_message = f'Porto Velho: {pvh_weather}º \n' \
                       f'Ponta Grossa: {pg_weather}º \n' \
                       f'Campinas: {campinas_weather}º\nNiterói: {niteroi_weather}º \nNova Venécia: {nv_weather}º'

    if message.content == 'tempo':
        print(response_nv.json()['main']['temp'])
        await message.channel.send(response_message)


client.run(TOKEN)
