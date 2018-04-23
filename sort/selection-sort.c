/*---- selection sort 选择排序 -----*/

#include <stdio.h>

void selection_sort(int *unsorted, int length) {
    int min_element;
    int min_element_index;
    int i,j;
    for (i = 0; i < length - 1; i++) {
        min_element = unsorted[i];
        min_element_index = i;
        for (j = i+1; j < length; j++) {
            if (unsorted[j] < min_element) {
                min_element = unsorted[j];
                min_element_index = j;
            }
        }
        //元素后移
        while (i < min_element_index) {
            unsorted[min_element_index] = unsorted[min_element_index - 1];
            min_element_index--;
        }
        unsorted[i] = min_element;
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

        selection_sort(test_set, test_set_length);
    
        printf("result:\n");
        for (i = 0; i < test_set_length; i++) {
            printf("%d ", test_set[i]);
        }
        printf("\n");
    }
    return 0;
}