import requests
import string
import random
import discord
from discord import app_commands
from discord.ext import commands

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())
slash = bot.tree.command

@bot.event
async def on_ready():
    print(f'{bot.user} is ready!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="roc4et.de"))

#Slash commands:

#Password Slash command:
@slash(name="password", description="Generates a secure password for you.")
async def password(interaction: discord.Interaction,lengh:int):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(lengh))
    embed = discord.Embed(title=f"**Here is your password:**", url="https://roc4et.de",color=random.randint(0, 0xFFFFFF))
    embed.set_author(name="roc4et.de", url="https://roc4et.de/")
    embed.set_thumbnail(url="https://i.imgur.com/f4k498G.png")
    embed.set_footer(text="roc4et.de - Skyl1ne")
    embed.add_field(name="", value=f'<:arrow:1089578080718299136><:arrow:1089578080718299136>  ||{password}||', inline=True)
    await interaction.response.send_message(embed=embed,ephemeral=True)

#IP Slash command:
@slash(name="iplookup",description="Looks up an IPv4 address and gives you information about it.")
async def ip(interaction: discord.Interaction, ip_address: str):
        # Make a GET request to the API with the IP address as a parameter
    response = requests.get(f"https://ipapi.co/{ip_address}/json/")

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response as JSON
        data = response.json()
        # Create an embed to display the information for the given IP address
        embed = discord.Embed(title=f"__Information for IP address__: {data['ip']}", url="https://roc4et.de",color=random.randint(0, 0xFFFFFF))
        embed.add_field(name="City:", value=data['city'], inline=True)
        embed.add_field(name="Region:", value=data['region'], inline=True)
        embed.add_field(name="Country:", value=data['country_name'], inline=True)
        embed.add_field(name="Country Code:", value=data['country_code'], inline=True)
        embed.add_field(name="Continent Code:", value=data['continent_code'], inline=True)
        embed.add_field(name="Timezone:", value=data['timezone'], inline=True)
        embed.add_field(name="ISP:", value=data['org'], inline=True)
        embed.add_field(name="IP:", value=data['ip'], inline=True)
        embed.set_author(name="roc4et.de", url="https://roc4et.de/")
        embed.set_thumbnail(url="https://i.imgur.com/f4k498G.png")
        embed.set_footer(text="roc4et.de - Skyl1ne")
        await interaction.response.send_message(embed=embed,ephemeral=True)
    else:
        embed = discord.Embed(title=f"", url="https://roc4et.de",color=random.randint(0, 0xFFFFFF))
        embed.add_field(name="", value="An error occurred while making the request.Please try again.", inline=False)
        embed.set_author(name="roc4et.de", url="https://roc4et.de/")
        embed.set_thumbnail(url="https://i.imgur.com/ok1aY5E.png")
        embed.set_footer(text="roc4et.de - Skyl1ne")
        await interaction.response.send_message(embed=embed,ephemeral=True)

#About Slash command:
@slash(name="about",description="Shows information about the bot and credits.")
async def about(interaction:discord.Interaction):
    embed = discord.Embed(title=f"__Credits and information__:", url="https://roc4et.de",color=random.randint(0, 0xFFFFFF))
    embed.add_field(name="Credits:", value="**<a:developer:1089573762392920125> **  [roc4et#0001](https://discord.com/users/540958304910835735/)\n **<:website:1089572830569578648>  Website**: [roc4et.de](https://roc4et.de/)", inline=False)
    embed.add_field(name="Support:", value="**<:support:1089571270359785582> Support Server**: [.gg/roc4et](https://discord.com/invite/qbPScWt8ZV)", inline=False)
    embed.add_field(name="Invite:", value="**<a:support:1089570993091129414> Add me to your server**: [Invite!](https://discord.com/api/oauth2/authorize?client_id=1015685371297804340&permissions=1102196173847&redirect_uri=https%3A%2F%2Fdiscord.com%2Finvite%2FqbPScWt8ZV&response_type=code&scope=bot%20guilds.join%20applications.commands%20messages.read)", inline=False)
    embed.set_author(name="roc4et.de", url="https://roc4et.de/")
    embed.set_thumbnail(url="https://i.imgur.com/f4k498G.png")
    embed.set_footer(text="roc4et#0001 - Skyl1ne")
    await interaction.response.send_message(embed=embed,ephemeral=False)

#Normal commands:

@bot.command()
async def password(ctx):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(16))
    embed1 = discord.Embed(title=f"**Here is your password:**", url="https://roc4et.de",color=random.randint(0, 0xFFFFFF))
    embed1.set_author(name="roc4et.de", url="https://roc4et.de/")
    embed1.set_thumbnail(url="https://i.imgur.com/f4k498G.png")
    embed1.set_footer(text="roc4et.de - Skyl1ne")
    await ctx.send(embed=embed1)
    embed2 = discord.Embed(title=f"", url="https://roc4et.de",color=random.randint(0, 0xFFFFFF))
    embed2.add_field(name="", value=f'> ||{password}||', inline=True)
    embed1.set_author(name="roc4et.de", url="https://roc4et.de/")
    embed1.set_thumbnail(url="https://i.imgur.com/f4k498G.png")
    embed1.set_footer(text="roc4et.de - Skyl1ne")
    await ctx.send(embed=embed2)

@bot.command()
async def ip(ctx, ip_address: str):
    # Make a GET request to the API with the IP address as a parameter
    response = requests.get(f"https://ipapi.co/{ip_address}/json/")

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response as JSON
        data = response.json()
        # Create an embed to display the information for the given IP address
        embed = discord.Embed(title=f"__Information for IP address__: {data['ip']}", url="https://roc4et.de",color=random.randint(0, 0xFFFFFF))
        embed.add_field(name="City:", value=data['city'], inline=True)
        embed.add_field(name="Region:", value=data['region'], inline=True)
        embed.add_field(name="Country:", value=data['country_name'], inline=True)
        embed.add_field(name="Country Code:", value=data['country_code'], inline=True)
        embed.add_field(name="Continent Code:", value=data['continent_code'], inline=True)
        embed.add_field(name="Timezone:", value=data['timezone'], inline=True)
        embed.add_field(name="ISP:", value=data['org'], inline=True)
        embed.add_field(name="IP:", value=data['ip'], inline=True)
        embed.set_author(name="roc4et.de", url="https://roc4et.de/")
        embed.set_thumbnail(url="https://i.imgur.com/f4k498G.png")
        embed.set_footer(text="roc4et.de - Skyl1ne")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=f"", url="https://roc4et.de",color=random.randint(0, 0xFFFFFF))
        embed.add_field(name="", value="An error occurred while making the request.Please try again.", inline=False)
        embed.set_author(name="roc4et.de", url="https://roc4et.de/")
        embed.set_thumbnail(url="https://i.imgur.com/ok1aY5E.png")
        embed.set_footer(text="roc4et.de - Skyl1ne")
        await ctx.send(embed=embed)

bot.run("TOKEN")