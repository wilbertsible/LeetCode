#include <iostream>
#include <cmath>
#include <string.h>

using namespace std;

class Solution{
    public:
        string longestPalindrome(string s)
        {
            string cur = "";
            string longest = "";
            for(int i = 0; i < s.length(); i ++)
            {
                cur = cur + s[i];
                for(int j = i; j < s.length(); j++)
                {
                    if(isPalindrome(cur) && cur.length() > longest.length())
                    {
                        longest = cur;
                    }
                    cur = cur + s[j+1];
                }
                cur = "";
            }
            return longest;
        }
        bool isPalindrome(string s)
        {
            for(int i = 0; i < s.length() / 2; i++)
            {
                if(s[i] != s[s.length() - i - 1])
                {
                    return false;
                }
            }
            return true;
        }
};


// Answer copied from https://www.youtube.com/watch?v=l-XCWjps-UQ&t=988s
class Manacher{
    public:
        string manacherSolution(string s)
        {
            string newString = getModifiedString(s);
            int *P = new int[newString.length()];
            for(int i = 0; i <newString.length(); i++)
            {
                P[i] = 0;
            }
            int center = 0;
            int rightBoundary = 0;
            for(int i = 0; i < newString.length(); i++)
            {
                int index_mirror = center - (i - center);
                if(i < rightBoundary){
                    P[i] = min(rightBoundary-i, P[index_mirror]);
                }
                int right = i + (P[i] + 1);
                int left = i - (P[i] + 1);
                while(right < newString.length()  && left >=0 && newString[left] == newString[right])
                {
                    P[i]++;
                    right++;
                    left--;
                }
                if(i+P[i] > rightBoundary)
                {
                    center = i;
                    rightBoundary = i + P[i];
                }
            }
            int max = 0;
            int index = 0;
            for(int i = 0; i < newString.length(); i++){
                if(P[i] > max){
                    max = P[i];
                    index = i;
                }
            }
            string answer = newString.substr(index-max, (2*max) + 1);
            string finalAnswer = "";
            for(int i = 1; i < answer.length() - 1; i= i + 2)
            {
                finalAnswer += answer[i];
            }
            return finalAnswer;
        }
        string getModifiedString(string s){
            string newString = "";
            for(int i = 0; i < s.length(); i++){
                newString += "#";
                newString +=s[i];
            }
            newString += "#";
            return newString;

        }

};

int main()
{
    string str1 = "abcba";
    string str2 = "reracecar";
    string str3 = "zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir";
    
    /*Solution *a = new Solution();
    cout << a->longestPalindrome(str1) << endl;
    cout << a->longestPalindrome(str2) << endl;
    cout << a->longestPalindrome(str3) << endl;
    */
    Manacher *m = new Manacher();
    cout << m->manacherSolution(str1) << endl;
    cout << m->manacherSolution(str2) << endl;
    cout << m->manacherSolution(str3) << endl;
}