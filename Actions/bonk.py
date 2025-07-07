# Import Python Modules
import discord
from discord.ext import commands
import random

# Import Data
from DataFiles import Actions_data, embedColors

class Bonk(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bonk(self, ctx, user: discord.User = 'none',):
        if user=='none':
            embed=discord.Embed(title=ctx.author.name+' has bonked themselves.... ', color=random.choice(embedColors.colorList))
            embed.set_image(url= f'{random.choice(Actions_data.bonk_gif_replies)}')
            await ctx.send(embed=embed)
        
        else:
            embed=discord.Embed(title=ctx.author.name+' has bonked '+user.name, color=random.choice(embedColors.colorList))
            embed.set_image(url= f'{random.choice(Actions_data.bonk_gif_replies)}')
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Bonk(client))