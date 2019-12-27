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

    def bfs(self, func, start):
        ''' 广度优先搜索，广度优先树
            树中节点的后继可以通过bfs_distance判断 '''
        WHITE = False
        BLACK = True
        for vertex in self.vertices:
            vertex.color = WHITE
            vertex.bfs_distance = len(self.vertices)
            vertex.bfs_precursor = None
        start.bfs_distance = 0
        queue = [start]
        while queue:
            current = queue.pop(0)
            func(current)
            current.color = BLACK
            for ele in current.edges:
                next_vertex = self.vertices[ele.end]
                if next_vertex.color == WHITE:
                    next_vertex.bfs_distance = current.bfs_distance + 1
                    next_vertex.bfs_precursor = current
                    if next_vertex not in queue:
                        queue.append(next_vertex)

    def dfs(self, func, start):
        ''' 深度优先搜索，深度优先森林 '''
        WHITE = False
        BLACK = True
        for vertex in self.vertices:
            vertex.color = WHITE
            vertex.dfs_precursor = None
        time = 0
        
        def visit(vert):
            func(vert)
            vert.color = BLACK
            nonlocal time
            time += 1
            vert.dfs_discover_time = time
            for ele in vert.edges:
                if self.vertices[ele.end].color == WHITE:
                    self.vertices[ele.end].dfs_precursor = vert
                    visit(self.vertices[ele.end])
                    break
            time += 1
            vert.dfs_finish_time = time

        for vertex in [start] + self.vertices:
            if vertex.color == WHITE:
                visit(vertex)

    def topological_sort(self):
        self.dfs(print_vertex, self.vertices[0])
        result = self.vertices
        get_finish_time = lambda vertex: vertex.dfs_finish_time
        result.sort(key=get_finish_time)
        return result


def print_vertex(vert):
    print('work on vertex index: ', vert.index)

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
    print('----------')
    g.bfs(print_vertex, g.vertices[0])
    print('----------')
    g.dfs(print_vertex, g.vertices[0])
    print('----------')
    print(g.topological_sort())