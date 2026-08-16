from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num # doing xor
            # bec 4 ^ 1 ^ 1 is 4 ^ 0 that is 4
        return ans