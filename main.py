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
	guildID = str(ctx.guild.id)

	with open(playersFile, "r") as players:
		jsonData = json.loads(players.read())

	try:
		jsonData[guildID][rlUser] = {
			"discord": discord
		}
	except KeyError:
		jsonData[guildID] = {}

		jsonData[guildID][rlUser] = {
			"discord": discord
		}

	with open(playersFile, "w") as players:
		json.dump(jsonData, players)

	await ctx.message.reply(f"Added {rlUser}")
 
@client.command(name="listplayers")
@commands.has_permissions(administrator=True)
async def listplayers_command(ctx):
	jsonData = {}
	guildID = str(ctx.guild.id)


	with open(playersFile, "r") as players:
		jsonData = json.loads(players.read())

	playerList = ""

	for player in jsonData[guildID]:
		playerList += f"- {player}\n"
	
	sender = ctx.author

	await sender.send("Player list by Rocket League username\n```" + playerList + "```")

@client.command(name="clearplayers")
@commands.has_permissions(administrator=True)
async def clearplayers_command(ctx):
	jsonData = {}
	guildID = str(ctx.guild.id)

	with open(playersFile, "r") as players:
		jsonData = json.loads(players.read())

	jsonData[guildID] = {}

	with open(playersFile, "w") as players:
		json.dump(jsonData, players)

	await ctx.message.reply("Cleared the player list")

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