class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Find the indices of the minimum and maximum values
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        
        # Step 2: Ensure a is the smaller index and b is the larger index
        a = min(min_idx, max_idx)
        b = max(min_idx, max_idx)
        
        # Step 3: Calculate deletions for each strategy
        # Strategy 1: Delete both from the front
        del_front = b + 1
        
        # Strategy 2: Delete both from the back
        del_back = n - a
        
        # Strategy 3: Delete 'a' from front and 'b' from back
        del_both = (a + 1) + (n - b)
        
        # Return the minimum number of deletions among the three choices
        return min(del_front, del_back, del_both)
