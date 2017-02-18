import discord

print("Starting Bot...")
print("Starting Discord Client")
client = discord.Client()
prefix = 'BB'
prefixalternative = ';'
token = 'TOKEN'

@client.event
async def on_ready():
    """
    Event handler, fires when the bot has connected and is logged in
    """
    print('Logged in as ' + client.user.name + " (" + client.user.id + ")")

    for instance in client.servers:
        await client.change_presence(game=discord.Game(name='Use ' + prefix + '/' + prefixalternative + 'help for a list of commands'))

@client.event
async def on_message(message):
    try:
        if message.content.startswith(prefix) or message.content.startswith(prefixalternative):
            await client.send_message(message.channel, 'debug')
        if message.server is None:
            await client.send_message(message.channel, 'Sorry, ' + client.user.name + 'cannot be used in DMs')
    except:
        pass

@client.event
async def on_member_join(member):
    await client.send_message(server.default_channel, member.nick + ' has joined ' + member.server.name)

@client.event
async def on_member_remove(member):
    await client.send_message(server.default_channel, member.nick + ' has left ' + member.server.name)


client.run(token)
