// LeetCode# 14: Longest Common Prefix

// Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".

// Example 1:

// Input: ["flower","flow","flight"]
// Output: "fl"

#include <iostream>
#include <vector>
using namespace std;

class Solution{
    public: 
        string longestCommonPrefix(vector<string>& strs)
        {
            if(strs.size() == 0)
            {
                return "";
            }
            string prefix = "";
            int minLength = 100000;
            for(int i= 0; i < strs.size(); i++)
            {
                if(strs[i].length() < minLength)
                {
                    minLength = strs[i].length();
                }
            }
            bool samePrefix = true;
            for(int i = 0; i < minLength; i++){
                for (int j = 0; j < strs.size()-1; j++)
                {
                    if(strs.at(j)[i] != strs.at(j+1)[i])
                    {
                        samePrefix = false;
                        return prefix;
                    }
                }
                prefix += strs.at(0)[i];
            }
            return prefix;
        }
};

int main()
{
    Solution *a = new Solution();
    vector <string> strs;
    strs.push_back("flower");
    strs.push_back("flow");
    strs.push_back("flight");
    cout << a->longestCommonPrefix(strs) << endl;
    
}