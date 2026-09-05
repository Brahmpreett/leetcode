class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return -1





            
        min_suff = [0] * n
        min_suff[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            min_suff[i] = min(nums[i], min_suff[i + 1])
            
        current_max = nums[0]
        for i in range(n):
            current_max = max(current_max, nums[i])
            instability_score = current_max - min_suff[i]
            
            if instability_score <= k:
                return i
                
        return -1
