/*---- counting sort 计数排序 ----*/

#include <stdio.h>

#define MAX_LENGTH 500

void counting_sort(int *array, int *result, int length) {
    int counter_length = MAX_LENGTH + 1;
    int counter[MAX_LENGTH + 1];
    int i;
    for (i = 0; i < counter_length; i++) {
        counter[i] = 0;
    }
    for (i = 0; i < length; i++) {
        counter[array[i]]++;
    }

    for (i = 1; i < counter_length; i++) {
        counter[i] += counter[i-1];
    }
    for (i = length-1; i >= 0; i--) {
        result[counter[array[i]]-1] = array[i]; // 需要将下标减一
        counter[array[i]]--;
    }
}

int main() {
    //test
    int test_set[MAX_LENGTH];
    int test_set_length;
    int result[MAX_LENGTH];
    int i;
    freopen("C:\\test_set\\unsorted_input.txt", "r", stdin);
    while (scanf("%d", &test_set_length) != EOF) {
        for (i = 0; i < test_set_length; i++) {
            scanf("%d", &test_set[i]);
        }

        counting_sort(test_set, result, test_set_length);

        printf("result:\n");
        for (i = 0; i < test_set_length; i++) {
            printf("%d ", result[i]);
        }
        printf("\n");
    }
    return 0;
}