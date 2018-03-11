/*---- heap sort 堆排序 ----
input：
6 #需要排序的元素数目
5 2 4 6 1 3
output:
1 2 3 4 5 6

heap sort: O(n log n)
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

int main() {
    //test
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

        heap_sort(test_set, test_set_length);
    
        printf("result:\n");
        for (i = 1; i < test_set_length; i++) {
            printf("%d ", test_set[i]);
        }
        printf("\n");
    }
    return 0;
}
