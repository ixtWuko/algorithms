/*---- quick sort 快速排序 -----*/

#include <stdio.h>

void quick_sort(int *array, int start_index, int end_index) {
    int key, temp;
    int i,j;
    if (start_index < end_index) {
        key = array[end_index];
        i = start_index;
        for (j = start_index; j < end_index; j++) {
            if (array[j] <= key) {
                temp = array[i];
                array[i] = array[j];
                array[j] = temp;
                i++;
            }
        }
        temp = array[i];
        array[i] = array[end_index];
        array[end_index] = temp;
        
        quick_sort(array, start_index, i-1);
        quick_sort(array, i+1, end_index);
    }
}

int main() {
    //test
    int test_set[100];
    int test_set_length; 
    int i;
    freopen("C:\\test_set\\unsorted_input.txt", "r", stdin);
    while (scanf("%d", &test_set_length) != EOF) {
        for (i = 0; i < test_set_length; i++) {
            scanf("%d", &test_set[i]);
        }

        quick_sort(test_set, 0, test_set_length-1);

        printf("result:\n");
        for (i = 0; i < test_set_length; i++) {
            printf("%d ", test_set[i]);
        }
        printf("\n");
    }
    return 0;
}