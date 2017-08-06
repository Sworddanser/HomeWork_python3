import os.path
import requests
import math
from xml.etree.ElementTree import fromstring

# DIR_PATH = os.path.abspath(os.path.dirname(__file__))# для удобства
# file_path = os.path.join(DIR_PATH, '3.4-currencies')
# file_name = 'travel.txt'

def file_open(file_path, file_name):
    with open(os.path.join(file_path, file_name)) as f:
        data = []
        for line in f:
            item = line.strip().split(' ')
            data.append(item)
    return data

def math_ave(data):
    sum = 0
    for i in data:
        sum += int(i[0])
    ave = int(round(sum / len(data)))
    return ave

def convert_temp(ave):
    response = requests.post(
        'http://www.webservicex.net/ConvertTemperature.asmx',
        headers = {'Content-Type': 'text/xml; charset=utf-8'},
        data= '''<?xml version="1.0" encoding="utf-8"?>
            <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
              <soap:Body>
                <ConvertTemp xmlns="http://www.webserviceX.NET/">
                  <Temperature>{ave}</Temperature>
                  <FromUnit>degreeFahrenheit</FromUnit>
                  <ToUnit>degreeCelsius</ToUnit>
                </ConvertTemp>
              </soap:Body>
            </soap:Envelope>
    '''.format(ave=ave)
    )
    tree = fromstring(response.text)
    return float(list(list(list(tree)[0])[0])[0].text)



def math_sum(data, file_name):
    sum = 0
    if file_name == 'travel.txt':
        for i in data:
            i[1] = ''.join(i[1].split(','))
            sum += int(float(i[1]))
    if file_name == 'temps.txt':
        for i in data:
            sum += int(float(i[0]))
    return sum

def math_ave(data, sum):
    ave = int(round(sum / len(data)))
    return ave


def convert_dist(sum):
    response = requests.post(
        'http://www.webservicex.net/length.asmx',
        headers = {'Content-Type': 'text/xml; charset=utf-8'},
        data= '''<?xml version="1.0" encoding="utf-8"?>
                <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                  <soap:Body>
                    <ChangeLengthUnit xmlns="http://www.webserviceX.NET/">
                      <LengthValue>{sum}</LengthValue>
                      <fromLengthUnit>Miles</fromLengthUnit>
                      <toLengthUnit>Kilometers</toLengthUnit>
                    </ChangeLengthUnit>
                  </soap:Body>
                </soap:Envelope>
    '''.format(sum=sum)
    )
    tree = fromstring(response.text)
    return float(list(list(list(tree)[0])[0])[0].text)


def convert_cur(from_cur, to_cur, numb):
    response = requests.post(
        'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx',
        headers = {'Content-Type': 'text/xml; charset=utf-8'},
        data= '''<?xml version="1.0" encoding="utf-8"?>
                    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                      <soap:Body>
                        <ConvertToNum xmlns="http://webservices.cloanto.com/currencyserver/">
                          <fromCurrency>{from_cur}</fromCurrency>
                          <toCurrency>{to_cur}</toCurrency>
                          <amount>{numb}</amount>
                          <rounding>1</rounding>
                        </ConvertToNum>
                      </soap:Body>
                    </soap:Envelope>
    '''.format(from_cur=from_cur, to_cur=to_cur,numb=numb)
    )
    tree = fromstring(response.text)
    el = list(list(list(tree)[0])[0])[0]
    return float(list(list(list(tree)[0])[0])[0].text)

def convertation(data):
    total_cost = 0
    for i in data:
        print (i)
        bvn = convert_cur(i[2],'RUB',i[1] )
        total_cost += bvn
        print('Стоимость билетов в рублях:', math.ceil(bvn))
    return total_cost

def main():
    file_path = input('Введите путь до папки:')
    file_name = input('Введите имя файла:')
    data = file_open(file_path, file_name)
    sum = math_sum(data, file_name)
    if file_name == 'temps.txt':
        ave = math_ave(data, sum)
        aff = convert_temp(ave)
        print('Температура', round(aff, 1),'по Цельсию')
    if file_name == 'travel.txt':
        dist = convert_dist(sum)
        print('Расстояние', round(dist, 2), 'км')
    if file_name == 'currencies.txt':
        cost = math.ceil(convertation(data))
        print('Итоговая стоимость:',cost)


main()

