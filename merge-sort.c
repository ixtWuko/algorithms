/*---- merge sort 归并排序 ----
input：
6 #需要排序的元素数目
5 2 4 6 1 3
output:
1 2 3 4 5 6

merge sort: Theta(n log n)
-----------------------------*/

#include <stdio.h>

int *merge_sort(int *unsorted, int length) {
    int left_length, right_length;
    int left[100], right[100];
    int *sorted_left, *sorted_right;
    int l,r,i;
    if (length == 0) {
        return NULL;
    } else if (length == 1) {
        return unsorted;
    } else {
        //分开
        left_length = length / 2;
        right_length = length - left_length;
        for (i = 0; i < left_length; i++) {
            left[i] = unsorted[i];
        }
        for (i = 0; i < right_length; i++) {
            right[i] = unsorted[i+left_length];
        }
        //排序
        sorted_left = merge_sort(left, left_length);
        sorted_right = merge_sort(right, right_length);
        //合并
        l = 0, r = 0;
        while (l < left_length && r < right_length) {
            if (sorted_left[l] < sorted_right[r]) {
                unsorted[l+r] = sorted_left[l];
                l++;
            } else {
                unsorted[l+r] = sorted_right[r];
                r++;
            }
        }
        //此时还有一些元素在左右两个序列之一中
        while (l < left_length) {
            unsorted[l+r] = sorted_left[l];
            l++;
        }
        while (r < right_length) {
            unsorted[l+r] = sorted_right[r];
            r++;
        }
        return unsorted;
    }
}

int main() {
    //test
    int test_set[100];
    int test_set_length; 
    int *result;
    int i;
	printf("merge sort\n");
    freopen("C:\\test_set\\unsorted_input.txt", "r", stdin);
    while (scanf("%d", &test_set_length) != EOF) {
        for (i = 0; i < test_set_length; i++) {
            scanf("%d", &test_set[i]);
        }

        result = merge_sort(test_set, test_set_length);
    
        printf("result:\n");
        for (i = 0; i < test_set_length; i++) {
            printf("%d ", result[i]);
        }
        printf("\n");
    }
    return 0;
}