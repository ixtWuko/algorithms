#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 161页
    二叉搜索树"""


class Tree_node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.data)

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_left(self):
        return self.left

    def set_left(self, left_ref):
        self.left = left_ref

    def get_right(self):
        return self.right

    def set_right(self, right_ref):
        self.right = right_ref

    def get_parent(self):
        return self.parent

    def set_parent(self, parent_ref):
        self.parent = parent_ref


class Binary_tree:
    def __init__(self):
        self.root = None

    def inorder_tree_walk(self, node=None):
        result = []
        if node is None:
            node = self.root
        if node:
            if node.get_left():
                result.extend(self.inorder_tree_walk(node.get_left()))
            result.append(node.get_data())
            if node.get_right():
                result.extend(self.inorder_tree_walk(node.get_right()))
        return result

    def preorder_tree_walk(self, node=None):
        result = []
        if node is None:
            node = self.root
        if node:
            result.append(node.get_data())
            if node.get_left():
                result.extend(self.preorder_tree_walk(node.get_left()))
            if node.get_right():
                result.extend(self.preorder_tree_walk(node.get_right()))
        return result

    def postorder_tree_walk(self, node=None):
        result = []
        if node is None:
            node = self.root
        if node:
            if node.get_left():
                result.extend(self.postorder_tree_walk(node.get_left()))
            if node.get_right():
                result.extend(self.postorder_tree_walk(node.get_right()))
            result.append(node.get_data())
        return result

    def __str__(self):
        return str(self.preorder_tree_walk())

    def search(self, data, node=None):
        if node is None:
            node = self.root
        while node:
            if node.get_data() == data:
                return node
            elif node.get_data() < data:
                node = node.get_right()
            else:
                node = node.get_left()
        return None

    def maximum(self, node=None):
        if node is None:
            node = self.root
        while node.get_right():
            node = node.get_right()
        return node

    def minimum(self, node=None):
        if node is None:
            node = self.root
        while node.get_left():
            node = node.get_left()
        return node

    def successor(self, node):
        if node.get_right():
            return self.minimum(node.get_right())
        node_tmp = node.get_parent()
        while node_tmp and (node is node_tmp.get_right()):
            node = node_tmp
            node_tmp = node_tmp.get_parent()
        return node_tmp

    def predecessor(self, node):
        if node.get_left():
            return self.maximum(node.get_left)
        node_tmp = node.get_parent()
        while node_tmp and (node is node_tmp.get_left()):
            node = node_tmp
            node_tmp = node_tmp.get_parent()
        return node_tmp

    def insert(self, data):
        insertion_node = Tree_node(data)
        if self.root is None:
            self.root = insertion_node
        else:
            parent_node = self.root
            while parent_node:
                if data <= parent_node.get_data():
                    if parent_node.get_left():
                        parent_node = parent_node.get_left()
                    else:
                        parent_node.set_left(insertion_node)
                        insertion_node.set_parent(parent_node)
                        break
                else:
                    if parent_node.get_right():
                        parent_node = parent_node.get_right()
                    else:
                        parent_node.set_right(insertion_node)
                        insertion_node.set_parent(parent_node)
                        break

    # def __transplant(self, u, v):
    #     if u.get_parent() is None:
    #         self.root = v

    def delete(self, node):
        parent_node = node.get_parent()
        left_node = node.get_left()
        right_node = node.get_right()
        if left_node is None and right_node is None:
            # has no left subtree, no right subtree
            if node is parent_node.get_left():
                parent_node.set_left(None)
            else:
                parent_node.set_right(None)
            del node
        elif left_node and right_node:
            # has left subtree and right subtree
            alter_node = self.minimum(right_node)
            self.delete(alter_node)
        elif left_node:
            # only has left subtree
            left_node.set_parent(parent_node)
            if node is parent_node.get_left():
                parent_node.set_left(left_node)
            else:
                parent_node.set_right(left_node)
            del node
        else:
            # only has right subtree
            right_node.set_parent(parent_node)
            if node is parent_node.get_left():
                parent_node.set_left(right_node)
            else:
                parent_node.set_right(right_node)
            del node


if __name__ == '__main__':
    t = Tree_node(35)
    print(t, t.get_left(), t.get_right(), t.get_parent())
    unsorted = [49, 27, 65, 97, 76, 12, 38]
    bst = Binary_tree()
    for ele in unsorted:
        bst.insert(ele)
    print(bst)
    n = bst.search(76)
    bst.delete(n)
    print(bst)