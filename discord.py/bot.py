#!/home/pi/marcus-server/discord.py/venv/bin/python3

# Imports

from secret import botToken
from http import client
import discord
from discord import guild
from discord.ext import commands
from random import choice

# Setup
intents = discord.Intents.all()

client = commands.Bot(command_prefix='d!', intents=intents)
E = 'Placeholder'


# Main Code

@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='you'))

@client.command()
async def kick(ctx, member: commands.MemberConverter):
    print(f'{ctx.author} kicked {member} from {ctx.guild.name}')
    await ctx.send(f'{member} was kicked!')
    await member.send(f"You have been kicked from {ctx.guild.name}")
    await ctx.guild.kick(member)
"""
    await ctx.send(f'{member} is not a member of {ctx.guild.name}')
    print(f"{ctx.author} tried to kick {member} but they were not in the server")
"""

@client.command("Hello")
async def ban(ctx, member: commands.MemberConverter):
    print(f'{ctx.author} banned {member} from {ctx.guild.name}')
    await ctx.send(f'{member} was banned')
    await member.send(f"You have been banned from {ctx.guild.name}")
    await ctx.guild.ban(member)

@client.command()
async def message(ctx, *args):
    """
    Repeats what you send it but with a '!'
    """
    text = " ".join(args[:])
    print(f"{ctx.author} sent '{text}' in {ctx.channel} in {ctx.guild.name}")
    await ctx.send(f'{text}!')

@client.command()
async def ping(ctx):
    """
    Get the ping to the server
    """
    latency = round(client.latency, 1)
    print(f"Latency for {ctx.author} in {ctx.guild.name} is {latency} ms of latency")
    await ctx.send('Pong! {0} ms of latency'.format(latency))

@client.command(aliases=['8ball'])
async def _8Ball(ctx, *, question):
    responses = [
                'It is certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes definitely.',
                'You may rely on it.',
                'As I see it, yes.',
                'Most likely.',
                'Outlook good.',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                "Don't count on it.",
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful.'
    ]
    await ctx.send(f'Question: {question}\nAnswer: {choice(responses)}')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)


@client.event
async def on_member_join(member):
    server = client.get_guild(1165490223187251331)
    channel = client.get_channel(1306140428474650666)
    print(f"{member.name} joined {server.name}")
    await member.send(f'Welcome to the {server.name} server, {member.name}! Hope you enjoy it here!:partying_face:')
    await channel.send(f'Welcome to the server {member.mention}! :partying_face:')

# End Code

client.run(botToken.token)
