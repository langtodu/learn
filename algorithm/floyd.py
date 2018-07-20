# -*- coding: utf-8 -*-

class Floyd(object):
    def __init__(self, graph=None):
        self.graph = graph
        print len(graph)
        self.graph_length = len(graph)
        self.distance = []
        self.route = []
        for i in range(self.graph_length):
            self.distance.append([])
            self.route.append([])
            for j in range(self.graph_length):
                try:
                    self.distance[i].append(self.graph[i][j])
                except:
                    self.distance[i].append(0)
                self.route[i].append([i,j])

    def process(self):
        all_point = []
        for point in range(self.graph_length):
            all_point.append(point)
        for i in range(self.graph_length):
            for j in all_point:
                if graphs[i][j] != 0:
                    for x1 in range(self.graph_length):
                        for x2 in range(len(self.route[x1])):
                            start = self.route[x1][x2][0]
                            end = self.route[x1][x2][-1]
                            if (end == i) and (self.distance[x1][x2]+self.graph[i][j]<self.distance[start][j]):
                                self.distance[start][j] = self.distance[x1][x2]+self.graph[i][j]
                                self.route[start][j].insert(-1, i)
        for i in range(self.graph_length):
            for j in range(self.graph_length):
                print str(self.route[i][j]) + "\t" + str(self.distance[i][j])

if __name__ == "__main__":
    graphs = [[0, 7, 0, 5, 0, 0, 0],
              [7, 0, 8, 1, 7, 0, 0],
              [0, 8, 0, 0, 5, 0, 0],
              [5, 1, 0, 0, 15, 6, 0],
              [0, 7, 5, 15, 0, 8, 9],
              [0, 0, 0, 6, 8, 0, 11],
              [0, 0, 0, 0, 9, 11, 0],
              ]
    a = Floyd(graph=graphs)
    a.process()
