import os
import discord
import markovhello

secret = os.environ["DISCORD_TOKEN"]

client = discord.Client()


@client.event
async def on_ready():
    print(f'Successfully connected! Logged in as {client.user}.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # greetings = ['hello', 'hi', 'yo']

    # word = message.content.split(" ")
    # for greeting in greetings:
    #     if greeting in word:
    #         message = "Hi there, bot!"
    #         await message.channel.send(message)

    if message.content.startswith('ey'):
        await message.channel.send(markovhello.text)
    elif message.content.startswith('good'):
        await message.channel.send('That is great!')
    elif message.content.startswith('bye'):
        await message.channel.send('Goodbye!')


client.run(secret)