## first install ChatterBot, then chatterbot-corpus

import discord

client = discord.Client()

from chatterbot import ChatBot

TOKEN = open("token.txt", "r").read()

bot = ChatBot(
    'Watts',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.sqlite3',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!Watts'):
        new_input = message.content[6:]
        print (new_input)
        channel = message.channel
        response = bot.get_response(new_input)
        msg = response
        await channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
