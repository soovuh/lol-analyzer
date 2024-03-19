import os
import json
import requests
from requests.exceptions import HTTPError
import cassiopeia as cass
from dotenv import load_dotenv
from riot_requests.champions import UserChampion

load_dotenv()
API_KEY = os.environ.get('RIOT_API_KEY')
DEFAULT_LANGUAGE_REGION = 'EUW'
cass.set_riot_api_key(API_KEY)


def get_user_puuid(nickname, tagline):
    tagline = tagline.replace('#', '')
    nickname = nickname.strip()

    url = f'https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{nickname}/{tagline}'
    headers = {'X-Riot-Token': API_KEY}
    response = requests.get(url=url, headers=headers)

    data = response.json()
    
    if response.status_code != 200:
        raise HTTPError
    
    return data['puuid']

def get_user_account_id(puuid, region):
    region = region.lower()
    
    url = f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}'
    headers = {'X-Riot-Token': API_KEY}
    response = requests.get(url=url, headers=headers)

    data = response.json()

    if response.status_code != 200:
        raise HTTPError
    
    return data['accountId']


class Player:
    def __init__(self, account_id, puuid, region, nickname):
        self.account_id = account_id
        self.puuid = puuid
        self.region = region
        self.nickname = nickname
        self.summoner = cass.get_summoner(account_id=account_id, region=region)
        
        # Get needed fields from Summoner class in cass
        self.level = self.summoner.level
        self.profile_icon_url = self.summoner.profile_icon().url
        print(self.profile_icon_url)
        
    def get_top_5_mastery_champs(self):
        url = f'https://{self.region.lower()}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{self.puuid}?api_key={API_KEY}'
        response = requests.get(url)

        data = response.json()
        data = data[0:5]
        champs = []
        for entry in data:
            champ = UserChampion(id=entry["championId"], region=DEFAULT_LANGUAGE_REGION, points=entry['championPoints'])
            champs.append(champ)
        return champs

