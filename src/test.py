# -*- coding: utf-8 -*-
import time
import requests

ti = 121 - 8 * 60 * 60
print(time.strftime("%H:%M:%S", time.localtime(ti)))
temp = '00:02:01'


def t2s(t):
    h, m, s = t.strip().split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)


print(t2s(temp))
