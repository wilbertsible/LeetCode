// Leetcode# 9: Palindome Number

// Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

// Example 1:

// Input: 121
// Output: true

#include <iostream>
#include<bits/stdc++.h> 
using namespace std;

class Solution{
    public:
        bool isPalindrome(int x){
            if(x * -1 > 0)
            {
                return false;
            }
            int count = 0;
            int checkLength = x;
            int powerOfTen = 1;
            while(checkLength != 0)
            {
                checkLength /= 10;
                powerOfTen *= 10;
                count++;
                
            }
            powerOfTen /= 10;
            int reverse = 0;
            int digit = 0;
            for(int i = 0; i < count /2; i++)
            {
                digit = x % 10;
                x /= 10;
                reverse = reverse * 10 + digit;
            }
            if(count%2 != 0)
            {
                x = x /10;
            }
            if(x == reverse)
            {
                return true;
            }
            else {
                return false;
            }
        }
};

int main()
{
    Solution *a = new Solution();
    int answer = a->isPalindrome(121);
    if (answer ==1){
        cout << "True" << endl;
    }
    else{
        cout << "False" << endl;
    }
}