/*---- randomized select 随机选择算法 ----
input:
6 5
5 2 4 6 1 3
output:
the 5th element is 5

randomized select: 期望运行时间 Theta (n)
如果寻找更好的key值, 可以使select的最坏运行时间为 Theta(n)
------------------------------------*/


#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int randomized_partition(int *array, int start_index, int end_index) {
    int temp, key;
    int i,j;
    srand((unsigned)time(0));
    i = rand() % (start_index - end_index) + start_index;
    temp = array[i];
    array[i] = array[end_index];
    array[end_index] = temp;

    j = start_index;
    key = array[end_index];
    for (i = start_index; i < end_index; i++) {
        if (array[i] <= key) {
            temp = array[i];
            array[i] = array[j];
            array[j] = temp;
            j++;
        }
    }
    temp = array[end_index];
    array[end_index] = array[j];
    array[j] = temp;
    return j;
}

int randomized_select(int *array, int start_index, int end_index, int ith) {
    int middle_index;
    int kth;
    if (start_index == end_index) {
        return array[start_index];
    }
    middle_index = randomized_partition(array, start_index, end_index);
    kth = middle_index - start_index + 1;
    if (ith == kth) {
        return array[middle_index];
    } else if (ith < kth) {
        return randomized_select(array, start_index, middle_index - 1, ith);
    } else {
        return randomized_select(array, middle_index+1, end_index, ith - kth);
    }

}

// test
int main() {
    int test_set[100];
    int test_set_length; 
    int i;
    int ith;
    freopen("C:\\test_set\\select_input.txt", "r", stdin);
    while (scanf("%d %d", &test_set_length, &ith) != EOF) {
        for (i = 0; i < test_set_length; i++) {
            scanf("%d", &test_set[i]);
        }

        i = randomized_select(test_set, 0, test_set_length-1, ith);
    
        printf("the %dth element is %d\n", ith, i);
    }
    return 0;
}