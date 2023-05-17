#!/usr/bin/env python3
from discord import Client, Intents
from configparser import ConfigParser
import sys
sys.path.append("/home/allebot/discord")
sys.path.append("/home/allebot/discord/plugins")
from plugins import allegro5
allegro5.basedir = "/home/allebot/discord"
from plugins import tins

intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith("? "):
        name = message.content[2:]
        if name == "tins":
            result = tins.run("", None)
        elif name in ["tins entrants", "tins *"]:
            result = tins.run(name[len("tins "):], None)
        else:
            result = allegro5.run(name, None)
        if result:
            if not result[0].startswith("http"):
                result[0] = "`" + result[0].replace(" (", "(") + "`"
            await message.channel.send("\n".join(result))

c = ConfigParser()
c.read("/etc/alledos.ini")
client.run(c["discord"]["token"])

