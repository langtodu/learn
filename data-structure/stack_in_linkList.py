# -*- coding: utf-8 -*-

class NodeData(object):
    def __init__(self, data=None, previous=None):
        self.data = data
        self.previous = previous
class Stack(object):
    def __init__(self, size=100):
        self.top = NodeData()
        self.size = size
        self.length = 0
    def isEmpty(self):
        return (self.top.previous == None)
    def push(self, data):
        if self.length < self.size:
            item = self.isNodedata(data)
            item.previous = self.top
            self.top = item
            self.length += 1
        else:
            print "stack is overflow"
            exit(1)
    def pop(self):
        if self.top.previous == None:
            print "stack is empty"
            exit(1)
        else:
            node = self.top
            print node.data
            self.top = node.previous
            self.length -= 1

    def isNodedata(self, data):
        item = None
        if isinstance(data, NodeData):
            item = data
        else:
            item = NodeData(data)
        return item

if __name__ == "__main__":
    stack = Stack(5)
    print stack.isEmpty()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.push([1,2,3])
    stack.pop()