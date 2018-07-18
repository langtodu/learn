# -*- coding: utf-8 -*-

class Floyd(object):
    def __init__(self, graph=None, startpoint=0, endpoint=0):
        self.graph = graph
        self.startpoint = startpoint
        self.endpoint = endpoint
        self.test = [1, 2, 3]
        print self.test

    def process(self):
        test = self.test
        test.append(6)
        print self.test
        print test

if __name__ == "__main__":
    graphs = [[0, 7, 0, 5, 0, 0, 0],
              [7, 0, 8, 9, 7, 0, 0],
              [0, 8, 0, 0, 5, 0, 0],
              [5, 9, 0, 0, 15, 6, 0],
              [0, 7, 5, 15, 0, 8, 9],
              [0, 0, 0, 6, 8, 0, 11],
              [0, 0, 0, 0, 9, 11, 0]
              ]
    a = Floyd()
    a.test = [3, 2, 4]
    a.process()
    a.test