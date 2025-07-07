# Import Python Modules
import discord
from discord.ext import commands
import datetime
import os

# Import Data
from main import games_commands_list


#variables
s_link = os.environ['support_link']
commands_text =''
commands_list = []

def HelpEmbed(self):
    commands_text=''

    #Getting list of all files under the category
    for filename in os.listdir('./Games'):
        if filename.endswith('.py'):
            commands_list.append(f"{filename[:-3]}")

    #converting list to string
    i=0
    for ele in games_commands_list:
        if i == 0:
            commands_text += ele
                
        else:
            commands_text += ', '+ele
        i+=1


    embed = discord.Embed(title=f':game_die: Games', color=0x050505)
    embed.add_field(name=f'Commands ['+str(i)+']',value='```'+commands_text+'```', inline=False)
    embed.set_footer(text='{0.user.name}'. format(self.client))
    embed.timestamp = datetime.datetime.utcnow()

    return embed



class Fun(commands.Cog):
    
    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(Fun(client))