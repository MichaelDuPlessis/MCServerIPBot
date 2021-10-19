import discord

# loading token from enviroment varibale
TOKEN = 'ODk5OTgxMzYzODkyMDkyOTU4.YW6q9Q.O6SL7U2OUP0t_v_qd4wh6YmTiAI' # token put in better place later

client = discord.Client()

@client.event
async def on_ready(): # printing once connected to server
    print(f'{client.user} has connected to Discord') 

client.run(TOKEN) # running bot