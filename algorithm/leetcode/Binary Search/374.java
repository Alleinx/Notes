/* The guess API is defined in the parent class GuessGame.
   @param num, your guess
   @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
      int guess(int num); */

      public class Solution extends GuessGame {
        public int guessNumber(int n) {
            int low = 1;
            int high = n;
            int mid;
            int guessResult;
            while (low <= high) {
                mid = (high - low) / 2 + low;
                guessResult = guess(mid);
                if (guessResult == 0) {
                    return mid;
                } else if (guessResult > 0) {
                    low = mid + 1;
                } else {
                    high = mid -1;
                }
            }
            
            return -1;
        }
    }