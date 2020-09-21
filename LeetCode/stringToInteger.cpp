#include <iostream>
using namespace std;

class Solution{
    public:
        int myAtoi(string str)
        {
            int integer = 0;
            bool negative = false;
            int counter = 0;
            while(str[counter] == 32)
            {
                counter++;     
            }
            if(str[counter] != 43 && str[counter] != 45 && !(str[counter] > 47 && str[counter] < 58) || (str[counter] == 45 && !(str[counter + 1] > 47 && str[counter + 1] < 58)))
            {
                return integer;
            }
            else if(str[counter] == 43)
            {
                counter++;
            }
            else if(str[counter] == 45)
            {
                negative = true;
                counter++;
            }
            while(str[counter] > 47 && str[counter] < 58)
            {
                int number = 0;
                switch(str[counter]){
                    case 48:
                    number = 0;
                    break;
                    case 49:
                    number = 1;
                    break;
                    case 50:
                    number = 2;
                    break;
                    case 51:
                    number = 3;
                    break;
                    case 52:
                    number = 4;
                    break;
                    case 53:
                    number = 5;
                    break;
                    case 54:
                    number = 6;
                    break;
                    case 55:
                    number = 7;
                    break;
                    case 56:
                    number = 8;
                    break;
                    case 57:
                    number = 9;
                    break;
                }
                cout << integer << endl;
                if(negative && ((integer == 214748364 && number > 7) || integer > 214748364))
                {
                    return -2147483648;
                }
                else if(!negative &&(integer >= 214748364 && number >= 7) || integer > 214748364)
                {
                    return 2147483647;
                }
                else{
                    integer *= 10;
                    integer += number;
                    counter++;
                }
            }
            if(negative)
            {
                integer *= -1;
            }
            return integer;
        }
};


int main()
{
    Solution *a = new Solution();
    cout << a->myAtoi("-2147483648") << endl;
}