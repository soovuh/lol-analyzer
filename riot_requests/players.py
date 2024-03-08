import os
import json
import requests
import cassiopeia as cass
from dotenv import load_dotenv
from riot_requests.champions import Champion

load_dotenv()
API_KEY = os.environ.get('RIOT_API_KEY')
DEFAULT_LANGUAGE_REGION = 'EUW'
cass.set_riot_api_key(API_KEY)


class Player:
    def __init__(self, name, region):
        self.name = name
        self.region = region
        self.cass_summoner = cass.get_summoner(name=name, region=region)
        self.puid = self.cass_summoner.puuid

    def get_top_3_mastery_champs(self):
        url = f'https://{self.region.lower()}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{self.puid}?api_key={API_KEY}'
        response = requests.get(url)

        data = response.json()
        data = data[0:5]
        champs = []
        for entry in data:
            champ = Champion(id=entry["championId"], region=DEFAULT_LANGUAGE_REGION)
            champs.append(champ)
        return champs
    


