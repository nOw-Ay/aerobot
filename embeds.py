#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Embeds du "PyBot"

import discord

#embed commande ".info"

infoemd=discord.Embed(title=""":page_facing_up: Information""", description="""Aerobot a été conçu par <@325506093180780545>. Encore Protoype, il a pour objectif final de fournir plusieurs fonctionnalités en lien avec l'aéronautique et le spatial.""", color=0x00e1ff)
infoemd.set_author(name="Aerobot", icon_url="https://i.goopics.net/e4wl4.png")
infoemd.set_thumbnail(url="https://i.goopics.net/3bxYk.png")
infoemd.add_field(name=""":octagonal_sign: Aide""", value="""Pour obtenir la liste des commandes disponibles sur votre serveur, merci de taper ".help". :warning: , il est possible qu'il n'y ait rien ici pour le moment.""", inline=False)
infoemd.set_footer(text="Des erreurs peuvent arriver, n'hésitez pas à me contacter en cas de problème récurent.")

#embed commande ".apod" [Transférée sur le script principal]
