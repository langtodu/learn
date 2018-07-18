# -*- coding: utf-8 -*-

#****************使用两个栈实现队列******************
#将stack1用于存储队列的输入数据，当队列需要输出时，若stack2有数据则只需从stack弹出；若stack2为空，将stack1的数据压入stack1
#使用列表用作栈
class StackQueue(object):
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    def inqueue(self, val):
        self.stack_in.append(val)
    def outqueue(self):
        if self.stack_out:
            return self.stack_out.pop()
        else:
            if self.stack_in:
                for _ in self.stack_in:
                    val = self.stack_in.pop()
                    self.stack_out.append(val)
                return self.stack_out.pop()
            else:
                print "Queue is empty!"
                return None

if __name__ == "__main__":

    example1 = StackQueue()
    example1.inqueue(1)
    print example1.outqueue()
    print example1.outqueue()
