import discord
from discord.ext import commands

TOKEN = 'ab6ad7bfc501ad4df77982b0c56ec48dc9e0a5a2855df71a9a87b116e329a8f2'
bot = commands.Bot(command_prefix='$')
@bot.command(pass_context=True)
async def test(ctx, arg):
    await ctx.send(arg)


bot.run(TOKEN)