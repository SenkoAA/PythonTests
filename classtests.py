# class tests

import sys


class Main(object):
    
    a = 10

    def __init__(self, b):
        self.b = b

    def method(self, c):
        pass

    @classmethod
    def class_method(cls, d):
        pass

    @staticmethod
    def static_method(a, b, c, d):
        pass

def main():
    for arg in sys.argv:
        print(arg)

if __name__ == '__main__':
    main()