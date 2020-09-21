//Leetcode # 3

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