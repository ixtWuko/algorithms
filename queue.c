/*----- queue 队列 -----
测试数据：
10
4 5 2 7 9 3 1 0 6 8

FIFO
-------------------*/

#include <stdio.h>

typedef struct list_node {
    int value;
    struct list_node * next;
} lnode;

lnode *build_queue() {
    lnode *start = malloc(sizeof(lnode));
    if (start != NULL) {
        start->value = 0;
        start->next = NULL;
    }
    return start;
}

int is_empty_queue(lnode *queue) {
    return queue->value == 0;
}

int enqueue(lnode *queue, int enqueue_value) {
    lnode *enqueue_node;
    lnode *p = queue;
    while (p->next != NULL) {
        p = p->next;
    }
    enqueue_node = malloc(sizeof(lnode));
    if (enqueue_node != NULL) {
        queue->value++;
        enqueue_node->value = enqueue_value;
        enqueue_node->next = NULL;
        p->next = enqueue_node;
        return queue->value;
    }
    return -1;
}

int dequeue(lnode *queue) {
    int dequeue_value;
    lnode *dequeue_node = queue->next;
    queue->value--;
    queue->next = dequeue_node->next;
    dequeue_value = dequeue_node->value;
    free(dequeue_node);
    return dequeue_value;
}

void queue_print(lnode *queue) {
    int i;
    int length = queue->value;
    for (i = 0; i < length; i++) {
        queue = queue->next;
        printf("%d ", queue->value);
    }
}

int main() {
    int length, i;
    int this_value;
    lnode *this_node;
    lnode *test_queue = build_queue();
    freopen("C:\\test_set\\data-structs.txt", "r", stdin);
    while (scanf("%d", &length) != EOF) {
        for (i = 0; i < length; i++){
            scanf("%d", &this_value);
            enqueue(test_queue, this_value);
        }
    }

    queue_print(test_queue);
    printf("%d ", is_empty_queue(test_queue));
    this_value = dequeue(test_queue);
    printf("%d ", this_value);
    if (enqueue(test_queue, 100) != -1) {
        queue_print(test_queue);
    }
    return 0;
}