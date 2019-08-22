# -*- coding: utf-8 -*-

PI = 3.1415926

def main():
    arr = [1, 0, '', False]
    print(abs(-11))
    print(all(arr))
    print(any(arr))
    print(ascii('hehhe你好'))
    print(bin(10))
    print(bool(None))
    print(bytearray('你好，世界', 'utf-8'))
    print(bytes('你好，世界', 'utf-8'))
    print(callable(abs))
    print(chr(97))
    print(delattr(Test, 'video'))
    print(Test)
    print(dir(Test()))
    print(divmod(5, 3))
    print(list(enumerate(arr)))
    print(eval('arr + [6]'))
    print(exec('print("hello, world")'))
    print(float(10))
    print('{1}, {0}'.format('hello', 'world'))
    print(frozenset(arr))
    print(getattr(Test, 'course'))
    print(globals())
    print(hasattr(Test, 'test'))
    print(hash('123'))
    print(hash('321'))
    print(hash('123'))
    # print(help(abs))
    print(hex(10))
    print(id(Test))
    print(id(Test))
    # print(input('please enter your name:'))
    print(isinstance(Test, object))
    print(issubclass(Test, object))
    print(len('test'))
    print(locals())
    print(globals())
    print(max(1, 2, 3, 9))
    print(max([2, 5, 12, 7]))
    # print(memoryview(Test))
    print(min(9, 2, 1, 0.2))
    print(min([0.01, 2, 4, -0.07]))
    print(oct(8))
    for line in open('src/test.py').readlines():
        print(line)
    print(ord('a'))
    print(chr(8364))
    print(ord('€'))
    print(pow(2, 3))
    print(2 ** 3)
    print(range(5))
    print(range(1, 5, 2))



class Test:
    course = 666
    lesson = 0
    video = 0

    def __dir__(self):
        return [1, 2, 3]


