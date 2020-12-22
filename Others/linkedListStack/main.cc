/*****
Write the insert and pop methods for a stack that is based on a linked list.
Assime the following is defined:
struct Node {
    Node next;
    int value;
} 
Node root;

Outline for the problem function
void insert(int value){}
int pop(){}
*****/

#include <iostream>

using namespace std;


// Create the struct
/* Note: the Node *next has to be a pointer because if you only use Node next, you are
creating a new struct Node inside which creates a new struct Node... ad infinitum(which is bad). 
If you use a pointer, it will allocate a memory space for the Node to point to later.
*/
struct Node
{
    Node *next;
    int value;
};
Node *root;

void insert(int value);
int pop();

int main()
{
    insert(0);
    insert(1);
    insert(2);
    insert(3);
    cout << root->value << " ";
    cout << root->next->value << " ";
    cout << root->next->next->value << " ";
    cout << root->next->next->next->value << " ";
    cout << endl;
    pop();
    cout << root->value << " ";
    cout << root->next->value << " ";
    cout << root->next->next->value << " ";
    cout << endl;
    

}

void insert(int value)
{
    Node *newNode = new Node();
    newNode->value = value;
    newNode->next = root;
    root = newNode;
}

int pop()
{
    Node *current = root;
    root = root->next;
    current->next = nullptr;
    int popValue = current->value;
    delete current;
    return popValue;
}

