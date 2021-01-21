# LeetCode # 19 Merge k Sorted Lists

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
 

# Constraints:

# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length won't exceed 10^4.

from typing import List

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) ->ListNode:
        if len(lists) < 1:
            return None
        while len(lists) > 1:
            tempList = []
            for i in range(0, len(lists) - 1, 2):
                out = self.mergeTwoLists(lists[i], lists[i+1])
                tempList.append(out)
                if len(lists) % 2 == 1:
                    tempList.append(lists[len(lists) - 1])
            lists = tempList
        return lists[0]

    def mergeTwoLists(self, list1:ListNode, list2:ListNode) ->ListNode:
        if list1 == None and list2 == None:
            return None
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1.val <= list2.val:
            curr = list1
            list1 = list1.next
            curr.next = None
            head = curr
        else:
            curr = list2
            list2 = list2.next
            curr.next = None
            head = curr
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
                curr.next = None
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
                curr.next = None
        if list1 == None and list2 != None:
            curr.next = list2
        elif list1 != None and list2 == None:
            curr.next = list1
        return head



s = Solution()


a = ListNode(-1)
b = ListNode(5)
c = ListNode(11)
a.next = b
b.next = c

d = ListNode(1)
e = ListNode(3)
f = ListNode(4)
d.next = e
e.next = f

g = ListNode(6)
h = ListNode(10)
g.next = h

lists = [None, a, None, g]

mergeList = s.mergeKLists(lists)

print(mergeList.val)
print(mergeList.next.val)
print(mergeList.next.next.val)
print(mergeList.next.next.next.val)
print(mergeList.next.next.next.next.val)
print(mergeList.next.next.next.next.next.val)
print(mergeList.next.next.next.next.next.next.val)
print(mergeList.next.next.next.next.next.next.next.val)