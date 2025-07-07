# Import Python Modules
import discord
from discord import client
from discord.ext import commands
import random

# Import Data
from DataFiles import Actions_data, embedColors

class Kick(commands.Cog):
    
    def __init__(self, client):
        self.client = client


    # Kick commands
    @commands.command()
    async def kick(self, ctx, user: discord.User = 'none'):
        if user=='none':
            await ctx.send(f'Who are you kicking? dummy...\n`{self.client.command_prefix}kick <mention user>`')

        else:
            if ctx.author == user:
                embed=discord.Embed(title=ctx.author.name+' You can\'t kick yourself... lol', color=random.choice(embedColors.colorList))
                await ctx.send(embed=embed)
            
            else:
                kick_type = random.choice(Actions_data.chances)

                if kick_type in [9, 10]:
                    output = random.choice(Actions_data.kickmiss_gif_replies)

                    embed=discord.Embed(title=ctx.author.name+' tried to kick '+user.name+', but they dodged it', color=random.choice(embedColors.colorList))
                    embed.set_image(url= output)
            
                else:
                    output = random.choice(Actions_data.kick_gif_replies)
                    embed=discord.Embed(title=ctx.author.name+' has kicked '+user.name, color=random.choice(embedColors.colorList))
                    embed.set_image(url= output)

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Kick(client))