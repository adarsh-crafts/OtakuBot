# Import Python Modules
import discord
from discord import client
from discord.ext import commands
import random

# Import Data
from DataFiles import Actions_data, embedColors

class punch(commands.Cog):
    
    def __init__(self, client):
        self.client = client


    # punch commands
    @commands.command()
    async def punch(self, ctx, user: discord.User = 'none'):
        if user=='none':
            await ctx.send(f'Who are you punching? dummy...\n`{self.client.command_prefix}punch <mention user>`')

        elif ctx.author == user:
            ctx.send('You can\'t punch yourself...')

        else:
	        embed=discord.Embed(description=ctx.author.name+' has punched '+user.name, color=random.choice(embedColors.colorList))
	        embed.set_image(url= f'{random.choice(Actions_data.punch_gif_replies)}')
	        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(punch(client))