class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1)//2
        nums_Sum = sum(nums)
        return total - nums_Sum