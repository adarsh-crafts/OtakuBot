import discord
from discord.ext import commands


class Info(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="to b.help"))

    #Info cmd
    @commands.command()
    async def info(srlf, ctx):
        embed = discord.Embed()



def setup(client):
    client.add_cog(Info(client))