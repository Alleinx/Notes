/* 
Let's call an array A a mountain if the following properties hold:
    1. A.length >= 3
    2. There exists some 0 < i < A.length - 1 such that 
        A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]

Given an array that is definitely a mountain, 
return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]. 

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1

Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.
*/



int peakIndexInMountainArray(int* A, int ASize) {
    int mountain_index = -1;
    int low = 0;
    int high = ASize;
    int mid;
    int temp;
    while (low <= high) {
        mid = (high - low) / 2 + low;
        temp = A[mid];
        
        if (temp > A[mid-1] && temp > A[mid+1]) {
            mountain_index = mid;
            break;
        } else if (temp > A[mid-1] && temp < A[mid+1]) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }
    
    return mountain_index;
}