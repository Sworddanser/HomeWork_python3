from pprint import pprint
from urllib.parse import urlencode, urljoin

import requests

AUTHORIZE_URL = 'https://oauth.yandex.ru/authorize'
APP_ID = 'e8753eab8ec6497ab7963298c37b0d37'

auth_data = {
    'response_type': 'token',
    'client_id': APP_ID
}
########### - выше глобальные переменные для получения первичной информации для запуска яндес метрики
TOKEN = 'AQAAAAAfNchVAARzp_6yVv8XQEvCkZ__CEqBYlo'


class YMBase:   # - данные для первичного запроса на сайтб где мы вводим уникальный токен, авторизация
    MANAGEMENT_URL = 'https://api-metrika.yandex.ru/management/v1/'
    STAT_URL = 'https://api-metrika.yandex.ru/stat/v1/data'

    def get_headers(self):
        return {
            'Authorization': 'OAuth {}'.format(self.token),
            'Content-Type': 'application/x-yametrika+json',
            'User-Agent': 'asdasdasd'
        }



class YandexMetrika(YMBase):

    def __init__(self, token):
        self.token = token

    def get_counters(self, add):
        self.add = add
        url = urljoin(self.MANAGEMENT_URL, 'counters')
        headers = self.get_headers()
        response = requests.get(url, headers=headers, params={'pretty': 1})
        counters = response.json()['counters']
        return [Counter(self.token, c['id'],add) for c in counters]


class Counter(YMBase):

    def __init__(self, token, counter_id, add):
        self.token = token
        self.id = counter_id
        self.add = add

    def metrics1(self, add):
        params = {
            'id': self.id,
            'metrics': add
        }
        return params

    def data(self):
        add = self.add
        headers = self.get_headers()
        params = self.metrics1(add)
        response = requests.get(self.STAT_URL, params, headers=headers)
        return response

    @property
    def visits(self):
        eim = {}
        add = self.add
        if add == 'ym:s:visits':
            response = self.data()
            eim['visits'] = response.json()['data'][0]['metrics'][0]
        elif add == 'ym:s:pageviews':
            response = self.data()
            eim['pageviews'] = response.json()['data'][0]['metrics'][0]
        elif add == 'ym:s:users':
            response = self.data()
            eim['users'] = response.json()['data'][0]['metrics'][0]
        return eim



ym = YandexMetrika(TOKEN)
counters = ym.get_counters('ym:s:visits')
for counter in counters:
    print(counter.visits)
counters = ym.get_counters('ym:s:pageviews')
for counter in counters:
    print(counter.visits)
    counters = ym.get_counters('ym:s:users')
for counter in counters:
    print(counter.visits)