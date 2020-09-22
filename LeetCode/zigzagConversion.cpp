// Leetcode# 7: Zigzag Conversion

// The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may 
//want to display this pattern in a fixed font for better legibility)

// P   A   H   N
// A P L S I I G
// Y   I   R
// And then read line by line: "PAHNAPLSIIGYIR"

// Write the code that will take a string and make this conversion given a number of rows:

// string convert(string s, int numRows);
// Example 1:

// Input: s = "PAYPALISHIRING", numRows = 3
// Output: "PAHNAPLSIIGYIR"

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