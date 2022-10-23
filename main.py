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
async def on_message(ctx, rlUser, discord):
	jsonData = {}

	with open(playersFile, "r") as players:
		jsonData = json.loads(players.read())

	jsonData[rlUser] = {
		"discord": discord
	}

	with open(playersFile, "w") as players:
		json.dump(jsonData, players)

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