# -*- coding: utf-8 -*-

##类的构建方法介绍

#**************** 方法 **************
## classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
## classmethod和staticmethod都不能调用实例属性
class Test(object):
    def __init__(self, str="Hello istancemethod!"):
        self.init_str = str

    def add1(self, val1, val2):     #类方法添加self才能使用类属性
        print self.init_str
        print "this is istancemethod"
        print val1+val2

    @classmethod
    def add2(cls, val1, val2):  # 类方法需要添加cls才能使用属性
        print cls.__name__
        print "this is classmethod"
        print val1 + val2

    @staticmethod
    def add3(val1, val2):  # 类方法不需要添加任何必要的参数就可以使用类属性
        # print StaticMethod.init_str
        print Test.__name__
        print "this is staticmethod"
        print val1 + val2


if __name__ == "__main__":
    stance1 = Test()
    stance1.add1(1, 2)

    Test.add2(2, 3)

    Test.add3(3, 4)

