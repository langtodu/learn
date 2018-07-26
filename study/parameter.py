# -*- coding: utf-8 -*-

# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
#  在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
#  这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、
#  命名关键字参数和关键字参数

#  传递混用方式遵守：str1=在*args之前， *args在**kwargs之前，如(str='', *args, **kwargs)

class Test(object):
    def __init__(self):
        pass
    def t1(self, val):
        print val

    def t2(self, val=0):
        print val

    def t3(self, val, *args):
        print val
        print args

    def t4(self, *args, **kwargs):
        print args
        print kwargs

    def t5(self, val=0, *args, **kwargs):
        print val
        print args
        print kwargs

if __name__ == '__main__':

    test = Test()
    test.t1('a')
    test.t2(2)
    test.t3(1, 'a', 'b')
    # val=1, args=['a', 'b']
    test.t4(1, 2, 3, test1='test-1', test2='test-2')
    # args=[1, 2, 3], kwargs={'test1':'test-1', 'test2':'test-2'}
    test.t5(1, 'a', 'b', test1='test-1', test2='test-2')
    # val=1, args=['a', 'b'], kwargs={'test1':'test-1', 'test2':'test-2'}