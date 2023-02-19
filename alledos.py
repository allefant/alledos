#!/usr/bin/env python3
from discord import Client, Intents
from configparser import ConfigParser
import sys
sys.path.append("/home/allebot/discord")
from plugins import allegro5
allegro5.basedir = "/home/allebot/discord"

intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith("? "):
        name = message.content[2:]
        result = allegro5.run(name, None)
        if result:
            if not result[0].startswith("http"):
                result[0] = "`" + result[0].replace(" (", "(") + "`"
            await message.channel.send("\n".join(result))

c = ConfigParser()
c.read("/etc/alledos.ini")
client.run(c["discord"]["token"])

