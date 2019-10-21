#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 110页
    基数排序"""

import re
from a_swap import swap


def get_alphabet(word, index):
    """return the index-th alphabet of a word
       if index > length-of-word, return '0' """
    if index > len(word) - 1:
        return '0'
    else:
        return word[index]


def radix_sort(lst):
    """sorting a word list to dict-order"""
    # get the length of the longest word
    longest_length = 0
    if len(lst) < 0:
        return
    for i in range(len(lst)):
        if len(lst[i]) > longest_length:
            longest_length = len(lst[i])
    # sorting
    for i in range(longest_length-1, -1, -1):
        # using any stable sorting algo, for example bubble sort
        for x in range(1, len(lst)):
            for y in range(len(lst) - x):
                if get_alphabet(lst, y) > get_alphabet(lst, y+1):
                    swap(lst, y, y+1)


if __name__ == '__main__':
    paragraph = """The shark swung over and the old man saw his eye was not alive and then he swung over once again, 
    wrapping himself in two loops of the rope. The old man knew that he was dead but the shark would not accept it. 
    Then, on his back, with his tail lashing and his jaws clicking, the shark plowed over the water as a speedboat 
    does. The water was white where his tail beat it and three-quarters of his body was clear above the water when 
    the rope came taut, shivered, and then snapped. The shark lay quietly for a little while on the surface and the 
    old man watched him. Then he went down very slowly. """
    word_lst = re.split(r'\W+', paragraph)
    word_lst = [word.lower() for word in word_lst if len(word) > 0]
    radix_sort(word_lst)
    print(word_lst)