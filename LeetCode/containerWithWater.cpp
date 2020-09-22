// LeetCode# 11: Container With Most Water

// Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical 
// lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together 
// with x-axis forms a container, such that the container contains the most water.

// Note: You may not slant the container and n is at least 2.

// Example:

// Input: [1,8,6,2,5,4,8,3,7]
// Output: 49

#include <iostream>
#include <vector>
using namespace std;

class Solution
{
    public: 
        int maxArea(vector<int> &height)
        {
            int max = 0;
            int start = 0;
            int end = height.size() - 1;
            int area = 0;
            while (start != end)
            {
                if (height[start] > height[end])
                {
                    area = (end - start) * height[end];
                    end--;
                }
                else
                {
                    area = (end-start) * height[start];
                    start++;
                }
                if(area > max)
                {
                    max = area;
                }
            }
            return max;
        }
};

int main()
{
    Solution *a = new Solution();
    vector<int> g;
    g.push_back(1);
    g.push_back(8);
    g.push_back(6);
    g.push_back(2);
    g.push_back(5);
    g.push_back(4);
    g.push_back(8);
    g.push_back(3);
    g.push_back(7);
    cout << a->maxArea(g) << endl;

}