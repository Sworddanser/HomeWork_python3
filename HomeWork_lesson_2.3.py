import json
import chardet


def get_file(file):
    with open(file, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        s = data.decode(result['encoding'])
        data = json.loads(s)
    d = data['rss']['channel']['items']

    news_words_list = []
    news_words = []
    for news in d:
        news_words_list.append(news['description'].split())
    for item_list in news_words_list:
        for items in item_list:
            if items.isalpha() is True:
                news_words.append(items)
    return news_words


def get_count_dict(news_words):
    fin = {}
    for word in news_words:
        l = len(word)
        if l > 6:
            if word not in fin:
                fin[word] = 1
            else:
                fin[word] += 1
    return fin


def main():
    file_name = ['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json']
    file = input('Выберите фаил(newsafr.json, newscy.json, newsfr.json, newsit.json):')
    if file in file_name:
        news_words = get_file(file)
        fin = get_count_dict(news_words)
        sorted_count_pairs = sorted(fin.items(), key=lambda x: x[1], reverse=True)
        top10 = sorted_count_pairs[:10]
        for word, fin in top10:
            print("Слово {} встретилось {} раз".format(word, fin))


main()
