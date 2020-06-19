import discord as ds
import secret

client = ds.Client()
TOKEN = pass

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print("-----------------")

client.run(TOKEN)