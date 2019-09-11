/* 
Problem: Given a string of Rs and Ws, find the smallest
number of steps needed to clump all the Rs together.
*/

#include <iostream>
#include <cstring>
#include <vector>


using namespace std;

void usage (const char* args)
{
    cerr << "Usage: " << args << " [string]" << endl;
    exit(EXIT_FAILURE);
}

int main(int argc, char *argv[])
{
    if (argc > 2 || argc <= 1)
    {
        usage(argv[0]);
    }
    char *letters = argv[1];
    cout << "The string is: " << letters << endl;
    
    //Cut the Ws in front and at the back
    int start = 0;
    while (letters[start] == 'W')
    {
        start++;
    }
    int end = strlen(letters);
    
    while(letters[end-1] == 'W')
    {
        end--;
    }
    bool prevIsR = true; // Is the previous letter R
    int counter = 0;
    vector <int> v1;
    for (int i= start; i < end;i++)
    {
        if(letters[i] == 'R') // Counts R
        {
            if(prevIsR)
            {
                counter++;
            }
            else
            {
                v1.push_back(counter);
                counter = 0;
                prevIsR = true;
                counter++;
            }
        }
        else // Counts W
        {
            if(prevIsR)
            {
                v1.push_back(counter);
                counter = 0;
                prevIsR= false;
                counter++;
            }
            else 
            {
                counter++;
            }
        }
        
    }
    v1.push_back(counter);
    for(int i = 0; i < v1.size(); i++)
    {
        cout << v1.at(i) << " ";
        
    }
    cout << endl;
    int lowest = 99999;
    int total = 0;
    for(int i = 0; i < v1.size(); i = i+2)
    {
        cout << "i is " << i << ":" << endl;
        int sumLeft = 0;
        int totalLeft = 0;
        for(int j = i; j > 0; j=j-2)
        {   
            cout << "j1 is " << j << ":" << endl;
            sumLeft = sumLeft + v1.at(j-1);
            totalLeft = totalLeft + (sumLeft * v1.at(j-2));
            cout << "sumLeft is " << sumLeft << endl;
            cout << "totalLeft is " << totalLeft << endl;
        }
        
        int sumRight = 0;
        int totalRight = 0;
        for(int j = i; j < v1.size()-1; j = j+2)
        {
             cout << "j2 is " << j << ":" << endl;
            sumRight = sumRight + v1.at(j+1);
            totalRight = totalRight + (sumRight * v1.at(j+2));
            cout << "sumRight is " << sumRight << endl;
            cout << "totalRight is " << totalRight << endl;
        }
        int total = totalLeft + totalRight;
        cout << "TOTAL is " << total << endl;
        cout << endl;
        if(total < lowest)
        {
            lowest = total;
        }
        
    }
    cout << "The answer is " << lowest << endl;
    
}