// Leetcode# 4: Median of Two Sorted Arrays
// Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
//
// Follow up: The overall run time complexity should be O(log (m+n)).
//
// Example 1:
//
// Input: nums1 = [1,3], nums2 = [2]
// Output: 2.00000
// Explanation: merged array = [1,2,3] and median is 2.


#include <iostream>
#include <vector>
#include <stack>
#include <iterator>
using namespace std;


class Solution{
    public :
        double findMedianSortedArrays(vector<int>&nums1, vector<int>& nums2)
        {
            
            int stack = 0;
            
            bool isOdd = false;
            
            if((nums1.size() + nums2.size()) % 2 == 1)
            {
                isOdd = true;
            }
            
            int size = (nums1.size() + nums2.size())/2;
            
            for(int i = 0; i < size; i++)
            {
                if (nums2.empty())
                {
                    stack = nums1.back();
                    nums1.pop_back();
                }
                else if (nums1.empty())
                {
                    stack = nums2.back();
                    nums2.pop_back();
                }
                else if(nums1.back() > nums2.back())
                {
                    stack = nums1.back();
                    nums1.pop_back();
                }
                
                else
                {
                    stack = nums2.back();
                    nums2.pop_back();
                }
            }
            if(isOdd)
            {
                if(nums1.empty())
                {
                    return nums2.back();
                }
                else if(nums2.empty())
                {
                    return nums1.back();
                }
                else if(nums1.back()>nums2.back() && !nums1.empty() && !nums2.empty())
                {
                    return nums1.back();
                }
               
                else
                {
                    return nums2.back();
                }
            }
            else
            {

                if(nums1.empty())
                {
                    return (double)(nums2.back() + stack) / 2.0;
                }
                else if(nums2.empty())
                {
                    return (double)(nums1.back() + stack) / 2.0;
                }
                else if(nums1.back() > nums2.back() && !nums1.empty() && !nums2.empty())
                {
                    return (double)(nums1.back() + stack) / 2.0;
                }
                else
                {
                    
                    return (double)(nums2.back() + stack) / 2.0;
                }
                
            }

        }
};

int main()
{
    Solution *a = new Solution();
    vector<int> nums1;
    vector<int> nums2;
    nums1.push_back(1);
    nums1.push_back(2);
    nums2.push_back(3);
    nums2.push_back(4);
    //nums2.push_back(4);
    cout << a->findMedianSortedArrays(nums1, nums2) << endl;

    


    
}