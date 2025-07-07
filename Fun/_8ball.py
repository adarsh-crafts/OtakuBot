# Import Python modules
import discord
from discord.ext import commands
import random
import datetime

# Import Data
from DataFiles import ball_replyData

#Help embed
def HelpEmbed(self):
    embed = discord.Embed(title='8ball', description='Ask a yes/No question.', color=0x050505)
    embed.add_field(name='Aliases', value='`8ball`, `8b`', inline=False)
    embed.add_field(name='Usage', value=f'`{self.client.command_prefix}8ball <question>`')
    embed.set_footer(text='{0.user.name}'. format(self.client))
    embed.timestamp = datetime.datetime.utcnow()

    return embed

#Class
class _8ball(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    #8ball command
    @commands.command(aliases=['8ball', '8b'])
    async def _8ball(self, ctx, *, question):
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(ball_replyData.ball_responses)}')

def setup(client):
    client.add_cog(_8ball(client))