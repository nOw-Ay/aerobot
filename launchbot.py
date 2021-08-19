#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Aerobot - Script principal

# Initialisation des packages nécessaires

from discord.ext import commands

from embeds import *
from nasaapi import *

# Initialisation des modules et variables nécessaires
load_dotenv(dotenv_path="config.txt")
cdate, sdate = getsevdate("both")


# Définition des paramètres du bot

class DocBot(commands.Bot):
    def __init__(self):
        super().__init__(help_command=None, command_prefix=".")


pybot = DocBot()
APOD = fetchAPOD()


@pybot.event
async def on_ready():
    print("Le bot est prêt.")


@pybot.command(name='info')
async def info(ctx):
    await ctx.send(embed=infoemd)
    print("""Commande ".info" executée""")


@pybot.command(name='apod')
async def info(ctx):
    a = APOD["explanation"]
    APODdesc = a[0:1024]
    apodemd = discord.Embed(title=APOD["title"], url=f"https://apod.nasa.gov/apod/ap{sdate}.html", color=0x00e1ff)
    apodemd.add_field(name="Description", value=APODdesc, inline=False)
    apodemd.set_footer(text=f"Des limitations liées à Discord peuvent couper l'explication, le texte complet est disponible en cliquant sur le lien du titre. APOD est un service de la NASA et de la Michigan Technological University. {cdate}")
    apodemd.set_image(url=APOD["url"])

    await ctx.send(embed=apodemd)
    print("""Commande ".apod" executée""")


# Démarrage!

pybot.run(os.getenv("DISCORDTOKEN"))
