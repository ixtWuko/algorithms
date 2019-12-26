#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 341页
    图
    """


class Graph_edge(object):
    def __init__(self, weight=1, end=None):
        self.weight = weight
        self.end = end # vertex index

class Graph_vertex(object):
    def __init__(self, key=None, index=None, edges=None):
        self.key = key
        self.index = index
        self.edges = edges

class Graph(object):
    def __init__(self, vertices=[], directed=False):
        self.directed = directed
        self.vertices = vertices
    
    def to_adjacent_matrix(self):
        length = len(self.vertices)
        not_exist = None if self.directed else 0
        result_matrix = [[not_exist]*length for i in range(length)]
        for vertex in self.vertices:
            for edge in vertex.edges:
                i = vertex.index
                j = edge.end
                result_matrix[i][j] = edge.weight
                # if not self.directed:
                #     result_matrix[j][i] = edge.weight
        return result_matrix
    
    def to_keys(self):
        result_keys = []
        for vertex in self.vertices:
            result_keys.append(vertex.key)
        return result_keys

    def from_adjacent_matrix(self, directed, keys, mat):
        self.directed = directed
        for i in range(len(keys)):
            self.vertices.append(Graph_vertex(key=keys[i], index=i, edges=[]))
        not_exist = None if self.directed else 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] != not_exist:
                    self.vertices[i].edges.append(Graph_edge(weight=mat[i][j], end=self.vertices[j].index))

    def __str__(self):
        result = []
        for vertex in self.vertices:
            s = "vertex index: " + str(vertex.index) + \
                "\nvertex key: " + str(vertex.key) + \
                "\nconnected to: " + str([e.end for e in vertex.edges])
            result.append(s)
        return '\n -------------------- \n'.join(result)


if __name__ == '__main__':
    keys = [1,2,3,4,5]
    mat = [
        [0,1,0,0,1],
        [1,0,1,1,1],
        [0,1,0,1,0],
        [0,1,1,0,1],
        [1,1,0,1,0]
    ]

    g = Graph()
    g.from_adjacent_matrix(False, keys, mat)
    print(g)
    print(g.to_adjacent_matrix())