// LeetCode# 15: 3Sum

// Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all 
// unique triplets in the array which gives the sum of zero.

// Notice that the solution set must not contain duplicate triplets.

 

// Example 1:

// Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]


#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
using namespace std; 

class Solution{
    public:
        vector<vector<int>> threeSum(vector<int> &nums)
        {
            vector <vector<int>> answer;
            sort(nums.begin(), nums.end());
            if(nums.size() < 3)
            {
                return answer;
            }
            int start = 0; 
            int mid =  start + 1; 
            int end = nums.size() - 1;
            int sum = 0;
            while (start < nums.size() - 2)
            {
                sum = nums[start] + nums[mid] + nums[end];
                if(sum < 0 && mid  < end)
                {
                    mid++;
                    while(mid  < end && nums[mid] == nums[mid-1])
                    {
                        mid++;
                    }
                }
                else if (mid < end && start < mid && sum == 0)
                {
                    vector<int> group;
                    group.push_back(nums[start]);
                    group.push_back(nums[mid]);
                    group.push_back(nums[end]);
                    answer.push_back(group);
                    mid++;
                    while(mid < end && nums[mid] == nums[mid-1])
                    {
                        mid++;
                    }
                }
                else if(mid  < end && sum > 0)
                {
                    end--;
                    while(mid  < end && nums[end] == nums[end+1])
                    {
                        end --;
                    }
                }
                else if(start > mid || mid >= end)
                {
                    start++;
                    while(start + 1 < end && nums[start] == nums[start-1])
                    {
                        start++;
                    }
                    mid = start + 1;
                    end = nums.size() - 1;
                }
            }
            return answer;
        }
        
};

int main()
{
    Solution *a = new Solution();
    vector <int> input;
    // input.push_back(-1);
    // input.push_back(0);
    // input.push_back(1);
    // input.push_back(2);
    // input.push_back(-1);
    // input.push_back(-4);

    // input.push_back(0);
    // input.push_back(0);
    // input.push_back(0);
    // input.push_back(0);

    input.push_back(-2);
    input.push_back(0);
    input.push_back(1);
    input.push_back(1);
    input.push_back(2);

    // input.push_back(-1);
    // input.push_back(0);
    // input.push_back(1);
    // input.push_back(2);
    // input.push_back(-1);
    // input.push_back(-4);
    // input.push_back(-2);
    // input.push_back(-3);
    // input.push_back(3);
    // input.push_back(0);
    // input.push_back(4);
    
    vector<vector<int>> answer = a->threeSum(input);
    for(int i = 0; i < answer.size(); i++)
    {
        for(int j = 0; j < 3; j++)
        {
            cout << answer[i][j] << ", ";
        }
        cout << endl;
    }
}