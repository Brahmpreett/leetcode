class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        a = min(min_idx, max_idx)
        b = max(min_idx, max_idx)
        del_front = b + 1
        
        del_back = n - a
        del_both = (a + 1) + (n - b)
        

        
        return min(del_front, del_back, del_both)
