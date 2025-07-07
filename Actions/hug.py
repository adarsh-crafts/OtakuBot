# Import Python Modules
import discord
from discord.ext import commands
import random

# Import Data
from DataFiles import Actions_data, embedColors

class hug(commands.Cog):
    
    def __init__(self, client):
        self.client = client


    # hug commands
    @commands.command()
    async def hug(self, ctx, user: discord.User = 'none'):
        if user=='none':
            await ctx.send('Who are you hugging dummy? lol')

        elif ctx.author == user:
            embed=discord.Embed(title=ctx.author.name+' needs a hug, they\'re trynna hug themselves', color=random.choice(embedColors.colorList))
            await ctx.send(embed=embed)

        else:
	        embed=discord.Embed(title=ctx.author.name+' has hugged '+user.name, color=random.choice(embedColors.colorList))
	        embed.set_image(url= f'{random.choice(Actions_data.hug_gif_replies)}')
	        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(hug(client))