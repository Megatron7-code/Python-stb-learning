

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
    print(('0x123').isdigit())
    print(('123').isdigit()) # 是否为十进制



