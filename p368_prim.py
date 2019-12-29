#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 368页
    最小生成树 Prim
    """

    
import p341_graph as graph

def mst_prim(g, start_vertex=None):
    if start_vertex == None:
        start_vertex = g.vertices[0]
    for vertex in g.vertices:
        for edge in vertex.edges:
            edge.start = vertex.index
    vertex_set = [start_vertex.index]
    edge_queue = start_vertex.edges
    result = []
    get_weight = lambda edge: edge.weight
    while edge_queue:
        edge_queue.sort(key=get_weight)
        edge = edge_queue.pop(0)
        if edge.end not in vertex_set:
            vertex_set.append(edge.end)
            next_vertex = g.vertices[edge.end]
            for e in next_vertex.edges:
                if e not in result:
                    edge_queue.append(e)
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

    mst = mst_prim(g)
    for edge in mst:
        output = str(g.vertices[edge.start].key) + \
                 ' to ' + \
                 str(g.vertices[edge.end].key) + \
                 '\n----------'
        print(output)