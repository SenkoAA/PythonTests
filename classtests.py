# class tests

import sys


class Main(object):
    
    a = 10

    def __init__(self, b):
        self.b = b

    def method(self, c):
        print(self.a)
        print(self.b)
        print(c)

    @classmethod
    def clsmethod(cls, c):
        print(cls.a)
        print(cls.b)
        print(c)
    
    @staticmethod
    def stcmethod(c):
        print(a)
        print(b)
        print(c)

def main():
    for idx, arg in enumerate(sys.argv):
        print('arg{} = {}'.format(idx, arg))
    
    try:
        obj = Main(15)
        obj.method
        #Main.clsmethod(20)
    except Exception as exc:
        print(exc)
    else:
        print('Everithing is ok!')
    finally:
        print('Finally block!')

if __name__ == '__main__':
    main()