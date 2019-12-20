#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 279页
    B树
    重点是在插入元素后节点的拆分与合并"""


class B_tree_node(object):
    def __init__(self, keys=None, children=None):
        if children is None:
            children = []
        if keys is None:
            keys = []
        self.keys = keys
        self.children = children
        self.parent = None

    def is_leaf(self):
        return not bool(self.children)


class B_tree(object):
    def __init__(self, t):
        self.root = B_tree_node()
        self.minimum_degree = t
        # the count of keys are t-1 to 2t-1
        # so the max index of keys are t-2 to 2t-2

    def search(self, value):
        node = self.root
        while node:
            i = 0
            while i < len(node.keys) and value > node.keys[i]:
                i += 1
            if i < len(node.keys) and value == node.keys[i]:
                return node, i
            node = node.children[i] if node.children else None
        return None, None

    def insert(self, value):
        def split_child(node, ith):
            """node's ith child is full, split it to two part"""
            the_child = node.children[ith]
            middle = self.minimum_degree - 1

            moving_key = the_child.keys[middle]
            rhs_keys = the_child.keys[middle+1:]
            rhs_children = the_child.children[middle+1:]
            new_node = B_tree_node(rhs_keys, rhs_children)
            new_node.parent = node

            node.keys.insert(ith, moving_key)
            node.children.insert(ith+1, new_node)
            the_child.keys = the_child.keys[:middle]
            the_child.children = the_child.children[:middle+1]

        def insert_nonfull(node, val):
            i = 0
            while i < len(node.keys) and val > node.keys[i]:
                i += 1
            if node.is_leaf():
                node.keys.insert(i, val)
            else:
                if len(node.children[i].keys) == 2 * self.minimum_degree - 1:
                    split_child(node, i)
                    if val > node.keys[i]:
                        i += 1
                insert_nonfull(node.children[i], val)

        if len(self.root.keys) == 2 * self.minimum_degree - 1:
            # the root is full
            new_root = B_tree_node()
            new_root.children.append(self.root)
            self.root = new_root
            split_child(new_root, 0)
        insert_nonfull(self.root, value)

    def delete(self, value, pnode=None):
        if pnode is None:
            pnode = self.root
        # 《算法导论》286页
        # case 1 注意之后的步骤会保证该叶节点的关键字数目大于t-1
        if pnode.is_leaf():
            if value in pnode.keys:
                pnode.keys.pop(pnode.keys.index(value))
                return value
            else:
                return None
        elif value in pnode.keys:
            # case 2
            ith = pnode.keys.index(value)
            y = pnode.children[ith]
            z = pnode.children[ith+1]
            if len(y.keys) >= self.minimum_degree:
                # case 2a
                predecessor = y
                while predecessor.children:
                    predecessor = predecessor.children[-1]
                value = predecessor.keys[-1]
                pnode.keys[ith] = predecessor.keys[-1]
                return self.delete(value, y)
            elif len(z.keys) >= self.minimum_degree:
                # case 2b
                successor = z
                while successor.children:
                    successor = successor.children[0]
                value = successor.keys[0]
                pnode.keys[ith] = successor.keys[0]
                return self.delete(value, z)
            else:
                # case 2c
                tmp = pnode.keys.pop(ith)
                y.keys.append(tmp)
                y.keys.extend(z.keys)
                y.children.extend(z.children)
                pnode.children.pop(ith+1)
                del z
                if pnode is self.root and len(pnode.keys) == 0:
                    self.root = y
                    del pnode
                return self.delete(value, y)
        else:
            # case 3
            child_num = 0
            while child_num < len(pnode.keys) and value > pnode.keys[child_num]:
                child_num += 1
            node = pnode.children[child_num]
            if len(node.keys) == self.minimum_degree - 1:
                little_bro = None
                if child_num > 0:
                    little_bro = pnode.children[child_num - 1]
                big_bro = None
                if child_num < len(pnode.keys):
                    big_bro = pnode.children[child_num+1]
                if little_bro and len(little_bro.keys) >= self.minimum_degree:
                    # case 3a
                    tmp = pnode.keys.pop(child_num-1)
                    node.keys.insert(0, tmp)
                    tmp = little_bro.keys.pop()
                    pnode.keys.insert(child_num-1, tmp)
                    if little_bro.children:
                        tmp = little_bro.children.pop()
                        node.children.insert(0, tmp)
                elif big_bro and len(big_bro.keys) >= self.minimum_degree:
                    tmp = pnode.keys.pop(child_num)
                    node.keys.append(tmp)
                    tmp = big_bro.keys.pop(0)
                    pnode.keys.insert(child_num, tmp)
                    if big_bro.children:
                        tmp = big_bro.children.pop(0)
                        node.children.append(tmp)
                else:
                    # case 3b
                    if little_bro:
                        tmp = pnode.keys.pop(child_num-1)
                        little_bro.keys.append(tmp)
                        little_bro.keys.extend(node.keys)
                        little_bro.children.extend(node.children)
                        pnode.children.pop(child_num)
                        del node
                        if pnode is self.root and len(pnode.keys) == 0:
                            self.root = little_bro
                            del pnode
                        node = little_bro
                    else:
                        tmp = pnode.keys.pop(child_num)
                        node.keys.append(tmp)
                        node.keys.extend(big_bro.keys)
                        node.children.extend(big_bro.children)
                        pnode.children.pop(child_num+1)
                        del big_bro
                        if pnode is self.root and len(pnode.keys) == 0:
                            self.root = node
                            del pnode
            return self.delete(value, node)


if __name__ == '__main__':
    unsorted = [536, 522, 4, 865, 813, 423, 254, 176, 995, 268, 632, 861, 872, 349, 628, 808, 70, 945, 712, 683, 84,
                331, 366, 441, 223, 133, 454, 837, 194, 756, 403, 379, 952, 286, 177, 653, 351, 360, 39, 893, 530, 372,
                424, 502, 527, 390, 969, 620, 64, 181, 109, 598, 615, 187, 206, 95, 478, 442, 590, 847, 545, 260, 280,
                650, 698, 835, 798, 790, 343, 851, 373, 326, 755, 346, 192, 175, 143, 243, 538, 233, 634, 651, 413, 258,
                764, 131, 466, 782, 57, 229, 634, 398, 918, 709, 619, 926, 180, 481, 628, 920]
    bt = B_tree(3)
    for ele in unsorted:
        bt.insert(ele)

    # unsorted.reverse()
    for ele in unsorted:
        print('*' * 30)
        print(ele)
        n, i = bt.search(ele)
        print(i)
        success = bt.delete(ele)
        print(success)
        n, i = bt.search(ele)
        print(i)
