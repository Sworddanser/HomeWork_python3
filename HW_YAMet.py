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

# print('?'.join((AUTHORIZE_URL, urlencode(auth_data))))


class YMBase:   # - данные для первичного запроса на сайтб где мы вводим уникальный токен, авторизация
    MANAGEMENT_URL = 'https://api-metrika.yandex.ru/management/v1/'
    STAT_URL = 'https://api-metrika.yandex.ru/stat/v1/data'

    def get_headers(self):
        return {
            'Authorization': 'OAuth {}'.format(self.token),
            'Content-Type': 'application/x-yametrika+json',
            'User-Agent': 'asdasdasd'
        }


class Metrika(YMBase):

    def __init__(self, token):
        self.token = token

    def get_counters(self):
        url = urljoin(self.MANAGEMENT_URL, 'counters')
        headers = self.get_headers()
        response = requests.get(url, headers=headers, params={'pretty': 1})
        counters = response.json()['counters']
        return [Counter(self.token, c['id']) for c in counters]


class Counter(YMBase):

    def __init__(self, token, counter_id):
        self.token = token
        self.id = counter_id

    @property
    def metrics_data(self):
        metrics = ['ym:s:visits', 'ym:s:pageviews', 'ym:s:users']
        eim = {}
        for metric in metrics:
            params = {
                'id': self.id,
                'metrics': metric
            }
            headers = self.get_headers()
            response = requests.get(self.STAT_URL, params, headers=headers)
            eim[metric] = response.json()['data'][0]['metrics'][0]
        return eim



ym = Metrika(TOKEN)
counters = ym.get_counters()

for counter in counters:
    pprint(counter.metrics_data)



