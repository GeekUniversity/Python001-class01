# Author Andy Fang
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def find_top10_urls(url):
    top10_movies_link = []
    header = {
        'Content-Type': 'text/plain; charset=UTF-8',
        'Origin': 'https://maoyan.com',
        'Referer': 'https://maoyan.com/films?showType=3',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Cookie':'__mta=150738441.1593157769843.1593160824465.1593161146500.4; uuid_n_v=v1; uuid=8F2963A0B78111EA801551553EAD9849E8BF317E589D41B68B14B6F443E579CD; _csrf=881c753de6d6a03771df0f24440c46402284b4ae084412209952f35da589d0f4; mojo-uuid=90a5645c0238bb3a951ac59e8fd65d83; mojo-session-id={"id":"7e3d93bc6657c31e418683e2b29017e8","time":1593157769493}; _lxsdk_cuid=172ef9a5a3fc8-07571fc6a3cbfd-3b634404-100200-172ef9a5a3fc8; _lxsdk=8F2963A0B78111EA801551553EAD9849E8BF317E589D41B68B14B6F443E579CD; lt=3vkYTSGMiRVJ99Zoas-CTnwvDXEAAAAA5woAAP0L56xTZWSA-mAli6O0geEhxzYIFV5NlCW10zKHRcTc_XBQ1zEJb1fai41iWWdFjA; lt.sig=0kqbR7qaUc8LVsV_z41gSc9nk30; mojo-trace-id=66; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593160833,1593161667,1593162012,1593162021; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593162021; __mta=150738441.1593157769843.1593161146500.1593162020659.5; _lxsdk_s=172ef9a5a41-f1a-c45-38e%7C%7C93'
    }
    request = requests.get(url, headers=header)
    html = request.text
    soup = bs(html,'html.parser')
    i = 0
    for tags in soup.find_all("div", attrs={"class": "movie-item film-channel"}):
        link = 'https://maoyan.com'+ tags.find('a').get('href')
        top10_movies_link.append(link)
        i = i + 1
        if(i >= 10):
            break
    return  top10_movies_link


def get_movie_info(url, movies_info_list):
    header = {
        'Content-Type': 'text/plain; charset=UTF-8',
        'Origin': 'https://maoyan.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Cookie':'__mta=150738441.1593157769843.1593160824465.1593161146500.4; uuid_n_v=v1; uuid=8F2963A0B78111EA801551553EAD9849E8BF317E589D41B68B14B6F443E579CD; _csrf=881c753de6d6a03771df0f24440c46402284b4ae084412209952f35da589d0f4; mojo-uuid=90a5645c0238bb3a951ac59e8fd65d83; mojo-session-id={"id":"7e3d93bc6657c31e418683e2b29017e8","time":1593157769493}; _lxsdk_cuid=172ef9a5a3fc8-07571fc6a3cbfd-3b634404-100200-172ef9a5a3fc8; _lxsdk=8F2963A0B78111EA801551553EAD9849E8BF317E589D41B68B14B6F443E579CD; lt=3vkYTSGMiRVJ99Zoas-CTnwvDXEAAAAA5woAAP0L56xTZWSA-mAli6O0geEhxzYIFV5NlCW10zKHRcTc_XBQ1zEJb1fai41iWWdFjA; lt.sig=0kqbR7qaUc8LVsV_z41gSc9nk30; mojo-trace-id=66; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593160833,1593161667,1593162012,1593162021; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593162021; __mta=150738441.1593157769843.1593161146500.1593162020659.5; _lxsdk_s=172ef9a5a41-f1a-c45-38e%7C%7C93'
    }
    request = requests.get(url, headers=header)
    html = request.text
    soup = bs(html, 'html.parser')
    tags = soup.find("div", attrs={"class": "movie-brief-container"})
    movie_name = tags.find('h1').text
    li_list = tags.find("ul").find_all("li")
    movie_type = ""
    for i in  li_list[0].find_all("a"):
        movie_type = movie_type + i.text + " "
    movie_time = li_list[2].text
    movie_info = [movie_name, movie_type, movie_time]
    movies_info_list.append(movie_info)


def output_movies_info(links):
    movies_info_list = []
    for i in links:
        get_movie_info(i, movies_info_list)

    writer = pd.DataFrame(data = movies_info_list)
    writer.to_csv('./top10_movies_info.csv', encoding='utf_8_sig',index=False, header=False )


movies_link = find_top10_urls('https://maoyan.com/films?showType=3')
output_movies_info(movies_link)


