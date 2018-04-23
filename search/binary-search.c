/*---- binary search 二分搜索 ----
input：
6 3 #需要排序的元素数目和需要查找的数字
1 2 3 4 5 6
output:
3 #位置是第三个

binary search: Theta(log n)
-----------------------------*/

#include <stdio.h>

int binary_search(int *unsorted, int length, int search_element, int start) {
    int i = length / 2;
    if (unsorted[i] == search_element) {
        return start + i + 1;
    } else if (unsorted[i] > search_element) {
        binary_search(unsorted, i, search_element, 0);
    } else {
        binary_search(&unsorted[i], length - i, search_element, start + i);
    }
}

int main() {
    //test
    int test_set[100];
    int test_set_length; 
    int test_search_element;
    int i;
    freopen("C:\\test_set\\sorted_search_input.txt", "r", stdin);
    while (scanf("%d %d", &test_set_length, &test_search_element) != EOF) {
        for (i = 0; i < test_set_length; i++) {
            scanf("%d", &test_set[i]);
        }

        i = binary_search(test_set, test_set_length, test_search_element, 0);

        printf("result:\n");
        if (i == 0) {
            printf("Can't found %d!", test_search_element);
        } else {
            printf("%d", i);
        }
        printf("\n");
    }
    return 0;
}