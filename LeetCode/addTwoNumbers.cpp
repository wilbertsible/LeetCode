//Leetcode# 2: Add Two Numbers
// You are given two non-empty linked lists representing two non-negative integers. The digits are stored in 
// reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
//
// You may assume the two numbers do not contain any leading zero, except the number 0 itself.
//
// Example:
//
// Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
// Output: 7 -> 0 -> 8
// Explanation: 342 + 465 = 807.


#include <iostream>
using namespace std;


struct ListNode{
    int val;
    ListNode *next;
    ListNode(int x): val(x), next(NULL) {}
};
class Solution{
    public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
    {
        ListNode *answerNode;
        ListNode *head;
        ListNode *nodeptr1 = l1;
        ListNode *nodeptr2 = l2;
        int carry = 0;
        int sum = nodeptr1->val + nodeptr2->val + carry;
        int digit;
        if (sum >= 10)
        {
            carry = sum / 10;
            digit = sum % 10;
        }
        else
        {
            digit = sum;
        }

        answerNode = new ListNode(digit);
        head = answerNode;
        while(nodeptr1->next != NULL && nodeptr2->next != NULL)
        {
            nodeptr1 = nodeptr1->next;
            nodeptr2 = nodeptr2->next;
            sum = nodeptr1->val + nodeptr2->val + carry;
            if (sum >= 10)
            {
            carry = sum / 10;
            digit = sum % 10;
            }
            else
            {
                digit = sum;
                carry = 0;
            }
        ListNode *newNode = new ListNode(digit);
        answerNode->next = newNode;
        answerNode = answerNode->next;
        }
        while(nodeptr1->next != NULL)
        {
            nodeptr1 = nodeptr1->next;
            sum = nodeptr1->val + carry;
            if (sum >= 10)
            {
            carry = sum / 10;
            digit = sum % 10;
            }
            else
            {
                digit = sum;
                carry = 0;
            }
            ListNode *newNode = new ListNode(digit);
            answerNode->next = newNode;
            answerNode = answerNode->next;
        }
        while(nodeptr2->next != NULL)
        {
            nodeptr2 = nodeptr2->next;
            sum = nodeptr2->val + carry;
            if (sum >= 10)
            {
            carry = sum / 10;
            digit = sum % 10;
            }
            else
            {
                digit = sum;
                carry = 0;
            }
            ListNode *newNode = new ListNode(digit);
            answerNode->next = newNode;
            answerNode = answerNode->next;
        }
        ListNode *answerptr = head;
        if(carry > 0)
        {
            ListNode *newNode = new ListNode(carry);
            answerNode->next = newNode;
            answerNode = answerNode->next;
        }
       
    }

};

int main()
{
    ListNode* l1 = new ListNode(2);
    l1->next = new ListNode(4);
    l1->next->next = new ListNode(3);
    
    ListNode* l2 = new ListNode(5);
    l2->next = new ListNode(6);
    l2->next->next = new ListNode(4);


    Solution *a = new Solution();
    ListNode *head = a->addTwoNumbers(l1,l2);
    while(head != NULL)
    {
        cout << head->val << endl; 
        head = head->next;
    }

}
