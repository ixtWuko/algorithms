/*----- stack 栈 -----
测试数据：
10
4 5 2 7 9 3 1 0 6 8

LIFO
-------------------*/

#include <stdio.h>

typedef struct list_node {
    int value;
    struct list_node * next;
} lnode;

//start节点的value存放链表的节点数目，start节点不计算在内
lnode *build_stack() {
    lnode *start = malloc(sizeof(lnode));
    if (start != NULL) {
        start->value = 0;
        start->next = NULL;
    }
    return start;
}

int is_empty_stack(lnode *stack) {
    return stack->value == 0;
}

int stack_push(lnode *stack, int push_value) {
    lnode *push_node = malloc(sizeof(lnode));
    if (push_node == NULL) {
        return -1;
    }
    stack->value += 1;
    push_node->value = push_value;
    push_node->next = stack->next;
    stack->next = push_node;
    return stack->value;
}

int stack_pop(lnode *stack) {
    int pop_value;
    lnode *pop_node = stack->next;
    stack->value -= 1;
    stack->next = pop_node->next;
    pop_value = pop_node->value;
    free(pop_node);
    return pop_value;
}

void stack_print(lnode *stack) {
    int i;
    int length = stack->value;
    for (i = 0; i < length; i++) {
        stack = stack->next;
        printf("%d ", stack->value);
    }
}

int main() {
    int length, i;
    int this_value;
    lnode *this_node;
    lnode *test_stack = build_stack();
    freopen("C:\\test_set\\data-structs.txt", "r", stdin);
    while (scanf("%d", &length) != EOF) {
        for (i = 0; i < length; i++){
            scanf("%d", &this_value);
            stack_push(test_stack, this_value);
        }
    }

    stack_print(test_stack);
    printf("%d ", is_empty_stack(test_stack));
    this_value = stack_pop(test_stack);
    printf("%d ", this_value);
    if (stack_push(test_stack, 100) != -1) {
        stack_print(test_stack);
    }
    return 0;
}