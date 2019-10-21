#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""《算法导论》 112页
    桶排序"""

import re
from p110_radix_sort import radix_sort


def bucket_sort(lst):
    bucket = {}
    for word in lst:
        if word[0] in bucket:
            bucket[word[0]].append(word)
        else:
            bucket[word[0]] = [word]
    for key in bucket:
        radix_sort(bucket[key])
    lst.clear()
    for ele in list('abcdefghijklmnopqrstuvwxyz'):
        if ele in bucket:
            lst.extend(bucket[ele])


if __name__ == '__main__':
    paragraph = """The shark swung over and the old man saw his eye was not alive and then he swung over once again, 
    wrapping himself in two loops of the rope. The old man knew that he was dead but the shark would not accept it. 
    Then, on his back, with his tail lashing and his jaws clicking, the shark plowed over the water as a speedboat 
    does. The water was white where his tail beat it and three-quarters of his body was clear above the water when 
    the rope came taut, shivered, and then snapped. The shark lay quietly for a little while on the surface and the 
    old man watched him. Then he went down very slowly. """
    word_lst = re.split(r'\W+', paragraph)
    word_lst = [word.lower() for word in word_lst if len(word) > 0]
    bucket_sort(word_lst)
    print(word_lst)