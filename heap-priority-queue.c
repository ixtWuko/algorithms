/*---- priority queue 优先队列 ----
using heap
---------------------------------*/

#include <stdio.h>

#define PARENT(i) (i / 2)
#define LEFT(i) (2 * i)
#define RIGHT(i) (2 * i + 1)

// 注意：下标是从1开始的，确保array[0]不会被用到
// 使一个堆中第i个内点满足最大堆的性质
void max_heapify(int *array, int length, int index) {
    //array从第一个元素开始，heap_size是数组的真实长度减一
    int l,r,largest;
    int temp;
    int heap_size = length - 1;
    l = LEFT(index);
    r = RIGHT(index);
    // 找出3个中最大的作为父节点
    if (l <= heap_size && array[l] > array[index]) {
        largest = l;
    } else {
        largest = index;
    }
    if (r <= heap_size && array[r] > array[largest]) {
        largest = r;
    }
    if (largest != index) {
        temp = array[index];
        array[index] = array[largest];
        array[largest] = temp;
        max_heapify(array, length, largest);
    }
}

// 从一个无序数组中构建最大堆
void build_max_heap(int *array, int length) {
    int i;
    int heap_size = length-1;
    // 数组的后半部分是树叶，前半部分是内点
    for (i = heap_size / 2; i > 0; i--) {
        max_heapify(array, length, i);
    }
}

/*------------------------- 堆排序算法 ---------------------------------------
- 将堆的根与最后一个树叶交换，交换后将堆的size减一；（此时堆后面的有效元素是排好的。）
- 使用max_heapify恢复堆的性质；
- 重复上述两步，直至堆中只剩下根，此时的array是排好顺序的。
---------------------------------------------------------------------------*/

void heap_sort(int *array, int length) {
    int i;
    int temp;
    int heap_size = length - 1;
    build_max_heap(array, length);
    for (i = heap_size; i > 1; i--) {
        temp = array[i];
        array[i] = array[1];
        array[1] = temp;
        max_heapify(array, i, 1);
        heap_size--;
    }
}

/*------------------------ 优先队列的实现 ---------------------------*/
int heap_maximum(int *array) {
    return array[1];
}

// 弹出最大的元素
int heap_extract_max(int *array, int length) {
    int heap_size = length - 1;
    int max;
    if (heap_size < 1) {
        printf("error: heap underflow!\n");
    }
    max = array[1];
    array[1] = array[heap_size];
    max_heapify(array, heap_size, 1);
    return max;
}

// 分配新的位置
void heap_inscrease_key(int *array, int index, int value) {
    int temp;
    if (array[index] > value) {
        printf("error: new value is smaller than current one!\n");
    }
    array[index] = value;
    while (index > 1 && array[PARENT(index)] < array[index]) {
        temp = array[index];
        array[index] = array[PARENT(index)];
        array[PARENT(index)] = temp;
        index = PARENT(index);
    }
}

// 插入一个元素
void max_heap_insert(int *array, int length, int value) {
    int new_length = length+1;
    int new_heap_size = length;
    array[new_heap_size] = value;
    heap_inscrease_key(array, new_length, value);
}

int main() {
    int test_set[1000];
    int test_set_length; 
    int i;
    test_set[0] = 0;
    freopen("C:\\test_set\\unsorted_input.txt", "r", stdin);
    while (scanf("%d", &test_set_length) != EOF) {
        test_set_length++;
        for (i = 1; i < test_set_length; i++) {
            scanf("%d", &test_set[i]);
        }

        build_max_heap(test_set, test_set_length);
    
        printf("result:\n");
        for (i = 1; i < test_set_length; i++) {
            printf("%d ", test_set[i]);
        }
        printf("\n");

        //test for priority queue
        printf("the max value of this heap is: %d\n", heap_extract_max(test_set, test_set_length));
        test_set_length--;

        max_heap_insert(test_set, test_set_length, 100);
        test_set_length++;

        printf("now the max value is: %d\n", heap_maximum(test_set));
    }
    return 0;
}
