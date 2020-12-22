#include <iostream>
using namespace std;


class Solution
{
    public: 
        void travel(int targetX, int targetY)
        {
            explore(targetX, targetY, 0, 0, "moves:");
        }
        void explore(int targetX, int targetY, int currX, int currY, string path)
        {
            if(currX == targetX && currY == targetY)
            {
                cout << path << endl;
            }
            else if (currX <= targetX && currY  <= targetY)
            {
                explore(targetX, targetY, currX, currY + 1, path+ " N");
                explore(targetX, targetY, currX + 1, currY, path+ " E");
                explore(targetX, targetY, currX + 1, currY + 1, path+ " NE");
            }
            
        }
};

int main()
{
    Solution *a = new Solution();
    a->travel(1,2);
}