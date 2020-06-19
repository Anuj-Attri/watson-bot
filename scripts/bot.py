import discord as ds

client = ds.Client()
TOKEN = ' '

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print("-----------------")

client.run(TOKEN)