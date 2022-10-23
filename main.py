# Imports
import discord
import json

from discord.ext import commands

# Variables
configFile = "./config.json"
playersFile = "./players.json"

token = ""

givenIntents = discord.Intents().all()

commandPrefix = "!"

client = commands.Bot(command_prefix=commandPrefix, intents=givenIntents)

# Events
@client.command(name="add")
@commands.has_permissions(administrator=True)
async def add_command(ctx, rlUser, discord):
	jsonData = {}

	with open(playersFile, "r") as players:
		jsonData = json.loads(players.read())

	jsonData[rlUser] = {
		"discord": discord
	}

	with open(playersFile, "w") as players:
		json.dump(jsonData, players)

	await ctx.message.reply(f"Added {rlUser}")
 
@client.command(name="listplayers")
@commands.has_permissions(administrator=True)
async def listplayers_command(ctx):
	jsonData = {}

	with open(playersFile, "r") as players:
		jsonData = json.loads(players.read())

	playerList = ""

	for player in jsonData:
		playerList += f"RL Username: {player},\n"
	
	sender = ctx.author

	await sender.send("Player list\n" + playerList)

@client.command(name="clearplayers")
@commands.has_permissions(administrator=True)
async def clearplayers_command(ctx):
    replace = "{}"
    
    with open(playersFile, "w") as players:
        players.write(replace)
    
    sender = ctx.author
    
    await ctx.reply("Cleared the player list")

# Main
def main():
	with open(configFile, "r") as config:
		data = config.read()
		
		jsonData = json.loads(data)
		
		token = jsonData['token']

	client.run(token=token)

def setupGame():
	pass

if __name__ == "__main__":
	main()