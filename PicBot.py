#!/usr/bin/python3

import requests
import telepot
import os
import yaml
import random
import re
import pdb
#from PIL import Image


telkey = 'YOUR TELEGRAM KEY'
botRe = re.compile(r"/pic(@YOUR_BOT_NAME)?\s+\S+")
subscription_key  = "YOUR BING SEARCH API KEY"

def bingSearch(query):
    global subscription_key
    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
    params  = {"q": query, "safeSearch":"Off"}#, "BingApis-Market":"en-US"}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    #print(response)
    #print(search_results)
    thumbnail_urls = [img["thumbnailUrl"] for img in search_results["value"][:16]]
    print(params)
    try:
        thumb_url = random.choice(thumbnail_urls)
    except:
        return "nada"
    #image_data = requests.get(thumb_url)
    #image_data.raise_for_status()
    #image = Image.open(BytesIO(image_data.content))        
    #image.save("tmp.png","PNG")
    msg = '<a href="{}">&#8204;&#10240;</a>'.format(thumb_url)
    print(msg)
    return msg


def handle(msg):
    global bot
    chatid=msg['chat']['id']
    msg = msg['text']
    if (re.match(botRe,msg)):
        query = msg[msg.find(" "):]
        ret = bingSearch(query)
        bot.sendMessage(chatid,ret,parse_mode='html')


bot = telepot.Bot(telkey)
bot.message_loop(handle, run_forever=True)
