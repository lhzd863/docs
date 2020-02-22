import requests
import re
from bs4 import BeautifulSoup
import json
import  os
from selenium import webdriver
from pyvirtualdisplay import Display

def read_txt(dict1):
    with open("t-audio.txt", "r") as f:
        data = f.read()
        arr1 = data.split(",")
        dict1['name']=arr1[1]
        dict1['catalog']='玄幻小说'
        dict1['announcer']=arr1[2]
        dict1['amount']=arr1[4]

    return dict1
def post_url(dict1):
    url1 = "http://122.51.161.53:9903/api/audio/add?accesstoken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjMzMDY0NzQzOTYsImlzcyI6ImF6eiJ9.6AfjNv08aXIYNeR9D4P66fx1HYErDDmD4icPR1bCPgY"
    headers1 = {'content-type': "application/json" }
    img1 = "http://122.51.161.53:12306/audio/"+dict1['catalog']+"/"+dict1['name']+"/"+dict1['name']+".jpg"
    body1 = {
       "catalog": dict1['catalog'],
       "name": dict1['name'],
       "info": "",
       "url": "http://122.51.161.53:12306/audio",
       "context": dict1['context'],
       "amount": dict1['amount'],
       "img": img1,
       "status": "更新中",
       "announcer": dict1['announcer'],
       "author": dict1['author'],
       "format": "mp3"
    }
    print(body1)
    response = requests.post(url1, data = json.dumps(body1), headers = headers1)
    print(response.text)
    #print(response.status_code)

def read_hislist():
    lst=[]
    with open("t-audio-lst.txt", "r") as f:
        for line in f:
            lst.append(line.strip('\n'))

    return lst

def open_spider(dict):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
    }
    res = requests.get(dict['url'],headers=header)
    res.encoding = 'gb2312'
    while res.status_code!=200:
        continue
    else:
        counts = res.text
        supers=BeautifulSoup(counts,"html.parser")
        for tag in supers.find_all('p',attrs={'id':'pla'}):
            t_context=tag.get_text()
            arr = t_context.split("\n")
            if len(arr)>1:
                dict['author'] = arr[0]
                dict['context'] = arr[1]
            else:
                dict['author'] = ""
                dict['context'] = arr[0]

            dict['author']=dict['author'].replace("\n","",-1).replace("\r","",-1).replace(u"\xa0",u"",-1).replace(u"\u3000",u"",-1).replace("作者：","").replace("作者:","")
            dict['context'] = dict['context'].replace("\"","").replace("\'","").replace("\?","").replace("\n","").replace("\r","").replace(u"\xa0",u"",-1).replace(u"\u3000",u"",-1)

        for tag2 in supers.find_all('span',attrs={'style': 'color: #ff0000'}):
            for tag3 in tag2.find_all('p'):
                t_arr0 = tag3.get_text().split(r"[:|：]")
                if t_arr0[0] == "类别":
                    dict['type'] = t_arr0[1]
                if t_arr0[0] == "状态":
                    dict['status'] = t_arr0[1]
                if t_arr0[0] == "时间":
                    dict['time'] = t_arr0[1]

    #dict0 = read_txt(dict)
    return dict

if __name__=="__main__":
    lst1=read_hislist()
    with open("audio-data.txt", "r") as f:
        for line in f:
            dict = {}
            d1 = line.strip('\n')
            arr = d1.split(",")
            url = arr[0]
            name = arr[1]
            dict['url'] = url
            dict['name'] = name
            dict['catalog'] = "玄幻小说"
            dict['announcer']=arr[2]
            dict['amount']=arr[4]
            if name in lst1:
                dict2=open_spider(dict)
                post_url(dict2)
                print(dict2)
