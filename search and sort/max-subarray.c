/*---- max subarray ----
input:
16 #数组的长度
13 -3 -25 20 -3 -16 -23 18 20 -7 12 -5 -22 15 -4 7
output:
from 8 to 11 is the max subarray

使用暴力的算法来求最大子数组：Theta(n^2)
使用分治的算法来求最大子数组：Theta(n log n)
----------------------*/

#include <stdio.h>

void *max_subarray(int *array, int start_index, int end_index, int *result) {
    int middle_index, left_index, right_index;
    int middle_sum, left_sum, right_sum, sum;
    int left_result[3]; 
    int right_result[3];
    int i;
    if (start_index == end_index) {
        result[0] = start_index;
        result[1] = end_index;
        result[2] = array[start_index];
    } else {
        //左部分为[start : middle], 右部分为[middle+1 : end]
        middle_index = (end_index - start_index) / 2 + start_index;
        
        //跨中点的
        sum = array[middle_index];
        left_sum = sum;
        left_index = middle_index;
        for (i = middle_index - 1; i >= start_index; i--) {
            sum += array[i];
            if (sum >= left_sum) {
                left_sum = sum;
                left_index = i;
            }
        }
        sum = array[middle_index + 1];
        right_sum = sum;
        right_index = middle_index + 1;
        for (i = middle_index + 2; i <= end_index; i++) {
            sum += array[i];
            if (sum >= right_sum) {
                right_sum = sum;
                right_index = i;
            }
        }
        middle_sum = left_sum + right_sum;

        //左右两个
        max_subarray(array, start_index, middle_index, left_result);
        max_subarray(array, middle_index+1, end_index, right_result);

        //判断大小，指定结果
        if (middle_sum > left_result[2] && middle_sum > right_result[2]) {
            result[0] = left_index;
            result[1] = right_index;
            result[2] = middle_sum;
        } else if (left_result[2] >= right_result[2]) {
            result[0] = left_result[0];
            result[1] = left_result[1];
            result[2] = left_result[2];
        } else {
            result[0] = right_result[0];
            result[1] = right_result[1];
            result[2] = right_result[2];
        }
    }
}

int main() {
    int test_set[1000];
    int test_set_length;
    int i;
    int result[3];
    freopen("C:\\test_set\\max_subarray.txt", "r", stdin);
    while (scanf("%d", &test_set_length) != EOF) {
        for (i = 0; i < test_set_length; i++) {
            scanf("%d", &test_set[i]);
        }

        max_subarray(test_set, 0, test_set_length-1, result);

        printf("from %d to %d is the max subarray\n", result[0]+1, result[1]+1);
    }
    return 0;
}