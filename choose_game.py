# Written with passion by @hatedabamboo

import requests
import random
import re


def get_steamid(user_id):
    if re.match(r'7656\d{13}', user_id):
        return user_id
    else:
        steam_id_url = 'https://steamcommunity.com/id/{}/?xml=1'.format(user_id)
        response = requests.get(steam_id_url).text
        user_id = re.findall(r'7656\d{13}', response)[0]
        return user_id


def game_select():
    url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={}&steamid={}&include_appinfo=1&format=json'.format(api_key, user_id)
    response = requests.get(url).json()
    game_list = response['response']['games']
    games_list = []
    for i in game_list:
        game_title = i['name']
        appid = i['appid']
        game_link = ' https://store.steampowered.com/app/' + str(appid)
        games_list.append(game_title + game_link)
    print('This time you will play:\n' + (games_list[random.randrange(len(games_list))]))


user_id = get_steamid(input('Enter Steam ID: '))
api_key = input('Enter your Steam API key (can be found here: http://steamcommunity.com/dev/apikey): ')


while True:
    answer = input('Wanna play? (y/n) ')
    if answer == 'y':
        game_select()
    elif answer == 'n':
        print('Goodbye.')
        break
    else:
        print('Wrong answer.')
