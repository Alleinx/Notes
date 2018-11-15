/**
 * Current Algorithm is O(nlogn) complexity.
 * If the elements are sorted, could run in O(n).
 * Could use hashTable to run in O(n).
 *  
 * O(n) with hashTable:
 * push all elements in larger Array of nums1 and nums2 into a hashTable
 * use Array[i]'s value as key and total amount of occurance as value
 * that means, if Array[i] is not in hashTable, put it into hashTable and set its value to 1
 * if Array[i] is already in the hashTable, update the value in hashtable to i + 1
 * then loop through the smaller Array to find intersection.
 * If B[i] is in hashTable and it's value is larger than 1, 
 * then add B[i] to result[] and update the value of Array[i] to i - 1;
 * 
 */
class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        // freq count for nums1
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        
        int min = (nums1.length > nums2.length) ? nums2.length : nums1.length;
        int[] result= new int[min];
        int index = 0;
        int l_nums1 = nums1.length;
        int l_nums2 = nums2.length;
        for (int i = 0, j = 0; i < l_nums1 && j < l_nums2; ) {
            if (nums1[i] == nums2[j]) {
                result[index] = nums1[i];
                index++;
                i++;
                j++;
            } else if (nums1[i] > nums2[j]) {
                j++;
            } else {
                i++;
            }
        }
        
        return Arrays.copyOf(result, index);
    }
}

