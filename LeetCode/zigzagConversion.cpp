//Leetcode # 7 Zigzag Conversion

#include <iostream>
#include <queue>
using namespace std;


class Solution
{
    public:
        string convert(string s, int numRows)
        {
            if(numRows < 2)
            {
                return s;
            }
            queue<char> queueArray[numRows];
            for (int i = 0; i < numRows; i++)
            {
                queue <char> q;
                queueArray[i] = q;
            }
            int counter = 0;
            int forward = true;
            for(int i = 0; i < s.length(); i++)
            {   
                queueArray[counter].push(s[i]);
                if(counter >= numRows-1)
                {
                    forward = false;
                }
                if(counter <= 0)
                {
                    forward = true;
                }
                if(forward)
                {
                    counter++;
                }
                else
                {
                    counter--;
                }
            }
            
            string answer = "";
            for(int i =0; i < numRows; i++){
                for(int j = 0; queueArray[i].size(); j++)
                {
                    answer += queueArray[i].front();
                    queueArray[i].pop();
                }
            }
            return answer;
        }
};

int main()
{
    Solution *a = new Solution();
    cout << a->convert("AB", 1) << endl;
}