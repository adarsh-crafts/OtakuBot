# Import Python Modules
import discord
from discord.ext import commands
import datetime

# Import Data


#Help embed
def HelpEmbed(self):
    embed = discord.Embed(title='Avatar', description='Displays the avatar', color=0x050505)
    embed.add_field(name='Aliases', value='`avatar`, `pfp`', inline=False)
    embed.add_field(name='Usage', value=f'`{self.client.command_prefix}avatar`')
    embed.set_footer(text='{0.user.name}'. format(self.client))
    embed.timestamp = datetime.datetime.utcnow()

    return embed


class Avatar(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    # punch commands
    @commands.command(aliases=['pfp'])
    async def avatar(self, ctx, target: discord.user = ''):
        
        # self-avatar
        if target == '':

            embed = discord.Embed(description=f'{ctx.author.mention}\'s Profile pic', color=0xecce8b)
            embed.set_image(url='{}'.format(ctx.author.avatar_url))

            await ctx.send(embed=embed)
        
        else:

            embed = discord.Embed(color=0xecce8b)
            embed.set_image(url='{}'.format(target.avatar_url))

            await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Avatar(client))