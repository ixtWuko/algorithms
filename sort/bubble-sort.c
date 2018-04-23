/*---- bubble sort 冒泡排序 ----*/

#include <stdio.h>

void bubble_sort(int *unsorted, int length) {
    int i,j;
    int temp;
    for (i = 0; i < length - 1; i++) {
        for (j = 1; j < length - i; j++) {
            if (unsorted[j-1] > unsorted[j]) {
                temp = unsorted[j-1];
                unsorted[j-1] = unsorted[j];
                unsorted[j] = temp;
            }
        }
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

        bubble_sort(test_set, test_set_length);

        printf("result:\n");
        for (i = 0; i < test_set_length; i++) {
            printf("%d ", test_set[i]);
        }
        printf("\n");
    }
    return 0;
}