// Leetcode# 7: Reverse Integer

// Given a 32-bit signed integer, reverse digits of an integer.

// Example 1:

// Input: 123
// Output: 321


#include <iostream>
#include<bits/stdc++.h> 
using namespace std;

class Solution{
    public:
        int reverseString(int x){
            int digit = 0;
            int answer = 0;
            while (x != 0)
            {
                digit = x % 10;
                x/=10;
                if(answer > INT_MAX/10 || answer == INT_MAX/ 10 && digit >= 7)
                {
                    cout << "gets to int max" << endl;
                    return 0;
                }
                if(answer < INT_MIN/10 || answer == INT_MIN/ 10 && digit >= 8)
                {
                    cout << "gets to int min" << endl;
                    return 0;
                }
                answer =  answer * 10 + digit;
            }

        }
};

int main()
{
    Solution *a = new Solution();
    cout << a->reverseString(-1463847412) << endl;
}