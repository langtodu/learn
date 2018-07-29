# -*- coding: utf-8 -*-

'''
寻找某一节点到其余各节点的最短路径
'''

class Dijkstra(object):
    def __init__(self, graph=None, startpoint=0):
        self.graph = graph
        self.allpoints_num = len(self.graph)
        self.startpoint = startpoint
        self.selcted_ponit = [startpoint]
        self.wait_select = []
        for i in range(self.allpoints_num):
            self.wait_select.append(i)
        self.wait_select.remove(startpoint)
        first_router = tuple([startpoint])
        self.router = []
        self.router.append(first_router)  # list内容必须是不可修改的方式，如元组
        self.distance = [0]

    def process(self):

        while len(self.selcted_ponit) != self.allpoints_num:
            test_point = {}
            for i in range(len(self.router)):
                for j in self.wait_select:
                    test_router = list(self.router[i])
                    if self.graph[test_router[-1]][j] != 0:
                        point_dist = self.graph[test_router[-1]][j] + self.distance[i]
                        test_router.append(j)
                        test_point.update({tuple(test_router): point_dist})
            test_sorted = sorted(test_point.items(), key=lambda item: item[1])
            a = list(test_sorted[0][0])
            self.router.append(a)
            self.distance.append(test_sorted[0][1])
            self.selcted_ponit.append(test_sorted[0][0][-1])
            self.wait_select.remove(test_sorted[0][0][-1])

        return self.router, self.distance

if __name__ == "__main__":

    graphs = [[0, 7, 0, 5, 0, 0, 0],
              [7, 0, 8, 9, 7, 0, 0],
              [0, 8, 0, 0, 5, 0, 0],
              [5, 9, 0, 0, 15, 6, 0],
              [0, 7, 5, 15, 0, 8, 9],
              [0, 0, 0, 6, 8, 0, 11],
              [0, 0, 0, 0, 9, 11, 0]
              ]
    a = Dijkstra(graph=graphs)
    graph_router, graph_distance = a.process()
    for i in range(len(graph_router)):
        print str(graph_router[i]) + "        " + str(graph_distance[i])



