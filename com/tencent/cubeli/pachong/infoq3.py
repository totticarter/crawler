# -*- coding: utf-8 -*
import gzip
import re
import http.cookiejar
import urllib2

# import urllib.request
# import urllib.parse


def getOpener(head):
    # deal with the Cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


header = {
    'Connection': 'Keep-Alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'http://raven.infoq.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'raven.infoq.com'
}

url = 'http://raven.infoq.com/'
opener = getOpener(header)
# op = opener.open(url)
# data = op.read()
# data = ungzip(data)  # 解压
# # uncode = data.decode()
# _xsrf = getXSRF(data)

url += 'users/auth'
id = 'l00164768@gmail.com  '
password = 'Tencent@123'
postDict = {
    'email': id,
    'password': password,
    'rememberme': 'y'
}

import urllib
postData = urllib.urlencode(postDict).encode()
op = opener.open(url, postData)
opener.
data = op.read()
data = ungzip(data)

print(data.decode())