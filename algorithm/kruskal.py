# -*- coding: utf-8 -*-

import numpy as np

class Kruskal(object):
    def __init__(self, graph=None):

        print "init ..."
        self.graph = np.array(graph)
        self.selectd_edges = []
        self.selectd_points = []
        self.all_points = []
        self.all_edges = {}
        for i in range(self.graph.shape[0]):
            self.all_points.append(i)
        for i in range(self.graph.shape[0]):
            for j in range(i, self.graph.shape[0]):
                self.all_edges.update({(i, j): self.graph[i][j]})
        print self.graph

    def had(self, x=None):

        if x not in self.selectd_edges:
            if (x[0] not in self.selectd_points) or (x[1] not in self.selectd_points):
                return True
            else:
                return False
        else:
            return False

    def hadpoint(self, x=None):

        point_list = []
        if x[0] not in self.selectd_points:
            point_list.append(x[0])
        if x[1] not in self.selectd_points:
            point_list.append(x[1])

        return point_list

    def process(self):

        (m, n) = self.graph.shape
        edge_sort = sorted(self.all_edges.items(), key=lambda item: item[1])

        for i in range(len(edge_sort)):
            if edge_sort[i][1] != 0:
                if self.had(x=edge_sort[i][0]):
                    self.selectd_edges.append(edge_sort[i][0])
                    point = self.hadpoint(x=edge_sort[i][0])
                    self.selectd_points = self.selectd_points + point

        print self.selectd_points
        print self.selectd_edges


if __name__ == "__main__":
    graphs = [[0, 7, 0, 5, 0, 0, 0],
              [7, 0, 8, 9, 7, 0, 0],
              [0, 8, 0, 0, 5, 0, 0],
              [5, 9, 0, 0, 15, 6, 0],
              [0, 7, 5, 15, 0, 8, 9],
              [0, 0, 0, 6, 8, 0, 11],
              [0, 0, 0, 0, 9, 11, 0]
              ]
    a = Kruskal(graph=graphs)
    a.process()