/*----- binary tree 二叉树 -----*/

#include <stdio.h>

typedef struct tree_node {
    int value;
    struct tree_node *left;
    struct tree_node *right;
} tnode;

