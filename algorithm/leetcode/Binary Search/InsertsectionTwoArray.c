/**
 * Given two arrays, write a function to compute their intersection
 * Example:
 * nums1 = [1,2,2,1]
 * nums2 = [2,2]
 * Note :Each element in the result must be unique
 * The result can be in any order;
 */
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdio.h>

#define MIN(a,b) ((a)<=(b)?(a):(b))
int* intersection(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    if(nums1Size <=0 || nums2Size <= 0)return NULL;   //if at least one of them are empty set, the intersection will be emtey set;
    sort(nums1, 0, nums1Size-1);
    sort(nums2, 0, nums2Size-1);
    int size = MIN(nums1Size, nums2Size);
    int* arr = (int*)malloc(sizeof(int)*size); //the size of the result will at most be size;
    int top = -1;
    int p1=0, p2=0;
    while(p1<nums1Size && p2<nums2Size)
    {
        if(nums1[p1] > nums2[p2]) p2++;
        else if(nums1[p1] < nums2[p2]) p1++;
        else //only collect the equal one;
        {
            if(top==-1 || arr[top]!=nums1[p1])  //avoid duplicates;
                arr[++top] = nums1[p1];
            p1++, p2++;
        }
    }
    *returnSize = top+1;
    return arr;
}
//[1,2,3] [5,4];
//[2,3,4,2,3,4] [2,3]
//O( M x N ):
/**
 * choose the smaller size: and nested loop;
 * if nums1[index] == nums2[i] continue;
 * else set it to 0;error what if set contain 0?
 * [2,2,2];
 */