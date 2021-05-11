# Importing neccary packages
import discord, random
from discord.ext import commands

# Prefix
client=commands.Bot(command_prefix='^')

# Pre-startup
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for ^help"))
    print('Bot online!') 


@client.command()
async def rock(ctx):
    embed=discord.Embed()
    embed.title='You choose rock!'
    replies=['I also choose rock! We tie!','I choose scissors! You beat me!','I choose paper! I win!',]
    embed.description=random.choice(replies)
    await ctx.send(embed=embed)

@client.command()
async def paper(ctx):
    embed=discord.Embed()
    embed.title='You choose paper!'
    replies=['I also choose paper! We tie!','I choose scissors! I win!','I choose rock! You win!',]
    embed.description=random.choice(replies)
    await ctx.send(embed=embed)

@client.command()
async def scissors(ctx):
    embed=discord.Embed()
    embed.title='You choose scissors!'
    replies=['I also choose scissors! We tie!','I choose rock! I win!','I choose paper! You win!',]
    embed.description=random.choice(replies)
    await ctx.send(embed=embed)

# Same thing but capitalized

@client.command()
async def Rock(ctx):
    embed=discord.Embed()
    embed.title='You choose rock!'
    replies=['I also choose rock! We tie!','I choose scissors! You beat me!','I choose paper! I win!',]
    embed.description=random.choice(replies)
    await ctx.send(embed=embed)

@client.command()
async def Paper(ctx):
    embed=discord.Embed()
    embed.title='You choose paper!'
    replies=['I also choose paper! We tie!','I choose scissors! I win!','I choose rock! You win!',]
    embed.description=random.choice(replies)
    await ctx.send(embed=embed)

@client.command()
async def Scissors(ctx):
    embed=discord.Embed()
    embed.title='You choose scissors!'
    replies=['I also choose scissors! We tie!','I choose rock! I win!','I choose paper! You win!',]
    embed.description=random.choice(replies)
    await ctx.send(embed=embed)


# Client secret
client.run('NzgxMzc4Nzk5MDkwMDA4MDg2.X78xtw.589DFBGYmKCMPkWweriRWK1w8Rs')