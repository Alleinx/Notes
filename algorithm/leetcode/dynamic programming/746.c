/** 
 * On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
 * Once you pay the cost, you can either climb one or two steps.
 * You need to find minimum cost to reach the top of the floor, 
 * and you can either start from the step with index 0, or the step with index 1.
 * 
 * Example 1:
 * Input: cost = [10, 15, 20]
 * Output: 15
 * Explanation: Cheapest is start on cost[1], pay that cost and go to the top. 
 */


int minCostClimbingStairs(int* cost, int costSize) {
    int stars[costSize+1];
    stars[0] = cost[0]; //go up 1
    stars[1] = cost[1]; //go up 2
    
    for (int i = 2; i < costSize; i++) {
        stars[i] = (stars[i-1] <= stars[i-2]) ? stars[i-1] + cost[i] : stars[i-2] + cost[i];
    }
    
    return stars[costSize - 1] < stars[costSize - 2] ? stars[costSize -1] : stars[costSize - 2];
}


