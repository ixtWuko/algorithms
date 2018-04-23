#include <stdio.h>

/*----- binary tree 二叉树 -----*/
typedef struct tree_node {
    int value;
    struct tree_node *left;
    struct tree_node *right;
} tnode;

/*----- tree 树 ------*/
typedef struct tree_node {
    int value;
    struct tree_node *parent;
    struct tree_node *left_tree;
    struct tree_node *right_brother;
} tnode;