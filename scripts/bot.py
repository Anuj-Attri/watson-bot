import discord as ds

client = ds.Client()
TOKEN = 'NzIzNDAzNjcwNzU0MTY0Nzc2.XuxT8Q.k1gnZ42ozjYySTxDKulZdpPMptM'

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print("-----------------")

client.run(TOKEN)