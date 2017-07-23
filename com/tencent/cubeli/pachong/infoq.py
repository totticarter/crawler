# -*- coding: utf-8 -*
import urllib
import urllib2
import requests
import re
import time

headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'http://raven.infoq.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'raven.infoq.com'
}

id = 'l00164768@gmail.com'
password = 'Tencent@123'
postDict = {
    'email': id,
    'password': password,
    'rememberme': 'y'
}
import requests.sessions
def login(postDict):
    loginURL = 'http://raven.infoq.com/'
    loginURL += 'users/auth'
    s = requests.session()
    login = s.post(loginURL, data=postDict, headers=headers)
    return (s,login)

def getLinks(postDict,logined):
    appliedMineURL= "http://raven.infoq.com/official/applied/mine"
    appliedAllURL = "http://raven.infoq.com/official/applied/all"
    rssNewsURL = "http://raven.infoq.com/official/rss/news"
    rssArticlesURL = "http://raven.infoq.com/official/rss/articles"

    urls ={'appliedMine':appliedMineURL,
            'appliedAll': appliedAllURL,
           'rssNews':rssNewsURL,
           'rssArticles':rssArticlesURL
           }


    for urlFile in urls:
        url = urls[urlFile]
        print urlFile
        response = logined[0].get(url, cookies=logined[1].cookies, headers=headers)
        link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", response.content)
        pattern = re.compile(r'http://www.infoq.com')
        file = open('urlcontent\\' + urlFile, 'w')
        for sublink in link_list:
            match = pattern.match(sublink)
            if match:
                print sublink
                file.writelines(sublink+'\n')
                break



logined = login(postDict)
while True:
    time.sleep(2)
    getLinks(postDict, logined)
    print '==========================='+ time.strftime('%Y-%m-%d:%H:%M:%S', time.localtime(time.time())) + '=============================='


# link_list =re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,content)
# file = open(r'mine.txt', 'w')
# file.write(content)
#
# import re
# file = open(r'mine.txt', 'r')
# dashboard = file.read()
# link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", dashboard)
#
# pattern = re.compile(r'http://www.infoq.com')
# for sublink in link_list:
#     match = pattern.match(sublink)
#     if match:
#         print sublink
