import discord
import os
from discord.ext import commands

BOT_TOKEN = os.getenv('BOT_TOKEN')
if BOT_TOKEN == None:
    raise Exception("not set BOT_TOKEN env.")

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message_delete(message: discord.Message):
    if message.author.bot:
        return
    if message.content.startswith(('.au ','!')):
        return
    embed = discord.Embed(
        # title="📣 ボイスチャンネル",
        description=message.content,
        color=discord.Colour.red()
    )
    embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
    await message.channel.send(embed=embed)

bot.run(BOT_TOKEN)