import discord

print("Starting Bot...")
print("Starting Discord Client")
client = discord.Client()
prefix = 'BB'
prefix_alternative = ';'
token = 'TOKEN'

@client.event
async def on_ready():
    """
    Event handler, fires when the bot has connected and is logged in
    """
    print('Logged in as ' + client.user.name + " (" + client.user.id + ")")

    # Change nickname to nickname in configuration
    for instance in client.servers:
    await client.change_presence(game=discord.Game(name='Use ' + prefix + 'help or ' + prefix_alternative + 'help for help'))


@client.event
async def on_message(message):
    """
    Event handler, fires when a message is received in the server.
    :param message: discord.Message object containing the received message
    """
    try:
        if message.content.startswith(prefix):
            await client.send_message(message.channel, 'debug')
        if message.server is None:
            await client.send_message(message.channel, 'Sorry, ' + client.user.name + 'can't be used in DMs)

@client.event
async def on_member_join(member):
    await client.send_message(server.default_channel, member.nick + ' has joined ' + member.server.name)

@client.event
async def on_member_remove(member):
    await client.send_message(server.default_channel, member.nick + ' has left ' + member.server.name)


client.run(token)
