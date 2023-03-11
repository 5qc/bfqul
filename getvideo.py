import requests
import re
import json
import random

def getvideos(channels):
    channel_id = random.choice(channels)

    r = requests.get(f"https://www.youtube.com/@{channel_id}/videos")
    t = re.findall('var ytInitialData = (.*?);<\/script>', r.text, flags=re.IGNORECASE)
    if len(t) == 0: return getvideos(channels)
    else: t = t[0]

    try: videos = json.loads(t)["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][1]["tabRenderer"]["content"]["richGridRenderer"]["contents"]
    except: return getvideos(channels)

    arr = []
    for v in videos:
        if "richItemRenderer" not in v: continue
        arr.append(v["richItemRenderer"]["content"]["videoRenderer"]["videoId"])

    return random.choice(arr)