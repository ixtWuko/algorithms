/*---- insertion sort 插入排序 ----*/

#include <stdio.h>

void insertion_sort(int *unsorted, int length) {
    int key;
    int i,j;
    for (i = 1; i < length; i++) {
        key = unsorted[i];
        j = i-1;
        //将大于key的每个元素都后移一格
        while (j>=0 && unsorted[j] > key) {
            unsorted[j+1] = unsorted[j];
            j--;
        }
        //将key插入
        unsorted[j+1] = key;
    }
}

int main() {
    //test
    int test_set[1000];
    int test_set_length; 
    int i;
    freopen("C:\\test_set\\unsorted_input.txt", "r", stdin);
    while (scanf("%d", &test_set_length) != EOF) {
        for (i = 0; i < test_set_length; i++) {
            scanf("%d", &test_set[i]);
        }

        insertion_sort(test_set, test_set_length);
    
        printf("result:\n");
        for (i = 0; i < test_set_length; i++) {
            printf("%d ", test_set[i]);
        }
        printf("\n");
    }
    return 0;
}