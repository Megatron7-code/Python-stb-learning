

def main():
    print(('string').capitalize())
    print(('HellO').casefold())
    print(('testing').center(22, '-'))
    print(('testtest').count('t'))
    print(('test').encode())
    print(('test').endswith('t'))
    print(('test').endswith('s'))
    print(('\ttest\t').expandtabs())
    print(('\ttest\t').expandtabs(4))
    print(('\ttest\t').expandtabs(2))
    print(('test').find('sd'))
    print(('test').find('st'))
    print(('test').find('s'))
    print(('test {test}'.format(test=123)))
    print(('test').index('t'))
    print(('test').index('e'))
    print(('test123-+').isalnum())
    print(('test123').isalnum()) # 是否都是字母+数字
    print(('test123').isalpha())
    print(('test').isalpha()) # 是否都是字母
    print(('test123').isdecimal())
    print(('123').isdecimal()) # 是否为数字
    print(('123.123').isdecimal()) # False
    print(('0x123').isdigit())
    print(('123').isdigit()) # 是否为十进制
    print(('Test').islower())
    print(('test').islower()) # 是否为小写字母
    print(('test123').isnumeric())
    print(('123.123').isnumeric())
    print(('123').isnumeric()) # 是否为数值
    print(('ttest').isprintable()) # 是否可以打印
    print(('tes t').isspace())
    print(("test").isspace())
    print(('title').istitle())
    print(('<title>title</title>').istitle())
    print(('Title').istitle())
    print(('Test').isupper())
    print(('TEST').isupper())
    print(('test temp').join('123'))
    print(('test temp').join('12'))
    print(('test temp').join('1'))
    print(('test').ljust(9, '-'))
    print(('test').rjust(9, '-'))
    print(('TeSt').lower())
    print(('Tet').lower())
    print(('----++test++-----').lstrip('-'))
    print(('----++test++-----').rstrip('-'))

    print(('----++test++-----').lstrip('-+'))
    print(('----++test++-----').rstrip('-+'))

    print(('----++test++-----').strip('-+'))

    print(('1, 2, 3').split(','))
    print(('1, 2, 3').split(',', maxsplit=1))
    print(('1, 2, 3').split(',', maxsplit=2))
    print(('1, 2, 3').split(',', maxsplit=3))
    print(('1, 2, 3').split(',', maxsplit=-1))

    print(('123\n456\t789\n').splitlines())
    print(('123\n456\t789\n').splitlines(keepends=True))

    print(('The girl from china').startswith('t'))
    print(('The girl from china').startswith('T'))

    print(('testTTemp').swapcase()) # 大小写翻转

    intab = 'test'
    outtab = '1234'
    trantab = str.maketrans(intab, outtab)
    print(('test').translate(trantab))

    print(('test').upper())
    print(('test').zfill(7)) # zero fill
    print(('test').zfill(2))












