from discord.ext import commands
import variables
from requests import get

client = commands.Bot(command_prefix='!')

@client.command(name='ip')
async def send_ip(ctx):
    ip = get('https://api.ipify.org').text
    await ctx.send(ip + ':25565')

@client.command(name='Hello')
async def send_kenobi(ctx):
    if ctx.message.content.lower().replace(' ', '') == '!hellothere':
        await ctx.send('General Kenobi')

# printing once connected to server
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

@client.event
async def on_command_error(ctx, error):
    # if isinstance(error, commands.errors.CheckFailure):
    await ctx.send('Command does not exist')

client.run(variables.TOKEN) # running bot