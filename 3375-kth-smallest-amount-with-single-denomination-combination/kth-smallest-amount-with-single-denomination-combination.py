from math import gcd
from itertools import combinations

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        subsets_lcm = []
        n = len(coins)
        
        for r in range(1, n + 1):
            sign = 1 if r % 2 != 0 else -1
            for comb in combinations(coins, r):
                current_lcm = comb[0]
                for coin in comb[1:]:
                    current_lcm = (current_lcm * coin) // gcd(current_lcm, coin)
                subsets_lcm.append((current_lcm, sign))
        
        def count_multiples_up_to(target: int) -> int:
            total_count = 0
            for lcm_val, sign in subsets_lcm:
                total_count += sign * (target // lcm_val)
            return total_count

        low = min(coins)
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_multiples_up_to(mid) >= k:
                ans = mid
                high = mid - 1  
            else:
                low = mid + 1   
                
        return ans
