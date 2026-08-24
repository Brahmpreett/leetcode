class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)
        prefix = list(stones)
        for i in range(1, n):
            prefix[i] += prefix[i - 1]
        res = prefix[-1]
        for i in range(n - 2, 0, -1):
            res = max(res, prefix[i] - res)
            
        return res
