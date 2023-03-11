import requests
import re
import json
import random
import urllib.parse

def getchannels(search):
    r = requests.get(f'https://www.youtube.com/results?search_query={urllib.parse.quote(search.replace(" ", "+"))}&sp=EgIQAg%253D%253D')
    t = re.findall(r'var ytInitialData = (.*?);<\/script>', r.text)[0]
    
    channels = json.loads(t)["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"]
    
    arr = []
    for c in channels:
        if "channelRenderer" not in c: continue
        arr.append(c["channelRenderer"]["navigationEndpoint"]["commandMetadata"]["webCommandMetadata"]["url"].replace("/@", ""))

    return arr