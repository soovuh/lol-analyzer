from riot_requests.players import Player, get_user_puuid, get_user_account_id

nickname = 'sooova'
tagline = 'RU1'
region = 'RU'

puuid = get_user_puuid(nickname, tagline)
account_id = get_user_account_id(puuid, region)
player = Player(account_id, puuid, region, nickname)

print(player.get_ranks())
history = player.summoner.match_history
counter = 0
for m in history:
    counter +=1

print(counter)