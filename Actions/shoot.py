# Import Python Modules
import discord
from discord.ext import commands
import random

# Import Data
from DataFiles import Actions_data, embedColors

class Shoot(commands.Cog):
    
    def __init__(self, client):
        self.client = client


    # bonk commands
    @commands.command()
    async def shoot(self, ctx, user: discord.User = 'none', *, Text=''):
        if user=='none':
            await ctx.send('Shoot who? you started shooting in the air in public and got arrested.')

        elif user==ctx.author:
            embed=discord.Embed(title= ctx.author.name+' no... you don\'t have to do that... ', description=Text, color=random.choice(embedColors.colorList))
            embed.set_image(url= f'{random.choice(Actions_data.self_shoot_gif_replies)}')
            
            await ctx.send(embed=embed)

        else:
            username = str(user.name)
            embed=discord.Embed(title= ctx.author.name+' shot down '+user.name, description=Text, color=random.choice(embedColors.colorList))
            embed.set_image(url= f'{random.choice(Actions_data.shoot_gif_replies)}')
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Shoot(client))