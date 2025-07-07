# Import Python Modules
import discord
from discord.ext import commands
import random

# Import Data
from DataFiles import Actions_data, embedColors


def HelpEmbed(self):
    embed = discord.Embed(title='greet', description='Greet someone', color=0x050505)
    embed.add_field(name='Aliases', value='`greet`', inline=False)
    embed.add_field(name='Usage', value=f'`{self.client.command_prefix}greet <@user> [reason/message]`')

    return embed


class Greet(commands.Cog):
    
    def __init__(self, client):
        self.client = client


    # bonk commands
    @commands.command()
    async def greet(self, ctx, user: discord.User = 'none', *, Text=''):
        if user=='none':
            await ctx.send(ctx.author.mention + ' who do you wanna greet?')

        else:
            embed=discord.Embed(title = ctx.author.name+' greets '+user.name, color=random.choice(embedColors.colorList))
            embed.set_image(url= f'{random.choice(Actions_data.greet_gif_replies)}')
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Greet(client))