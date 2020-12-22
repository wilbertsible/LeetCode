// LeetCode# 12: Integer to Roman
// Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

// Symbol       Value
// I             1
// V             5
// X             10
// L             50
// C             100
// D             500
// M             1000

// For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, 
// XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

// Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is 
// not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it 
// making four. The same principle applies to the number nine, which is written as IX. There are six 
// instances where subtraction is used:

// I can be placed before V (5) and X (10) to make 4 and 9. 
// X can be placed before L (50) and C (100) to make 40 and 90. 
// C can be placed before D (500) and M (1000) to make 400 and 900.
// Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

// Example 1:

// Input: 3
// Output: "III"

// LeetCode# 13 Roman to Integer

// Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

// For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, 
// XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

// Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is 
// not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it 
// making four. The same principle applies to the number nine, which is written as IX. There are six 
// instances where subtraction is used:

// I can be placed before V (5) and X (10) to make 4 and 9. 
// X can be placed before L (50) and C (100) to make 40 and 90. 
// C can be placed before D (500) and M (1000) to make 400 and 900.

// Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

// Example 1:

// Input: "III"
// Output: 3



#include <iostream> 
using namespace std;

class Solution{
    public:
        string intToRoman(int num)
        {
            int remainder = 0;
            int thousands = num / 1000;
            remainder = num % 1000;
            int hundreds = remainder / 100;
            remainder = num % 100;
            int tens = remainder / 10;
            remainder = num % 10;
            int ones = remainder;
            
            string thousandTable[4] = {"", "M", "MM", "MMM"};
            string hundredTable[10] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
            string tensTable[10] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
            string onesTable[10] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
            
            return thousandTable[thousands] + hundredTable[hundreds] + tensTable[tens] + onesTable[ones];
        }
        int romanToInt(string s)
        {
            int answer = 0;
            int integer[s.length()];
            for(int i =0; i < s.length(); i++)
            {
                if(s[i] == 'M')
                {
                    integer[i] = 1000;
                }
                else if(s[i] == 'D')
                {
                    integer[i] =  500;
                }
                else if(s[i] == 'C')
                {
                    integer[i] =100;
                }
                else if(s[i] == 'L')
                {
                    integer[i] = 50;
                }
                else if(s[i] == 'X')
                {
                    integer[i] = 10;
                }
                 else if(s[i] == 'V')
                {
                    integer[i] = 5;
                }
                else if(s[i] == 'I')
                {
                    integer[i] = 1;
                }
            }
            for (int i = 0; i < s.length()-1; i++)
            {
                if(integer[i] < integer[i+1])
                {
                    integer[i + 1] -= integer[i];
                    integer[i] = 0;
                }
            }
            for (int i = 0; i < s.length(); i++)
            {
                answer += integer[i];
            }
            return answer;
        }
};

int main()
{
    Solution *a = new Solution();
    string roman =  a->intToRoman(2020);
    cout << roman << endl;
    int integer = a->romanToInt(roman);
    cout << integer << endl;

}