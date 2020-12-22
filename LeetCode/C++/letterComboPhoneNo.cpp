// LeetCode# 17: Letter Combinations of a Phone Number

// Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the 
// number could represent.

// A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not 
// map to any letters.


#include <iostream>
#include <vector>
using namespace std;

class Solution{
    public: 
        vector<string> letterCombinations(string digits)
        {
            vector<string> answer;
            int combo[digits.size()];
            int count[digits.size()];
            int permutations = 1;
            for(int i = 0; i < digits.size(); i++)
            {
                combo[i] = 0;
                if(digit[i] == '2' || digit[i] == '3' || digit[i] == '4' || digit[i] == '5' || digit[i] == '6' || digit[i] == '8')
                {
                    count[i] = 3;
                    permutations *= 3;
                }
                else
                {
                    count[i] = 4;
                    permutations *= 4
                }
            }
            for(int i = 0; i < digits.size(); i--)
            {
                for(int j = 0; j < count[i]; j++;)
                {
                    if(combo[i] == 0 && digit[])
                }
            }
            return answer;
        }
};

int main()
{
    Solution *a = new Solution();
    a->letterCombinations("237");
}