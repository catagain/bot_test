import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='喵')

@bot.event
async def on_ready():
    print(" >>Bot is Online<< ")

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')

bot.run("NjgyMDUyNTA2NTk5MDMwODE5.XlYA2w.60JMZPVm2gZRLC7gfqEAyyouuAQ", bot = True)