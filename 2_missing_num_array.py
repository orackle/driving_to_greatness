class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # total sum
        # expected sum
        # return the -
        n = len(nums)
        x = int((n*(n+1))/2)
        return x - sum(nums)

    def another_bit_solution(self, nums:List[int]) ->int:
        # XOR with itself is 0 
        # so whatever is left is the missing number
        x = 0
        for i in range(len(nums)+1):
            x ^= i
        for j in nums:
            x ^= j
        return x