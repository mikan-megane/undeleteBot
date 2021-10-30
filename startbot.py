import discord
from discord.ext import commands

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
    if message.content.startswith(('.au ','!'))
        return
    embed = discord.Embed(
        # title="📣 ボイスチャンネル",
        description=message.content,
        color=discord.Colour.red()
    )
    embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
    await message.channel.send(embed=embed)

bot.run('OTAzNjQzNTQxMzM3NjgxOTcy.YXv9oQ.n65iSloeoRG0hVFeylToshF4UnU')