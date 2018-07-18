# -*- coding: utf-8 -*-

class NodeData(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class LinkList(object):
    def __init__(self):
        self.head = NodeData()
        self.length = 0
    def isEmpty(self):
        return (self.length == 0)
    def append(self, data):
        item = self.isNodedata(data)
        if self.head.next:
            node = self.head
            while node.next:
                node = node.next
            node.next = item
            self.length += 1
        else:
            self.head.next = item
            self.length += 1
    def insert(self, index, data):
        if self.isEmpty():
            print "the linklist is empty!"
            exit(1)
        if index <0 or index >= self.length:
            print "out of index!"
            exit(1)
        item = self.isNodedata(data)
        node = self.head
        if index == 0:
            item.next = node.next
            node.next = item
        else:
            for _ in range(index):
                node = node.next
            item.next = node.next
            node.next = item
    # delete the node which is in index
    def delete_index(self, index):
        if self.isEmpty():
            print "the linklist is empty!"
            exit(1)
        if index <0 or index > self.length:
            print "out of index!"
            exit(1)
        node = self.head
        prenode = None
        if index == 0:
            prenode = node
            node = node.next
            prenode.next = node.next
        else:
            for _ in range(index):
                node = node.next
            prenode = node
            node = node.next
            prenode.next = node.next
    # delete the first data which is equal with data
    def delete_data(self, val):
        if self.isEmpty():
            print "the linklist is empty!"
            exit(1)
        node = self.head
        prenode = self.head
        not_deleted = True
        while not_deleted and node.next:
            node = node.next
            if node.data == val:
                prenode.next = node.next
                not_deleted = False
                print "delete data success"
            else:
                prenode = node
        if not_deleted:
            print "the val does not exist "

    def isNodedata(self, data):
        item = None
        if isinstance(data, NodeData):
            item = data
        else:
            item = NodeData(data)
        return item

if __name__ == "__main__":

    node = LinkList()
    print node.isEmpty()
    node.append(1)
    node.append(2)
    node.append(3)
    node.append(4)
    node.insert(3, "a")
    node.delete_index(2)
    node.delete_data(2)
    item = node.head
    while item.next:
        item = item.next
        print item.data

