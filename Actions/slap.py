# Import Python Modules
import discord
from discord.ext import commands
import random

# Import Data
from DataFiles import Actions_data, embedColors

class slap(commands.Cog):
    
    def __init__(self, client):
        self.client = client


    # punch commands
    @commands.command()
    async def slap(self, ctx, user: discord.User = 'none'):
        if user=='none' or user==ctx.author.name:
            embed=discord.Embed(title=ctx.author.name+' has slapped themselves', description='Somebody help them...', color=random.choice(embedColors.colorList))
            embed.set_image(url= f'{random.choice(Actions_data.slapself_gif_replies)}')
            await ctx.send(embed=embed)


        else:
	        embed=discord.Embed(title=ctx.author.name+' has slapped '+user.name, color=random.choice(embedColors.colorList))
	        embed.set_image(url= f'{random.choice(Actions_data.slap_gif_replies)}')
	        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(slap(client))