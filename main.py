import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(" >>Bot is Online<< ")


bot.run('NjgyMDUyNTA2NTk5MDMwODE5.XlXZBQ.BQ0WB8R8ORYpKNB27xSBMDNGN4Y')