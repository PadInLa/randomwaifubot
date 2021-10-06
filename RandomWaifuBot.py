import tweepy
import urllib.request
import numpy as np
import time
import os
import random
from random import randint
from os import path
from keys import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def rollFactor():
    # Raises or lowers depending on likes *To be implemented*
    # cursedfactor =
    cursedfactor = round(random.uniform(0.3, 2.0), 1)
    return cursedfactor

def rollSeed():
    seednumber = randint(1, 99999)
    seednumberstr = str(seednumber)
    if len(seednumberstr) == 4:
        seednumberstr = "0" + seednumberstr
    elif len(seednumberstr) == 3:
        seednumberstr = "00" + seednumberstr
    elif len(seednumberstr) == 2:
        seednumberstr = "000" + seednumberstr
    elif len(seednumberstr) == 1:
        seednumberstr = "0000" + seednumberstr
    return seednumberstr

def WaifuPost():
    # GAN psi level
    resfactor = rollFactor()

    # Seed number
    res = rollSeed()

    if os.path.exists("D:\\Archivos\\Documentos\\RandomWaifuBot\\seedData.txt"):
        f = open("D:\\Archivos\\Documentos\\RandomWaifuBot\\seedData.txt", "r")
        salir = False
        line = f.readline()
        print(line)
        while line != "" and salir != True:
            fields = line.split(";")
            print(fields)
            if fields[0] == res and fields[1] == resfactor:
                salir = True
            line = f.readline()

        if salir == False:
            f = open("D:\\Archivos\\Documentos\\RandomWaifuBot\\seedData.txt", "a")
            f.write(res + ";" + str(resfactor) + "\n")
            f.close()
        else:
            WaifuPost()

    else:
        f = open("D:\\Archivos\\Documentos\\RandomWaifuBot\\seedData.txt", "a")
        f.write(str(res) + ";" + str(resfactor) + "\n")
        f.close()

    # Gets image url
    url = "https://thisanimedoesnotexist.ai/results/psi-" + \
        str(resfactor) + "/seed" + res + ".png"

    # Cookies
    req = urllib.request.build_opener()
    req.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64)')]
    urllib.request.install_opener(req)

    # Makes file
    filename = "D:\\Archivos\\Documentos\\RandomWaifuBot\\temp.png"

    # Checks if file exists
    if os.path.exists(filename):
        os.remove(filename)
        urllib.request.urlretrieve(url, filename)
    else:
        urllib.request.urlretrieve(url, filename)

    # Uploads and tweets
    img_obj = api.media_upload(filename)
    api.update_status("This is today's waifu, seed " + res,
                      media_ids=[img_obj.media_id_string])
    print("Si llegó aqui, debería servir")


WaifuPost()
