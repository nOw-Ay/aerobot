#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os
import pytz
from urllib import *
from datetime import datetime
from dotenv import load_dotenv

load_dotenv(dotenv_path="config.txt")

nasatoken = os.getenv("NASATOKEN")

def getsevdate(form):
    localt = pytz.timezone('Europe/Paris').localize(datetime.now())
    ust = localt.astimezone(pytz.timezone('US/Eastern'))
    if form == "composed":
        return ust.strftime('%Y-%m-%d')
    elif form == "simple":
        return ust.strftime('%y%m%d')
    elif form =="both":
        return ust.strftime('%Y-%m-%d'), ust.strftime('%y%m%d')
    else:
        raise TypeError("""Vous n'avez pas donné un argument correct à la fonction, essayez "simple" ou "composed".""") 

def fetchAPOD():
  URL_APOD = "https://api.nasa.gov/planetary/apod"
  params = {
      'api_key':nasatoken,
      'date':getsevdate("composed"),
      'hd':'True'
  }
  response = requests.get(URL_APOD,params=params).json()
  return response

def get_dailyAPOD():
    path='images'
    date = getsevdate("composed")
    files = [os.path.splitext(filename)[0] for filename in os.listdir(path)]
    for name in files:
        if name == getsevdate("composed"):
            return "L'APOD du jour est déjà importée!"
    APODimage = fetchAPOD()
    request.urlretrieve(APODimage["url"],f"{path}/{date}.jpg")
    return "APOD du jour importée !"
 
