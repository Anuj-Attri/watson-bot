import discord
import os

client = discord.Client()
TOKEN = process.env.bot_token

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print("-----------------")

client.run(TOKEN)