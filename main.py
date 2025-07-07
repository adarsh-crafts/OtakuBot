# Import Python Modules
import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='b.')
client.remove_command('help')

actions_commands_list =[]
fun_commands_list=[]
misc_commands_list=[]
games_commands_list=[]

# Load Action cog files - Command Files
for filename in os.listdir('./Actions'):
    if filename.endswith('.py'):
        file = f"{filename[:-3]}"

        client.load_extension(f'Actions.{file}')
        actions_commands_list.append(file)


# Load Config cog files - Startup & command files
#for filename in os.listdir('./Config'):
#    if filename.endswith('.py'):
#        client.load_extension(f'Config.{filename[:-3]}')


# Load Fun cog files - Command Files
for filename in os.listdir('./Fun'):
    if filename.endswith('.py'):
        file = f"{filename[:-3]}"

        client.load_extension(f'Fun.{file}')
        fun_commands_list.append(file)


# Load Games cog files - Command Files
for filename in os.listdir('./Games'):
    if filename.endswith('.py'):
        file = f"{filename[:-3]}"

        client.load_extension(f'Games.{file}')
        games_commands_list.append(file)


# Load Misc cog files - Command Files
for filename in os.listdir('./Misc'):
    if filename.endswith('.py'):
        file = f"{filename[:-3]}"

        client.load_extension(f'Misc.{file}')
        misc_commands_list.append(file)


############################# RUN #############################
client.run(os.environ['key'])