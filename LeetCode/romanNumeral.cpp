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
    string roman =  a->intToRoman(1994);
    cout << roman << endl;
    int integer = a->romanToInt(roman);
    cout << integer << endl;

}