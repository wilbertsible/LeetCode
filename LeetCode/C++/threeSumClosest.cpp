// LeetCode# 16: 3Sum Closest

// Given an array nums of n integers and an integer target, find three integers in nums such that the sum is 
// closest to target. Return the sum of the three integers. You may assume that each input would have 
// exactly one solution.

// Example 1:

// Input: nums = [-1,2,1,-4], target = 1
// Output: 2
// Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

// Constraints:

// 3 <= nums.length <= 10^3
// -10^3 <= nums[i] <= 10^3
// -10^4 <= target <= 10^4



#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution{
    public: 
        int threeSumClosest(vector<int> &nums, int target)
        {
            int answer = 0;
            int difference = 0;
            int minDiff = 10000;
            sort(nums.begin(), nums.end());
            for(int i = 0; i < nums.size() - 2; i++){
                for(int k = i + 2; k < nums.size(); k++)
                {
                    for(int j = i + 1; j < k; j++)
                    {
                        int sum = nums[i] + nums[j] + nums[k];
                        difference = abs(sum - target);
                        if(difference < minDiff)
                        {
                            minDiff  = difference;
                            answer = sum;
                        }
                    }
                }
            }
            return answer;
        }
};

int main()
{
    Solution *a = new Solution();
    vector<int> input;
    input.push_back(-1);
    input.push_back(2);
    input.push_back(1);
    input.push_back(-4);
    cout << a->threeSumClosest(input, 1) << endl;
}