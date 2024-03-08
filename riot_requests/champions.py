import os
import cassiopeia as cass
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get('RIOT_API_KEY')
cass.set_riot_api_key(API_KEY)

class Champion:
    def __init__(self, id, region):
        self.id = id
        self.region = region
        self.cass_champ = cass.Champion(id=id, region=region)
        print(self.cass_champ.name)
