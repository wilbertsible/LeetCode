# LeetCode February Coding Challenge 2021 #8: Peeking Iterator
# Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

# Example:

# Assume that the iterator is initialized to the beginning of the list: [1,2,3].

# Call next() gets you 1, the first element in the list.
# Now you call peek() and it returns 2, the next element. Calling next() after that still return 2. 
# You call next() the final time and it returns 3, the last element. 
# Calling hasNext() after that should return false.
# Follow up: How would you extend your design to be generic and work with all types, not just integer?

import copy

class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.curr = 0
        self.nums = nums
        

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        if self.curr >= len(self.nums):
            return False
        return True

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        if self.curr >= len(self.nums):
            raise StopIteration
        out = self.nums[self.curr]
        self.curr += 1
        return out

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.defaultIterator = copy.deepcopy(iterator)
        self.iterator = iterator
        self.count = 0
        
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.iterator.hasNext():
            out = self.iterator.next()
        else:
            raise StopIteration
        self.iterator = copy.deepcopy(self.defaultIterator)
        for i in range(0, self.count):
            self.iterator.next()
        return out
        

    def next(self):
        """
        :rtype: int
        """
        
        self.count += 1
        return self.iterator.next()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.iterator.hasNext()


nums = [1,2,3,4]
nums2 = [[[1,2,3,4]],[],[],[],[],[],[],[],[],[],[],[],[],[]]
i = Iterator(nums2)
peekIterator = PeekingIterator(i)

# print(peekIterator.peek())
# print(peekIterator.peek())
# print(peekIterator.next())

print(peekIterator.hasNext())
print(peekIterator.peek())
print(peekIterator.peek())
print(peekIterator.next())
print(peekIterator.next())
print(peekIterator.peek())
print(peekIterator.peek())
print(peekIterator.next())
print(peekIterator.hasNext())
print(peekIterator.peek())
print(peekIterator.hasNext())
print(peekIterator.next())
print(peekIterator.hasNext())



