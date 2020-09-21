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
    g.push_back(1);
    // g.push_back(6);
    // g.push_back(2);
    // g.push_back(5);
    // g.push_back(4);
    // g.push_back(8);
    // g.push_back(3);
    // g.push_back(7);
    cout << a->maxArea(g) << endl;

}