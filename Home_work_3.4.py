from urllib.parse import urlencode
import requests
from pprint import pprint
import json
import time

AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
APP_ID = 6119344
VERSION = '5.67'
ACCESS_TOKEN=''#введите токен



# print(urlencode(auth_data))
#
# print('?'.join((AUTHORIZE_URL, urlencode(auth_data))))


def get_my_fr():
    params = {
        'access_token': ACCESS_TOKEN,
        'v': VERSION,
        'fields': 'id, first_name, last_name'
     }

    response = requests.get('https://api.vk.com/method/friends.get',params)
    data_frends = response.json()
    return data_frends

def get_fr_fr(data_frends,list_of_fr):
    my_friends = data_frends['response']['items']
    q = 0
    for i in my_friends:
        q += 1
        if q < 5:# ограничиваю количество этираций т.к. долго ждать ответа
            print('id', i['id'])
            params = {
            'access_token': ACCESS_TOKEN,
            'v': VERSION,
            'user_id': i['id'],
            'fields': 'id, first_name, last_name'
            }

            response = requests.get('https://api.vk.com/method/friends.get', params)
            # pprint(response.json())
            my_friends_friends = response.json()
            time.sleep(5)# уходим от ошибки большого количества запросов в 3 секунды.
            if 'response' in my_friends_friends.keys():
                list_of_fr.append(my_friends_friends['response']['items'])
    return list_of_fr

def cross(list_of_fr):
    id_name = []
    # pprint(len(list_of_fr))
    for num, list_numb in enumerate(list_of_fr):
        if num < 2:
            for peopl in list_of_fr[0]:
                if peopl in list_of_fr[1]:
                    id_name.append(peopl)
                    # print('1:', id_name)
        if num >= 2:
            for peopl in id_name:
                if peopl not in list_of_fr[num]:
                    id_name.remove(peopl)
                    # print('ост:', id_name)
    return id_name


def main():
    auth_data = {
        'client_id': APP_ID,
        'redirect_url': 'https://oauth.vk.com/blank.html',
        'display': 'mobile',
        'scope': 'friends',
        'response_type': 'token',
        'v': VERSION
    }
    data_frends = get_my_fr()
    list_of_fr = [data_frends['response']['items']]
    list_of_fr = get_fr_fr(data_frends, list_of_fr)
    id_name = cross(list_of_fr)
    print('Вот что:',len(id_name),id_name)

main()