# -*- coding: utf-8 -*-

class NodeData():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Tree():
    def creat(self):
        data = raw_input("input a number: ")
        if data not in [" ",""]:
            if isinstance(data, NodeData):
                item = data
            else:
                item = NodeData(data)
            item.left = self.creat()
            item.right = self.creat()
        else:
            item = None
        return item
    def preorder(self, node):
        if node:
            print node.data
            self.preorder(node.left)
            self.preorder(node.right)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print node.data
            self.inorder(node.right)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print node.data


if __name__ == "__main__":
    tree = Tree()
    nodes = tree.creat()
    print "preorder ..."
    tree.preorder(nodes)
    print "inorder ..."
    tree.inorder(nodes)
    print "postorder ..."
    tree.postorder(nodes)
