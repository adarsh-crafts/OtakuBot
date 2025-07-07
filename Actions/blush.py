# Import Python Modules
import discord
from discord.ext import commands
import random

# Import Data
from DataFiles import Actions_data, embedColors

class Blush(commands.Cog):
    
    def __init__(self, client):
        self.client = client


    # bonk commands
    @commands.command()
    async def blush(self, ctx, user: discord.User = 'none', *, Text=''):
        if user=='none':
            embed=discord.Embed(title='Something\'s making '+ctx.author.name+' blush.... ', color=random.choice(embedColors.colorList))
            embed.set_image(url= f'{random.choice(Actions_data.blush_gif_replies)}')
            await ctx.send(embed=embed)

        else:
            username = str(user.name)
            embed=discord.Embed(title= ctx.author.name+' is blushing because of '+user.name, description=Text, color=random.choice(embedColors.colorList))
            embed.set_image(url= f'{random.choice(Actions_data.blush_gif_replies)}')
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Blush(client))