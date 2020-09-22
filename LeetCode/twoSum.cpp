// LeetCode# 1: Two Sum
//
// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
//
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
//
// You can return the answer in any order.
//
// Example 1:
//
// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Output: Because nums[0] + nums[1] == 9, we return [0, 1].

#include <iostream> 
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> answer;
        for(int i = 0; i < nums.size(); i++)
        {
            for(int j = i+1; j < nums.size(); j++)
            {
                if(nums[i]+nums[j] ==target)
                {
                    
                    answer.push_back(i);
                    answer.push_back(j);
                    
                }
            }
        }
        return answer;
    }
};

int main(){
    Solution *a = new Solution();
    vector<int> nums;
    nums.push_back(2);
    nums.push_back(7);
    nums.push_back(11);
    nums.push_back(15);
    vector <int> answer = a->twoSum(nums, 9);
    for(int i = 0; i < answer.size(); i++)
    {
        cout << answer[i] << endl;
    }

}