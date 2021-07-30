import discord
from discord.ext import commands

TOKEN = 'ODcwNzI2NDU1MjE3MjM4MDE4.YQQ9NA.iM_CvFLVgZNLEiSeVTbogMZyNV0'
bot = commands.Bot(command_prefix='$')
@bot.command(pass_context=True)
async def test(ctx, arg):
    await ctx.send(arg)


bot.run(TOKEN)