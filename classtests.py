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
    
    @staticmethod
    def otherstcmethod(c):
        return c**2

    def othermethod(self, c):
        #return self.otherstcmethod(c)
        return c**2

def main():
    for idx, arg in enumerate(sys.argv):
        print('arg{} = {}'.format(idx, arg))
    
    try:
        obj = Main(15)
        obj1 = Main(17)
        #obj.method(20)
        #Main.b = 12
        #Main.clsmethod(20)
        print('prev a = {}'.format(obj1.a))
        #Main.a = 777
        obj.a = 777
        print('new a = {}'.format(obj1.a))
        #Main.stcmethod(20)
        print(Main.otherstcmethod(10))
        print(obj.othermethod(10))
    except Exception as exc:
        print(exc)
    else:
        print('Everything is ok!')
    finally:
        print('Finally block!')

if __name__ == '__main__':
    main()