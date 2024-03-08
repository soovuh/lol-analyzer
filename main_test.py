from riot_requests.players import Player

player = Player('sooova', region='RU')
champs = player.get_top_5_mastery_champs()
print(f'Player {player.name} with level {player.cass_summoner.level} is playing on region {player.region}.\nThe highest amount of skill:')
for champ in champs:
    print(f'{champ.name} - {champ.points} points.')
