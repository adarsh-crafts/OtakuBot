import discord
from discord.ext import commands
import random
import datetime

# Import Data


#Help
def HelpEmbed(self):
    embed = discord.Embed(title='Flip coin', description='Flips a coin & returns Heads or Tails.', color=0x050505)
    embed.add_field(name='Aliases', value='`flip`', inline=False)
    embed.add_field(name='Usage', value=f'`{self.client.command_prefix}flip`')
    embed.set_footer(text='{0.user.name}'. format(self.client))
    embed.timestamp = datetime.datetime.utcnow()

    return embed
            


class Flip(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    coin = ['Heads', 'Tails']

    # punch commands
    @commands.command()
    async def flip(self, ctx):
        side= random.choice(Flip.coin)
        
        await ctx.send('**'+ctx.author.name+'** it\'s '+side+'!!')


def setup(client):
    client.add_cog(Flip(client))