/**
 * letters = ["c", "f", "j"]
 * target = "a"
 * Output: "c"
 * */


char nextGreatestLetter(char* letters, int lettersSize, char target) {
    int low = 0;
    int high = lettersSize;
    int mid;
    while (low <= high) {
        
        if (letters[mid] <= target) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }

    /* If target is larger than all elements in the array, return letters[0] */
    return letters[low % lettersSize];
}