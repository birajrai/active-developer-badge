import nextcord
from nextcord.ext import commands
import os

bot = commands.Bot()


@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name + ' (' + str(bot.user.id) + ')')


@bot.slash_command(description="Replies with pong!")
async def badge(interaction: nextcord.Interaction):
    await interaction.send("**You will be able to claim your Active Developer Badge within 24 hours**", ephemeral=True)

bot.run("Replace_With_Token")
