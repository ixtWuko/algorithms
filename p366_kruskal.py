#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 366页
    最小生成树 Kruskal
    """


import p341_graph as graph

def mst_kruskal(g):
    edges = []
    for vertex in g.vertices:
        for edge in vertex.edges:
            edge.start = vertex.index
            edges.append(edge)
    get_weight = lambda edge: edge.weight
    edges.sort(key=get_weight)
    vertex_set = {i:i for i in range(len(g.vertices))}
    result = []
    for edge in edges:
        if vertex_set[edge.start] == vertex_set[edge.end]:
            continue
        else:
            end_group = vertex_set[edge.end]
            for key,item in vertex_set.items():
                if item == end_group:
                    vertex_set[key] = edge.start
            result.append(edge)
    return result


if __name__ == '__main__':
    keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    mat = [
        [0,4,0,0,0,0,0,8,0],
        [4,0,8,0,0,0,0,11,0],
        [0,8,0,7,0,4,0,0,2],
        [0,0,7,0,9,14,0,0,0],
        [0,0,0,9,0,10,0,0,0],
        [0,0,4,14,10,0,2,0,0],
        [0,0,0,0,0,2,0,1,6],
        [8,11,0,0,0,0,1,0,7],
        [0,0,2,0,0,0,6,7,0]
    ]

    g = graph.Graph()
    g.from_adjacent_matrix(False, keys, mat)
    print(g)

    mst = mst_kruskal(g)
    for edge in mst:
        output = str(g.vertices[edge.start].key) + \
                 ' to ' + \
                 str(g.vertices[edge.end].key) + \
                 '\n----------'
        print(output)