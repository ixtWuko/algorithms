#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 341页
    单源最短路径算法
    """


import p341_graph as graph

def initialize_single_source(g, start_vertex=None):
    if start_vertex == None:
        start_vertex = g.vertices[0]
    for vertex in g.vertices:
        vertex.d = float('inf')
        vertex.pi = None
    start_vertex.d = 0

def relax(u,v):
    weight = None
    for edge in u.edges:
        if v.index == edge.end:
            weight = edge.weight
    if weight is not None:
        if v.d > u.d + weight:
            v.d = u.d + weight
            v.pi = u

def bellman_ford(g, start_vertex=None):
    if start_vertex == None:
        start_vertex = g.vertices[0]
    initialize_single_source(g,start_vertex)
    for i in range(len(g.vertices)):
        for vertex in g.vertices:
            for edge in vertex.edges:
                relax(vertex, g.vertices[edge.end])
    for vertex in g.vertices:
        for edge in vertex.edges:
            end_vertex = g.vertices[edge.end]
            if end_vertex.d > vertex.d + edge.weight:
                return False
    return True

def dijkstra(g, start_vertex=None):
    if start_vertex == None:
        start_vertex = g.vertices[0]
    initialize_single_source(g,start_vertex)
    s = []
    q = g.vertices.copy()
    get_d = lambda vertex: vertex.d
    while q:
        q.sort(key=get_d)
        u = q.pop(0)
        s.append(u)
        for edge in u.edges:
            relax(u, g.vertices[edge.end])
    return s

if __name__ == '__main__':
    # test bellman ford
    # keys = ['s', 't', 'x', 'y', 'z']
    # mat = [
    #     [0,6,0,7,0],
    #     [0,0,5,8,-4],
    #     [0,-2,0,0,0],
    #     [0,0,-3,0,9],
    #     [2,0,7,0,0]
    # ]

    # g1 = graph.Graph()
    # g1.from_adjacent_matrix(False, keys, mat)
    # print(g1)

    # print(bellman_ford(g1))

    # test dijkstra
    keys = ['s', 't', 'x', 'y', 'z']
    mat = [
        [0,10,0,5,0],
        [0,0,1,2,0],
        [0,0,0,0,4],
        [0,3,9,0,2],
        [7,0,6,0,0]
    ]

    g2 = graph.Graph()
    g2.from_adjacent_matrix(False, keys, mat)
    print(g2)

    s = dijkstra(g2)
    for vertex in s:
        print(vertex.key)