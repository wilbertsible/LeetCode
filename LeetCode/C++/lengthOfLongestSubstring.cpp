//Leetcode# 3: Longest Substring without Repeating Characters

// Given a string s, find the length of the longest substring without repeating characters.

// Example 1:

// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.

#include <iostream> 
using namespace std;


//O(N^2) Solution
class Solution{
    public:
        int lengthOfLongestSubstring(string s)
        {
            int length = 0;
            string substring = "";
            for(int i = 0; i < s.length(); i++)
            {
                int substringCount = 0;
                while(substringCount < substring.length() && s[i] != substring[substringCount])
                {
                    substringCount++;
                }
                if(s[i] == substring[substringCount])
                {
                    if(length < substring.length())
                    {
                        length = substring.length();
                    }
                    i = i - substring.length();
                    substring = "";
                    substringCount  = 0;
                }
                else{
                    substring = substring + s[i];
                }
                if(length < substring.length())
                    {
                        length = substring.length();
                    }

            }
            return length;
        }
};

int main()
{   
    Solution *a = new Solution();
    cout << a->lengthOfLongestSubstring("dvdf") << endl;
}