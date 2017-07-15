import requests
import os.path
import os


def translate_it(text,lang):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20170715T071503Z.8a621d8185bfbaea.672beeea575e14244f4e72f5c6c37450193451cc'

    params = {
        'key': key,
        'lang': lang,
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))


def get_text(files, lang_in, file_path):
    text = str()
    if lang_in in files.keys():
        with open(os.path.join(file_path, files[lang_in])) as f:
            text = f.read()
    return text


def crate_file(a, translate_path, lang):
    with open(os.path.join(translate_path, lang + '.txt'), 'w') as out:
        print(a, file=out)# почему pycharm выделяет фаилб вроде все верно и сама функция работает?


def main():
    while True:
        files = {'de': 'DE.txt', 'es': 'ES.txt', 'fr': "FR.txt"}
        file_path = input('Введите путь до файла с указанием имени файла: ')
        lang_in = input('Введите язык текста(fr, es, de) : ')
        lang_out = input('Введите язык перевода: ')
        translate_path = input('Введите путь куда сохранить: ')
        lang = lang_in + '-' + lang_out
        text = get_text(files, lang_in, file_path)
        a = translate_it(text, lang)
        crate_file(a, translate_path, lang)


main()
