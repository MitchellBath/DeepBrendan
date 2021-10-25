import os

import discord
import random
from dotenv import load_dotenv
# To keep the server alive
#import keep_alive

# Text Generation stuff
from textgenrnn import textgenrnn
tg = textgenrnn()


load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']
#TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = os.getenv('DISCORD_GUILD')

# Old stuff for getting members
intents = discord.Intents.default()
intents.members = True
#client = discord.Client(intents = intents)

client = discord.Client()
brendandata = ["transformers"]
xandata = ["i love warhammer"]
mitchdata = ["my brendan neural network"]
kadendata = ["im just fuckin wit cha man"]
daviddata = ["heh"]

# Variables
historysize = 10000
epochs = 10
gens = 2

@client.event
async def on_ready():
	print(f'{client.user.name} has connected to Discord!')	

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content == "!init":
		# Brendan
		await message.channel.send("<:brendanpog:796963750984810506> fetching brendan slang")
		async for elem in message.channel.history(limit=historysize):
			if elem.author.name == "BluePineapple72":
				if elem.content != '':
					brendandata.append(elem.content)
					print(elem.content)
		await message.channel.send("initialization <:brendanpog:796963750984810506> complete <:brendanpog:796963750984810506>")

		# Mitch
		await message.channel.send("<:mitchglare:755289903339798599> fetching mitch slang")
		async for elem in message.channel.history(limit=historysize):
			if elem.author.name == "beingDevisor":
				if elem.content != '':
					mitchdata.append(elem.content)
					print(elem.content)
		await message.channel.send("initialization <:mitchglare:755289903339798599> complete <:mitchglare:755289903339798599>")

		# Xan
		await message.channel.send("<:squad2xan:816901536109690890> fetching xan slang")
		async for elem in message.channel.history(limit=historysize):
			if elem.author.name == "Xan":
				if elem.content != '':
					xandata.append(elem.content)
					print(elem.content)
		await message.channel.send("initialization <:squad2xan:816901536109690890> complete <:squad2xan:816901536109690890>")

		# Kaden
		await message.channel.send("<:disgustedkaden:819098222106247218> fetching kaden slang")
		async for elem in message.channel.history(limit=historysize):
			if elem.author.name == "Fredrick Freaker":
				if elem.content != '':
					kadendata.append(elem.content)
					print(elem.content)
		await message.channel.send("initialization <:disgustedkaden:819098222106247218> complete <:disgustedkaden:819098222106247218>")

		# David
		await message.channel.send("<:squad2david:816901536118210560> fetching david slang")
		async for elem in message.channel.history(limit=historysize):
			if elem.author.name == "Ketasive":
				if elem.content != '':
					daviddata.append(elem.content)
					print(elem.content)
		await message.channel.send("initialization <:squad2david:816901536118210560> complete <:squad2david:816901536118210560>")
		await message.channel.send("all initializations complete. simulate your friends.")

		# Text Generation Data setup


	# Message handling
	if message.content == '!brendanh':
		result = random.choice(brendandata)
		print(result)
		await message.channel.send(result)

	elif message.content == '!mitchh':
		result = random.choice(mitchdata)
		print(result)
		await message.channel.send(result)

	elif message.content == '!davidh':
		result = random.choice(daviddata)
		print(result)
		await message.channel.send(result)

	elif message.content == '!kadenh':
		result = random.choice(kadendata)
		print(result)
		await message.channel.send(result)

	elif message.content == '!xanh':
		result = random.choice(xandata)
		print(result)
		await message.channel.send(result)

	# Generated messages
	elif message.content == '!brendan':
		tg.reset()
		tg.train_on_texts(brendandata, num_epochs=epochs, gen_epochs=gens)
		result = tg.generate(1)
		await message.channel.send(result)
	elif message.content == '!mitch':
		tg.reset()
		tg.train_on_texts(mitchdata, num_epochs=epochs, gen_epochs=gens)
		result = tg.generate(1)
		await message.channel.send(result)
	elif message.content == '!david':
		tg.reset()
		tg.train_on_texts(daviddata, num_epochs=epochs, gen_epochs=gens)
		result = tg.generate(1)
		await message.channel.send(result)
	elif message.content == '!kaden':
		tg.reset()
		tg.train_on_texts(kadendata, num_epochs=epochs, gen_epochs=gens)
		result = tg.generate(1)
		await message.channel.send(result)
	elif message.content == '!xan':
		tg.reset()
		tg.train_on_texts(xandata, num_epochs=epochs, gen_epochs=gens)
		result = tg.generate(1)
		await message.channel.send(result)

	elif message.content == 'raise-exception':
		raise discord.DiscordException

#keep_alive.keep_alive()
client.run(TOKEN)
