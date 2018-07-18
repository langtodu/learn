# -*- coding: utf-8 -*-

#************************************************#
#在类属性中。以单下划线_开头的属性，是protected类型变量，允许自身和子类访问；外部也已访问
#双划线__表示private类型变量，只能允许该类本身访问；外部不能通过实例化名.属性名来访问，外部可以通过实例名._类名__属性名访问
#
#************************************************#
#在类方法中。以单下划线_开头的函数，不能通过from my_module import * 来使用
#双划线__表示private类型变量，只能允许该类本身访问；外部不能通过实例化名.属性名来访问，外部可以通过实例名._类名__属性名访问
#
#************************************************#

class Test1(object):
    def __init__(self, str1="Test1 _", str2="Test1 __"):
        self._str1= str1
        self.__str2 = str2
    def output(self):
        return self._str2


class Test2(Test1):
    def __init__(self, val1="Test2 _", val2="Test2 __"):
        self._val1 = val1
        self.__val2 = val2
    def output2(self):
        print Test1.output()
        print self.__val2

if __name__ == "__main__":

    print Test1.__dict__