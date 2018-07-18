# -*-coding: utf-8 -*-

class Stack(object):
    def __init__(self, size=100):
        self.stacklist = []
        self.size = size
    def isEmpty(self):
        return (len(self.stacklist) == 0)
    def push(self, data):
        if len(self.stacklist) < self.size:
            self.stacklist.append(data)
        else:
            print "stack is overflow"
            exit(1)
    def pop(self):
        if self.isEmpty():
            print "stack is empty"
            exit(1)
        else:
            print self.stacklist[-1]
            self.stacklist.remove(self.stacklist[-1])

if __name__ == "__main__":

    stack = Stack(10)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()