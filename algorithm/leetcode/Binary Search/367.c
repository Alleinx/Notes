/** 
 * O(logn)
 */

bool isPerfectSquare(int num) {
    if (num < 1) return false;

    /* use 8bytes to prevent overflow */

    long long cur = 1;
    long long limit = num; 
    long long check; 
    long long mid;
    
    while (cur <= limit) {
        mid = (limit - cur) / 2 + cur;
        check = mid * mid;
        if (check == num) {
            return true;
        } else if (check < num){
            cur = mid + 1;
        } else {
            limit = mid - 1;
        }
    }
    
    return false;
}


/** 
 * Newton Method to calculate the square root or num
 * O(logn)
 */
bool isPerfectSquare(int num) {
    long x = num;
    while (x * x > num) {
        x = (x + num / x) >> 1;
    }
    
    return x * x == num;
}