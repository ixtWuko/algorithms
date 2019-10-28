#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 246页
    赫夫曼编码"""


class Huffman_tree_node(object):
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        self.parent = None
        self.code = ''

    def is_leaf(self):
        return self.left is None and self.right is None

    def is_left(self):
        return self is self.parent.left

    def is_right(self):
        return self is self.parent.right

    def get_freq(self):
        return self.freq

    def get_char(self):
        return self.char


class Huffman_tree(object):
    def __init__(self, freq_lst):
        node_list = [Huffman_tree_node(key, value) for key, value in freq_lst.items()]
        while len(node_list) > 1:
            node_list.sort(key=lambda x: x.get_freq(), reverse=True)
            node_a = node_list.pop()
            node_b = node_list.pop()
            node_list.append(self.__build_tree(node_a, node_b))
        self.root = node_list[0]
        self.build_dict()

    def __build_tree(self, node_a, node_b):
        node_p = Huffman_tree_node(None, node_a.get_freq() + node_b.get_freq())
        node_a.parent = node_p
        node_b.parent = node_p
        if node_a.get_freq() > node_b.get_freq():
            node_p.left = node_b
            node_p.right = node_a
        else:
            node_p.left = node_a
            node_p.right = node_b
        return node_p

    def build_dict(self, node=None, code=''):
        if node is None:
            node = self.root
        if node.left:
            self.build_dict(node.left, code+'0')
        if node.right:
            self.build_dict(node.right, code+'1')
        if node.is_leaf():
            node.code = code

    def __str(self, node):
        result = ''
        if node.is_leaf():
            result += node.char + ': ' + str(node.freq) + ', ' + node.code + '\n'
        else:
            if node.left:
                result += self.__str(node.left)
            if node.right:
                result += self.__str(node.right)
        return result

    def __str__(self):
        return self.__str(self.root)


if __name__ == '__main__':
    origin_string = """The shark swung over and the old man saw his eye was not alive and then he swung over once again, 
    wrapping himself in two loops of the rope. The old man knew that he was dead but the shark would not accept it. 
    Then, on his back, with his tail lashing and his jaws clicking, the shark plowed over the water as a speedboat 
    does. The water was white where his tail beat it and three-quarters of his body was clear above the water when 
    the rope came taut, shivered, and then snapped. The shark lay quietly for a little while on the surface and the 
    old man watched him. Then he went down very slowly. """
    freq_list = {}
    for ele in origin_string:
        if ele in freq_list:
            freq_list[ele] += 1
        else:
            freq_list[ele] = 1

    ht = Huffman_tree(freq_list)
    print(ht)