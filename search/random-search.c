/*---- random search 随机搜索 ----
input：
6 3 #需要排序的元素数目和需要查找的数字
2 4 5 3 6 1
output:
3 #位置

random search: Theta(n)
------------------------------*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_LENGTH 100

//产生一个[0 : length-1]的均匀随机排列
void permute_by_sorting(int *array, int length) {
    int permute[MAX_LENGTH];
    int i,j,temp;
    srand((unsigned)time(NULL));
    for (i = 0; i < length; i++) {
        permute[i] = rand();
    }
    for (i = 0; i < length - 1; i++) {
        for (j = 1; j < length - i; j++) {
            if (permute[j-1] > permute[j]) {
                temp = permute[j-1];
                permute[j-1] = permute[j];
                permute[j] = temp;
                temp = array[j-1];
                array[j-1] = array[j];
                array[j] = temp;
            }
        }
    }
}

//随机搜索
int random_search(int *array, int length, int search_element, int *random_array) {
    int i;
    for (i = 0; i < length; i++) {
        if (array[random_array[i]] == search_element) {
            return random_array[i];
        }
    }
    return -1;
}

int main() {
    int index[MAX_LENGTH];
    int unsorted_array[MAX_LENGTH];
    int test_array_length;
    int test_search_element;
    int i;
    freopen("C:\\test_set\\unsorted_search_input.txt", "r", stdin);
    while (scanf("%d %d", &test_array_length, &test_search_element) != EOF) {
        for (i = 0; i < test_array_length; i++) {
            scanf("%d", &unsorted_array[i]);
        }

        for (i = 0; i < test_array_length; i++) {
            index[i] = i;
        }
        permute_by_sorting(index, test_array_length);

        i = random_search(unsorted_array, test_array_length, test_search_element, index);

        printf("result:\n");
        if (i == -1) {
            printf("Can't found %d!", test_search_element);
        } else {
            printf("%d", i);
        }
        printf("\n");
    }
    return 0;
}