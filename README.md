# **[roc4et.de](http://roc4et.de/ "roc4et.de") Discord bot**
This is a Python script that defines a Discord bot with three slash commands: `password`, `iplookup`, and `about`. The `password` command generates a secure password, the iplookup command looks up information about an IPv4 address, and the `about` command shows information about the bot and credits.

## Requirements
- Python 3.8 or higher
- `discord` and `requests` modules

## Installation
1. Clone the repository.
2. Install the `discord` and `requests` modules by running` pip install discord requests` in your terminal.
3. Create a new Discord bot and copy its token.
4. Rename `config.example.ini` to `config.ini` and fill in the required information (such as the bot token).
5. Run the script with `python main.py`.

## Usage
After running the script, you can interact with the bot using the following commands:

- `.password <length>` : Generates a secure password with the given length.
- `.iplookup <ip_address>` : Looks up information about the given IPv4 address.
- `.about` : Shows information about the bot and credits.

## Code documentation
### Importing modules

```python
import requests
import string
import random
import discord
from discord import app_commands
from discord.ext import commands
```
This code block imports the necessary modules for the bot: `requests`, `string`, `random`, and `discord`. The `app_commands` module is also imported from `discord`, but it is not used in this script.

### Creating the bot instance
```python
bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())
```
This code block creates a `bot` instance with the command prefix set to `.` and all intents enabled.

### Syncing slash commands

```python
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
```
This code block defines the `slash` variable as `bot.tree.command`, which is used to create slash commands. The `on_ready` event is then defined, which syncs the slash commands and sets the bot's presence.

### Password Command
```python
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
```
This code block defines the `password` command as a slash command with the name "password" and the description "Generates a secure password for you".

### IP command
The ip command retrieves information about a given IP address using the ipapi.co API.

#### Syntax
`.ip <ip_address>`

#### Parameters
| Parameter  |  Description |
| :------------  | :------------ |
|  ip_address | The IP address for which to retrieve information. Must be a string.  |




#### Example Usage
`.ip 8.8.8.8`

##### Response
The response will be an embedded message containing the following fields:

|  Field |  Description |
| :------------ | :------------ |
| City  |  	The city associated with the IP address |
| Region  | The region associated with the IP address  |
| Country  | 	The country associated with the IP address  |
| Country Code  | The ISO code of the country associated with the IP address  |
| Continent Code  |  The ISO code of the continent associated with the IP address |
|  Timezone | The timezone associated with the IP address  |
|   ISP | The ISP associated with the IP address  |
|   IP |  The IP address for which information was requested |

##### Example Response

```yaml
Information for IP address: 8.8.8.8
City: Mountain View
Region: California
Country: United States
Country Code: US
Continent Code: NA
Timezone: America/Los_Angeles
ISP: Google LLC
IP: 8.8.8.8
```

#### Permissions
The `ip` command requires the `embed_links` permission to be enabled for the bot in order to display the embedded message.
