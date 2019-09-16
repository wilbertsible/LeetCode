/*
Write the insert and remove methods for a sorted doubly linked list.
Assume the following is defined
struct Node 
{
    Node next;
    Node prev;
    int value;
}
Node root;

Outline for the problem function
void insert(int value){}
int remove(int location = 0);
*/

#include <iostream>
using namespace std;

struct Node
{
    Node *next;
    Node *prev;
    int value;
};
Node *root;


void insert(int value);
int remove(int location = 0);

int main()
{
   insert(0);
   cout << "Added 0 :";
   cout << root->value << " "; 
   cout << endl;
   insert(1);  
   cout << "Added 1: ";
   cout << root->value << " "; 
   cout << root->next->value << " ";
   cout << endl;
   insert(3);
   cout << "Added 3: ";
   cout << root->value << " "; 
   cout << root->next->value << " ";
   cout << root->next->next->value << " ";
   cout << endl;
   insert(2);
   cout << "Added 2: ";
   cout << root->value << " "; 
   cout << root->next->value << " ";
   cout << root->next->next->value << " ";
   cout << root->next->next->next->value << " ";
   cout << endl;
   insert(4);
   cout << "Added 4: ";
   cout << root->value << " "; 
   cout << root->next->value << " ";
   cout << root->next->next->value << " ";
   cout << root->next->next->next->value << " ";
   cout << root->next->next->next->next->value << " ";
   cout << endl;
   remove(0);
   cout << "Removed 0: ";
   cout << root->value << " "; 
   cout << root->next->value << " ";
   cout << root->next->next->value << " ";
   cout << root->next->next->next->value << " ";
   cout << endl;
   remove(1);
   cout << "Removed 1: ";
   cout << root->value << " "; 
   cout << root->next->value << " ";
   cout << root->next->next->value << " ";
    cout << endl;
   remove(2);
   cout << "Removed 2: ";
   cout << root->value << " "; 
   cout << root->next->value << " ";
    cout << endl;
   remove(0);
   cout << "Removed 0: ";
   cout << root->value << " "; 
   cout << endl;
   remove(0);
}
// Insert function works by traversing the linked list, and switching the value to be inserted
// with the node value if node value is greater, then continuously doing this until the 
// end of the linked list and adding another node, then placing the biggest number in 
// the node.
void insert(int value)
{
    Node *curr = root;
    Node *newNode = new Node;
    if (curr == nullptr)
    {
        root = newNode;
        root->value = value;
        root->prev = nullptr;
        root->next = nullptr;
        return;
    }
    int tempValue = value;
    while(curr->next != nullptr)
    {
        
        int temp = tempValue;
        if(curr->value > tempValue)
        {
            tempValue = curr->value;
            curr->value = temp;
        }
        curr = curr->next;
    }
    curr->next = newNode;
    if(curr->value < tempValue)
    {
        curr->next->value = tempValue;
    }
    else
    {
        curr->next->value = curr->value;
        curr->value = tempValue;
    }
    curr->next->prev = curr;
}
// Remove function works by removing the node from the linked list.
int remove (int location)
{
    Node *curr = root;
    for(int i = 0; i < location; i++)
    {
        curr = curr->next;
    }
    if(curr->next != nullptr)
    {
        curr->next->prev = curr->prev;
    }
    if (curr->prev != nullptr)
    {
        curr->prev->next = curr->next;
    }
    if(curr == root && curr->next != nullptr)
    {
        root = curr->next;
    }
    else if(curr == root && curr->next == nullptr)
    {
        root = nullptr;
    }
    curr->prev = nullptr;
    curr->next = nullptr;
    delete curr;
}
