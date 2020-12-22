/*
Write a function ticketValue that takes in an int array representing the amount 
of tickets each ticket station has and takes in an int of the number of tickets 
that need to be sold. The function will return an int representing the optimal 
amount of money that can be made by selling the tickets. 

The amount of money made from selling a ticket is equal to the amount of tickets left. 
For example if the ticket station has 15 tickets then selling one ticket will net 15 dollars 
and selling two tickets will net 29 dollars. Can be solved in O(n log k) where 
n is the length of the array and k is the number of tickets to be sold.

An example looks like:
([13, 12, 15, 20], 5) -> 20 + 19 + 18 + 17 + 16 =  90

int ticketValue(int[] ticketStations, int ticketsToSell) {}
*/


#include <iostream>

using namespace std;


int ticketValue(int ticketStations[], int ticketsToSell, int arraySize);
void percolateDown(int ticketStations[], int nodeToPercolate, int size);

int main()
{
    int arr[] = {1, 2, 3, 4, 5, 6, 7};
    int size = sizeof(arr)/sizeof(arr[0]);
    int total = ticketValue(arr,5,size);
    
    cout << "Total is " << total << endl;
    
}

int ticketValue(int ticketStations[], int ticketsToSell, int size)
{
    // Construct a  binary max heap array
    for (int i = size/2 - 1; i >= 0; i--)
    {
        percolateDown(ticketStations, i, size);
    } 
    for(int i =0; i < size; i++)
    {
        cout << ticketStations[i] << " ";
    }
    cout << endl;
    int total = 0;
    // Solving for the tickets
    for(int i = 0; i < ticketsToSell; i++)
    {
        total += ticketStations[0];
        ticketStations[0]--;
        percolateDown(ticketStations, 0, size);
    }
    return total;
}

void percolateDown(int ticketStations[], int nodeToPercolate, int size)
{
       
    while(nodeToPercolate < size - 1)
    {
        int child1 = 2 * nodeToPercolate + 1;
        int child2 = child1 + 1;
        int largerChild = child1;
        if(child2 < size && ticketStations[child2] > ticketStations[child1])
        {
            largerChild = child2;
        }
        if(child1 < size && ticketStations[largerChild] > ticketStations[nodeToPercolate])
        {
            
            int temp = ticketStations[nodeToPercolate];
            ticketStations[nodeToPercolate] = ticketStations[largerChild];
            ticketStations[largerChild] = temp;
            nodeToPercolate = largerChild;
        }
        else
        {
            nodeToPercolate = size;
        }
       
    }
}


