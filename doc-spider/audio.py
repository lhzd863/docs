import requests
import re
from bs4 import BeautifulSoup
import json
import  os
from selenium import webdriver
from pyvirtualdisplay import Display

def store(data):
    with open('audio-data.json', 'w') as fw:
        json.dump(data,fw)

def load():
    with open('audio-data.json','r') as f:
        data = json.load(f)
        return data

def storestr(st1):
    with open('./audio-data.txt','a') as fw:
        fw.write(str(st1))
        fw.close()

def getiframeid(driver,url1):
    #display = Display(visible=0, size=(900, 800))
    #display.start()

    #driver = webdriver.Firefox(executable_path='./geckodriver')
    driver.get(url1)
    driver.switch_to.frame('play')
    html = driver.page_source
    #print(html)
    pattern = re.compile('([0-9]{13}x[0-9]{10}x[0-9]{13}-\w+)',re.I)
    iframeid = pattern.search(str(html)).group()
    #driver.quit()
    #display.quit()
    return iframeid

def dump_load(lst,driver,url):
    dict = {}
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
    }
    res = requests.get(url,headers=header)
    res.encoding = 'gb2312'
    while res.status_code!=200:
        continue
    else:
        counts = res.text
        supers=BeautifulSoup(counts,"html.parser")
        for tag in supers.find_all('li'):
            m_url=tag.find('a').get('href')
            m_context = tag.find('a').get_text()
            t_url = "https://www.5tps.com"+ m_url
            dict['url'] = t_url
            arr = m_context.split("／")
            if len(arr)<2:
                dict['name'] = arr[0]
                dict['author'] = ''
            else:
                dict['name'] = arr[0]
                dict['author'] = arr[1]
            if arr[0] in lst:
                print(arr[0]," has stat")
                break
            print(t_url,m_context)
            contens_rs = requests.get(t_url,headers=header)
            contens_rs.encoding = 'gb2312'
            while contens_rs.status_code!=200:
                continue
            else:
                #rescsa=json.loads(contens_rs.content.decode())
                counts1 = contens_rs.text.replace('<li class=\"lxx\"></li>','')
                #print(counts1)
                supers1=BeautifulSoup(counts1,"html.parser")
                num=0
                for tag1 in supers1.find_all('li'):
                    d = tag1.find_all('a', attrs={'title': re.compile("mp3$")})
                    if len(d)==0 :
                        continue
                    m_url1=tag1.find('a').get('href')
                    m_context1 = tag1.find('a').get_text()
                    m_title1 = tag1.find('a').get('title')
                    dict['format'] = m_title1
                    #print(m_url1,m_context1,m_title1)
                    t_url1 = "https://www.5tps.com"+m_url1
                    if num==0:
                        print(t_url1)
                        #iframeid = getiframeid(driver,t_url1)
                        #dict['iframeid'] = iframeid
                    #contens_rs2 = requests.get(t_url1,headers=header)
                    #while contens_rs2.status_code!=200:
                    #    continue
                    #else:
                    #    counts1 = contens_rs2.text.replace('<li class=\"lxx\"></li>','')
                    num+=1
                    #break
                dict['num'] = num
                title1 = supers1.find_all('h4')
                #print(title1)

                for tag2 in supers1.find_all('span',attrs={'style': 'color: #ff0000'}):
                    m_context2 = tag2.find('p').get_text()
                    #print(m_context2)
                    dict['tag'] = m_context2.replace('类别:','')

            #break
            st1 = dict['url']+','+dict['name']+','+dict['author']+','+dict['tag']+','+str(dict['num'])+','+dict['format']+','+dict['iframeid']+'\n'
            storestr(st1)
            lst.append(dict['name'])
            store(lst)
            print(lst)
    return dict

if __name__=="__main__":
    display = Display(visible=0, size=(900, 800))
    display.start()
    driver = webdriver.Firefox(executable_path='./geckodriver')
    lst = load()
    url = "https://www.5tps.com/mlist/46_1.html" #请求要访问小说页面的主页面
    for i in range(2, 65):
        url = "https://www.5tps.com/mlist/46_%d.html"%i
        dict1=response = dump_load(lst,driver,url) # 获取小说每页列表并解析出 音频地址 和 小说单张名称
        #st1 = dict1['url']+','+dict1['name']+','+dict1['author']+','+dict1['tag']+','+str(dict1['num'])+','+dict1['format']
        #print(st1)
        #lst.append(dict1)
        #storestr(st1)
    #print(lst)
    driver.quit()
    display.quit()
    
