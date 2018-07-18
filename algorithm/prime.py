# -*- coding: utf-8 -*-

import numpy as np

class Prim(object):
    def __init__(self, graph=None, outset=0):

        self.graph = np.array(graph)
        self.outset = outset
        self.selectd_point = [self.outset]
        self.selectd_edge = [[self.outset, self.outset]]
        self.all_points = self.graph.shape[1]
        self.all_edges = self.graph.shape[0]
        print "init"
        print self.graph

    def edged(self):
        print "edge"
        while len(self.selectd_point) != self.all_points:
            # select_point = []
            # select_edge = []
            record_edge = []
            min = 66
            for i in self.selectd_point:
                for j in range(self.all_points):
                    num = self.graph[i][j]
                    if (num < min) and (num != 0) and ((i not in self.selectd_point) or (j not in self.selectd_point)):
                        min = num
                        record_edge = [i, j]
            self.selectd_point.append(record_edge[1])
            self.selectd_edge.append(record_edge)
            print self.selectd_point, self.selectd_edge

        print self.selectd_point, self.selectd_edge


if __name__ == "__main__":
    graphs = [[0, 7, 0, 5, 0, 0, 0],
              [7, 0, 8, 9, 7, 0, 0],
              [0, 8, 0, 0, 5, 0, 0],
              [5, 9, 0, 0, 15, 6, 0],
              [0, 7, 5, 15, 0, 8, 9],
              [0, 0, 0, 6, 8, 0, 11],
              [0, 0, 0, 0, 9, 11, 0]
              ]

    a = Prim(graph=graphs, outset=0)
    a.edged()
