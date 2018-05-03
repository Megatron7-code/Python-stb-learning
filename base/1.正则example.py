# -*- coding:utf-8 -*-

import re

t = 'abcdeahsdfweaaer23'

# 前瞻断言
print(re.findall('(?=a)\w+?', t))

# 反前瞻断言
print(re.findall('(?!a)\w+?', t))

# 后顾断言
print(re.findall('(?<=a)\w+?', t))

# 反后顾断言
print(re.findall('(?<!a)\w+?', t))
