
int search(int* nums, int numsSize, int target) {
    int low = 0;
    int high = numsSize;
    int mid;
    while (low <= high) {
        mid = (high - low) / 2 + low;
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] > target) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    
    return -1;
}