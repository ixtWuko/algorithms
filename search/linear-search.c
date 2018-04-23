/*---- linear search 线性搜索 ----
input：
6 3 #需要排序的元素数目和需要查找的数字
2 4 5 3 6 1
output:
3 #位置

linear search: Theta(n)
-----------------------------*/

#include <stdio.h>

int linear_search(int *unsorted, int length, int search_element) {
    int i;
    int result = 0;
    for (i = 0; i < length; i++) {
        if (unsorted[i] == search_element) {
            result = i+1;
            break;
        }
    }
    return result;
}

int main() {
    //test
    int test_set[100];
    int test_set_length; 
    int test_search_element;
    int i;
    freopen("C:\\test_set\\unsorted_search_input.txt", "r", stdin);
    while (scanf("%d %d", &test_set_length, &test_search_element) != EOF) {
        for (i = 0; i < test_set_length; i++) {
            scanf("%d", &test_set[i]);
        }

        i = linear_search(test_set, test_set_length, test_search_element);

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