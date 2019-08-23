
import math

def main():
    print(False) # 右值无法赋值
    print(True)
    print(None)
    print(type(None))
    print(NotImplemented)
    # exit(1)
    # quit(0)
    # print(copyright())
    # print(license())
    temp = 3.1415926j
    print(temp.real)
    print(temp.imag)
    print(complex(temp.real, temp.imag))
    print(divmod(2, 3))
    print(0 ** 0)
    print(math.trunc(3.14))
    print(round(3.14))
    print(math.floor(3.14))
    print(math.ceil(3.14))
    print((4).bit_length()) # 3位
    print((4).to_bytes(2, byteorder='big'))
    print((3.14).is_integer())
    print((3.0).is_integer())
    print((3.0).hex())
    print((-0.91).hex())
    print(float.fromhex('3.14'))