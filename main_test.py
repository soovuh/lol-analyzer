from riot_requests.players import Player, get_user_puuid, get_user_account_id

nickname = 'sooovuh'
tagline = 'kayn'
region = 'RU'

puuid = get_user_puuid(nickname, tagline)
account_id = get_user_account_id(puuid, region)
player = Player(account_id, puuid, region, nickname)
champs = player.get_top_5_mastery_champs()
for champ in champs:
    print(champ.name)
