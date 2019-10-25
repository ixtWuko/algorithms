#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 192页
    动态顺序统计"""

from a_sequence_generator import generate_sequence


Red = True
Black = False


class Tree_node:
    def __init__(self, data):
        self.data = data
        self.color = Black
        self.size = 1
        self.p = None
        self.left = None
        self.right = None

    def __str__(self):
        if self.color:
            color = 'R'
        else:
            color = 'B'
        return 'color: ' + color + ' size: ' + str(self.size) + ' value: ' + str(self.data)


class Order_statistic_tree:
    def __init__(self):
        self.root = None

    def inorder_tree_walk(self, node=None):
        result = []
        if node is None:
            node = self.root
        if node:
            if node.left:
                result.extend(self.inorder_tree_walk(node.left))
            result.append(node.__str__())
            if node.right:
                result.extend(self.inorder_tree_walk(node.right))
        return result

    def __str__(self):
        return str(self.inorder_tree_walk())

    def search(self, data, node=None):
        if node is None:
            node = self.root
        while node:
            if node.data == data:
                return node
            elif node.data < data:
                node = node.right
            else:
                node = node.left
        return None

    def maximum(self, node=None):
        if node is None:
            node = self.root
        while node.right:
            node = node.right
        return node

    def minimum(self, node=None):
        if node is None:
            node = self.root
        while node.left:
            node = node.left
        return node

    def successor(self, node):
        if node.right:
            return self.minimum(node.right)
        node_tmp = node.p
        while node_tmp and (node is node_tmp.right):
            node = node_tmp
            node_tmp = node_tmp.p
        return node_tmp

    def predecessor(self, node):
        if node.left:
            return self.maximum(node.left)
        node_tmp = node.p
        while node_tmp and (node is node_tmp.left):
            node = node_tmp
            node_tmp = node_tmp.p
        return node_tmp

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.p = x
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y
        y.size = x.size
        if x.left and x.right:
            x.size = x.left.size + x.right.size + 1
        elif x.left:
            x.size = x.left.size + 1
        elif x.right:
            x.size = x.right.size + 1
        else:
            x.size = 1

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.p = x
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.right = x
        x.p = y
        y.size = x.size
        if x.left and x.right:
            x.size = x.left.size + x.right.size + 1
        elif x.left:
            x.size = x.left.size + 1
        elif x.right:
            x.size = x.right.size + 1
        else:
            x.size = 1

    def __insert_fixup(self, node):
        while node.p and node.p.color == Red:
            if node.p is node.p.p.left:
                uncle_node = node.p.p.right
                if uncle_node and uncle_node.color == Red:
                    node.p.color = Black
                    uncle_node.color = Black
                    node.p.p.color = Red
                    node = node.p.p
                else:
                    if node is node.p.right:
                        node = node.p
                        self.left_rotate(node)
                    node.p.color = Black
                    node.p.p.color = Red
                    self.right_rotate(node.p.p)
            else:
                uncle_node = node.p.p.left
                if uncle_node and uncle_node.color == Red:
                    node.p.color = Black
                    uncle_node.color = Black
                    node.p.p.color = Red
                    node = node.p.p
                else:
                    if node is node.p.left:
                        node = node.p
                        self.right_rotate(node)
                    node.p.color = Black
                    node.p.p.color = Red
                    self.left_rotate(node.p.p)
        self.root.color = Black

    def insert(self, data):
        insertion_node = Tree_node(data)
        if self.root is None:
            self.root = insertion_node
        else:
            insertion_node.color = Red
            parent_node = self.root
            while parent_node:
                if data <= parent_node.data:
                    if parent_node.left:
                        parent_node = parent_node.left
                    else:
                        parent_node.left = insertion_node
                        insertion_node.p = parent_node
                        break
                else:
                    if parent_node.right:
                        parent_node = parent_node.right
                    else:
                        parent_node.right = insertion_node
                        insertion_node.p = parent_node
                        break
            size_change_node = insertion_node.p
            while size_change_node:
                size_change_node.size += 1
                size_change_node = size_change_node.p
            self.__insert_fixup(insertion_node)

    def __delete_fixup(self, node):
        """ref: https://zhuanlan.zhihu.com/p/22800206"""
        while node is not self.root and node.color == Black:
            if node is node.p.left:
                bro = node.p.right
                if bro.color == Red:
                    # case 5
                    bro.color = Black
                    bro.left.color = Red
                    self.left_rotate(node.p)
                    break
                else:
                    if bro.left is None and bro.right is None:
                        # case 4
                        bro.color = Red
                        node = node.p
                    elif bro.right is None:
                        # case 2
                        bro.color = Red
                        bro.left.color = Black
                        self.right_rotate(bro)
                    else:
                        # case 1,3
                        bro.color = node.p.color
                        bro.right.color = Black
                        node.p.color = Black
                        self.left_rotate(node.p)
                        break
            else:
                bro = node.p.left
                if bro.color == Red:
                    # case 5
                    bro.color = Black
                    bro.right.color = Red
                    self.right_rotate(node.p)
                    break
                else:
                    if bro.left is None and bro.right is None:
                        # case 4
                        bro.color = Red
                        node = node.p
                    elif bro.left is None:
                        # case 2
                        bro.color = Red
                        bro.right.color = Black
                        self.left_rotate(bro)
                    else:
                        # case 1,3
                        bro.color = node.p.color
                        bro.left.color = Black
                        node.p.color = Black
                        self.right_rotate(node.p)
                        break

    def delete(self, node):
        if node.left is None and node.right is None:
            # has no subtree
            if node.color == Black:
                self.__delete_fixup(node)
            if node is node.p.left:
                node.p.left = None
            else:
                node.p.right = None
            size_change_node = node.p
            while size_change_node:
                size_change_node.size -= 1
                size_change_node = size_change_node.p
            del node
        elif node.left is None:
            node.data = node.right.data
            self.delete(node.right)
        elif node.right is None:
            node.data = node.left.data
            self.delete(node.left)
        else:
            # has two subtree
            node_tmp = self.successor(node)
            node.data = node_tmp.data
            self.delete(node_tmp)

    def select(self, ith, node=None):
        if node is None:
            node = self.root
        if node.left:
            r = node.left.size + 1
        else:
            r = 1
        if ith == r:
            return node
        elif ith < r:
            return self.select(ith, node=node.left)
        else:
            return self.select(ith-r, node=node.right)

    def rank(self, node):
        if node.left:
            r = node.left.size + 1
        else:
            r = 1
        tmp_node = node
        while tmp_node is not self.root:
            if tmp_node is tmp_node.p.right and tmp_node.p.left:
                r += tmp_node.p.left.size + 1
            tmp_node = tmp_node.p
        return r


if __name__ == '__main__':
    t = Tree_node(35)
    print(t)

    unsorted = generate_sequence()
    print(unsorted)

    ost = Order_statistic_tree()
    for ele in unsorted:
        ost.insert(ele)
    print(ost)
    for ele in unsorted[:10]:
        t = ost.search(ele)
        if t:
            ost.delete(t)
        print(ost)

    for ith in range(1, 10):
        t = ost.select(ith)
        if t:
            print(t)
            print(ost.rank(t))