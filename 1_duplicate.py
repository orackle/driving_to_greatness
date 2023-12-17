# mine
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # iterate through the list O(n)
        # add to hashset O(1)
        #  total O(n)
        # comparison is O(1)
        if set(nums) == len(nums):
            return False
        return True

# most efficient solution

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create hashset and check if in hashset. 
        # O(n) time complexity
        
        x = set()
        for i in nums:
            if i in x:
                return True
            x.add(i)
        return False
        
        
# 217. Contains Duplicate
# Solved
# Easy
# Topics
# Companies
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true