import discord
from discord.ext import commands

class Say(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    #commands
    @commands.command()
    async def say(self, ctx, str):
        embed = discord.Embed(description=str, color=0xf13582)

        await ctx.send(embed=embed)

    @commands.command()
    async def sayText(self, ctx, str):
        await ctx.send(str)
        

def setup(client):
    client.add_cog(Say(client))