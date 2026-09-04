class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        # Create an array to store the suffix minimums from right to left
        right = [nums[-1]] * n
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])
            
        # Track the running maximum from the left prefix
        left = 0
        for i, x in enumerate(nums):
            left = max(left, x)
            # Check if the instability score is less than or equal to k
            if left - right[i] <= k:
                return i
                
        return -1
