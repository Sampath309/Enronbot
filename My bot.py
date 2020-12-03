import discord
from discord.ext import commands
import random
from discord.ext.commands import CommandNotFound
import keep_alive
import os
import datetime


client = commands.Bot(command_prefix="E!")
client.remove_command("help")

rules = [":one: Treat every member of our Discord with respect.",
":two:  Absolutely no spam or solicitation. This includes advertising of any kind for any thing.",
":three:  No one should invite player to your manor if they are not your friends.",
":four: If you break these rules, you may be subject to a mute, kick, ban or whatever staff believes is the correct course of action."]

reaction_title=""
reactions = {}

@client.command(name="reaction_create_post")
async def reaction_create_post(context):

	embed = discord.Embed(title="Create Reation Post", color=0x8cc542)
	embed.set_author(name="Enron Bot")
	embed.add_field(name="Set Title", value="E!reaction_set_title\"New Title\"", inline=False)
	embed.add_field(name="Add Role", value="E!reaction_add_role @Role EMOJI_HERE", inline=False)

	await context.send(embed=embed)
	await context.message.delete()

@client.command(name="reaction_set_title")
async def reaction_set_title(context, new_title):

	global reaction_title
	reaction_title = new_title
	await context.send("The title for the message is now " + reaction_title + "!")
	await context.message.delete()

@client.command(name="reaction_add_role")
async def reaction_set_role(context, role: discord.Role, reaction):

	if role != None:
		reaction[role.name] = reaction
		await context.send("Role "+ role.name + " has been added with emoji" + reaction)
	else:
		await context.send("Please try again!")

	print(reactions)

	global reaction_title
	reaction_title = new_title
	await context.send("The title for the message is now " + reaction_title + "!")
	await context.message.delete()

@client.command(name="help")
async def help(context):

	myEmbed = discord.Embed(title="Enron-Bot Command List!", description="You can find my support server here!", color=0xFF0000)
	myEmbed.add_field(name=":zany_face: Fun", value="E!fun")
	myEmbed.add_field(name=":handshake: Support", value="E!support")
	myEmbed.add_field(name=":clipboard:Bot Stats", value="E!Stats")
	myEmbed.add_field(name=":mute: Mod", value="E!mod")
	myEmbed.add_field(name=":cyclone: Other", value="E!other")
	await context.message.channel.send(embed=myEmbed)


@client.command(name="version")
async def version(context):

	embedVar = discord.Embed(title="Current Version", description="The bot is in Version 1.0", color=0xFF0000)
	embedVar.add_field(name="Version Code", value="v1.0.", inline=False)
	embedVar.add_field(name="Date Released", value="December 2nd, 2020", inline=False)
	embedVar.set_footer(text="Type E! before every command")

	await context.message.channel.send(embed=embedVar)

@client.command(name="fun")
async def fun(context):
	embedVar = discord.Embed(title=":zany_face: Fun", color=0xFF0000)
	embedVar.add_field(name="dog", value="sends a random dog images.", inline=False)
	embedVar.add_field(name="cat", value="sends a random cat images.", inline=False)
	embedVar.add_field(name="panda", value="sends a random panda images.", inline=False)
	embedVar.add_field(name="sparrow", value="sends a random sparrow images.", inline=False)
	embedVar.set_footer(text="Type E! before every command")
	await context.message.channel.send(embed=embedVar)

@client.command(name="support")
async def support(context):
	
	embedVar = discord.Embed(title=":handshake: Support", color=0xFF0000)
	embedVar.add_field(name="server", value="gives you link of offcial server.", inline=False)
	embedVar.add_field(name="invite", value=" gives you link to add me to your server.", inline=False)
	embedVar.set_footer(text="Type E! before every command")
	await context.message.channel.send(embed=embedVar)

@client.command(name="mod")
async def mod(context):

	myEmbed = discord.Embed(title=":mute:Mod", color=0xFF0000)
	myEmbed.add_field(name="delete <amount>", value="deletes an amount of messages.", inline=False)
	myEmbed.add_field(name="kick <@user> <reason>", value="kick the user from a server", inline=False)
	myEmbed.add_field(name="ban <@user> <reason>", value="ban the user from a server", inline=False)
	myEmbed.set_footer(text="Type E! before every command")
	await context.message.channel.send(embed=myEmbed)

@client.command(name="stats")
async def stats(context):

	myEmbed = discord.Embed(title=":clipboard:Bot Stats", color=0xFF0000)
	myEmbed.add_field(name="servers", value="says how many servers im in.", inline=False)
	myEmbed.set_footer(text="Type E! before every command")
	await context.message.channel.send(embed=myEmbed)

@client.command(name="other")
async def other(context):
	
	embedVar = discord.Embed(title=":cyclone: - Other", color=0xFF0000)
	embedVar.add_field(name="ping", value="returns pong and says how many ms it took to respond.", inline=False)
	embedVar.add_field(name="hello", value=" says hi!", inline=False)
	embedVar.set_footer(text="Type E! before every command")
	await context.message.channel.send(embed=embedVar)

@client.command(name="servers")
async def servers(context):
	embedVar = discord.Embed(title=f'I am serving {len(client.guilds)} servers!', color=0xFF0000)
	for server in client.guilds:
		print(server.name)
	await context.message.channel.send(embed=embedVar)

@client.command()
async def rule(ctx,*,number):
	await ctx.send(rules[int(number)-1])

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error
@client.command()
async def hello(ctx):
	await ctx.send("Hi !, I'm Enron a discord bot.")

@client.event
async def on_ready():
	
	await client.change_presence(status=discord.Status.online, activity=discord.Game('enron.gg | E!help'))

@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
	await ctx.channel.purge(limit = amount)
	await ctx.send('The message has been deleted!')
	await context.message.delete()

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(context, member: discord.Member):

	await member.kick()
	await context.send ('User ' + member.display_name + ' has been kicked')

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(context, member: discord.Member):

	await member.ban()
	await context.send (' User ' + member.display_name + ' has been baned ')

@client.command(name="dog")
async def dog(context):

	images = ["dog.jpeg", "dog2.jpeg", "dog3.jpeg", "dog4.jpeg"]

	random_image = random.choice(images)

	await context.send(file=discord.File(random_image))

@client.command(name="cat")
async def cat(context):

	images = ["cat1.jpeg", "cat2.jpeg", "cat3.jpeg", "cat4.jpeg"]

	random_image = random.choice(images)

	await context.send(file=discord.File(random_image))

@client.command(name="sparrow")
async def sparrow(context):

	images = ["sparrow1.jpeg", "sparrow2.jpeg", "sparrow3.jpeg", "sparrow4.jpeg"]

	random_image = random.choice(images)

	await context.send(file=discord.File(random_image))

@client.command(name="panda")
async def panda(context):

	images = ["panda1.jpeg", "panda2.jpeg", "panda3.jpeg", "panda4.jpeg"]

	random_image = random.choice(images)

	await context.send(file=discord.File(random_image))

@client.event
async def on_message(message):

	if message.content == 'E!invite':

		await message.author.send("Here the link to invite me: https://discord.com/api/oauth2/authorize?client_id=783328484927340585&permissions=2110782711&scope=bot")

	if message.content == 'E!server':

		await message.author.send("https://discord.gg/DxjyWBSsCV")

	await client.process_commands(message)

@client.command()
async def ping(ctx):
	await ctx.send(f'Ping: {round(client.latency * 1000)}ms')

keep_alive.keep_alive()
token = os.environ.get("Token")
client.run(token)