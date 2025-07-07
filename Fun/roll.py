# Import Python Modules
import discord
from discord.ext import commands
import random
import datetime


#Help EMbed
def HelpEmbed(self):
    embed = discord.Embed(title='Roll', description='Rolls a number from 1-100', color=0x050505)
    embed.add_field(name='Aliases', value='`roll`', inline=False)
    embed.add_field(name='Usage', value=f'`{self.client.command_prefix}roll`')
    embed.set_footer(text='{0.user.name}'. format(self.client))
    embed.timestamp = datetime.datetime.utcnow()    

    return embed


class roll(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    # punch commands
    @commands.command()
    async def roll(self, ctx):
        num= random.randint(1, 101)
        string= str(num)
        await ctx.send('**'+ctx.author.name+'** rolls **'+string+'**(1-100)')


def setup(client):
    client.add_cog(roll(client))