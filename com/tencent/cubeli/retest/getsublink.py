import re

file = open(r'C:\Users\cubeli\PycharmProjects\pachong\com\tencent\cubeli\infoqpage\mine.txt', 'r')
dashboard = file.read()
link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", dashboard)

pattern = re.compile(r'http://www.infoq.com')
for sublink in link_list:
    match = pattern.match(sublink)
    if match:
        print sublink