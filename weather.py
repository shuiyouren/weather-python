# -*- coding: utf-8 -*-

import requests
import sys
import os
# curent_dir = os.path.dirname(__file__)
# print(curent_dir)
# sys.path.append(curent_dir)

from bs4 import BeautifulSoup
from .weather_id import mylist


def show_weather(sumht,sumwea):
    str = None
    try:
        l1 = '温度:'+sumht[0]
        l2 = '天气:'+sumwea[0]
        str = "{0}; {1}".format(l2, l1)
    except:
        print('未查询到天气!!!')
    else:
        print(l1)
        print(l2)
    return str

def get_city_id(name_id):
    l = mylist()
    for i in l:
        if i['name'] == name_id:
            s = i['id']
    return s

def get_7dweather(header,id):
    #最高温
    temperatureHigh = []
    #天气
    wth = []
    url = 'http://www.weather.com.cn/weather/%s.shtml'%id
    req = requests.get(url,headers=header)
    req.encoding = 'utf-8'
    html = req.text
    bs = BeautifulSoup(html,'html.parser')
    tagToday = bs.select('p[class="tem"]')
    wth1 = bs.select('p[class="wea"]')
    for x in tagToday:
        temperatureHigh.append(x.text.strip())
    for z in wth1:
        wth.append(z.string)
    return (temperatureHigh, wth)

def get_weather_info(city: str):
    header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    city_id = get_city_id(city)
    (sumht, sumwea) = get_7dweather(header,city_id)
    return show_weather(sumht,sumwea)

def get_weather_list_str():
    text = "上海(%s)\n杭州(%s)\n" % (get_weather_info('上海'), get_weather_info('杭州'))
    return text

if __name__ == '__main__':
    get_weather_info('上海')
    print(get_weather_list_str())
