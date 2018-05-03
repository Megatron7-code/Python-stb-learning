# -*- coding:utf-8 -*-
import urllib.request

re = urllib.request.Request("http://www.baidu.com")

f = urllib.request.urlopen(re)

s = f.read()

s = s.decode('utf-8', 'ignore')

file = open('ttt.txt', 'a', 1, 'utf-8')

file.write(s)
file.close()
