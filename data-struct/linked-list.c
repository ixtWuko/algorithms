/*----- linked list 链表 -----
测试数据：
10
4 5 2 7 9 3 1 0 6 8
--------------------------*/

#include <stdio.h>

typedef struct list_node {
    int value;
    struct list_node *next;
} lnode;

lnode *build_list() {
    lnode *start = malloc(sizeof(lnode));
    if (start != NULL) {
        start->value = 0;
        start->next = NULL;
    }
    return start;
}

lnode *list_search(lnode *list, int search_value) {
    lnode *p = list->next;
    while (p->value != search_value && p != NULL) {
        p = p->next;
    }
    return p;
}

int list_insert(lnode *list, int insert_value) {
    lnode *insert_node = malloc(sizeof(lnode));
    if (insert_node != NULL) {
        insert_node->value = insert_value;
        insert_node->next = list->next;
        list->value++;
        list->next = insert_node;
        return list->value;
    }
    return -1;
}

void list_delete(lnode *list, int delete_value) {
    lnode *delete_node_previous = list;
    lnode *delete_node = list->next;
    while (delete_node->value != delete_value && delete_node != NULL) {
        delete_node_previous = delete_node;
        delete_node = delete_node->next;
    }
    if (delete_node != NULL) {
        delete_node_previous->next = delete_node->next;
        list->value--;
        free(delete_node);
    }
}

int main() {

}