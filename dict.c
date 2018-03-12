/*----- dictionary(key-value) 字典 ------*/

typedef struct dict_node {
    char key[100];
    int value;
    struct dict_node *next;
} dnode;

/*----- 链接法解决散列表冲突 -----
typedef struct dict_child_node {
    int value;
    struct dict_child_node *next;
}
typedef struct dict_key_node {
    char key[100];
    struct dict_child_node *child;
    struct dict_key_node *next;
}
-------------------------------*/