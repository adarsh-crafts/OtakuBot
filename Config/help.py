import discord
from discord.ext import commands
import datetime
import os


class Help(commands.Cog):
    
    def __init__(self, client):
        self.client = client


    # Help command
    @commands.command()
    async def help(self, ctx, word=''):
        if word=='':
            embed = discord.Embed(title='Akane\'s Command List', description=f'Here are all the available command categories, run `{self.client.command_prefix}help < category >` To view the list of commands from the category.\n\nRun {self.client.command_prefix}help < command > in order to get help on how to use the command.', color=0x050505)

            embed.set_footer(text='{0.user.name}'. format(self.client))
            embed.timestamp = datetime.datetime.utcnow()

            await ctx.author.send(embed=embed)

# setting up client
def setup(client):
    client.add_cog(Help(client))