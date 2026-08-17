class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        
        # 1. Prefix sums for O(1) subarray sum queries
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]
            
        # 2. DP tables
        # dp[l][r] stores the max score for interval [l, r]
        dp = [[0] * n for _ in range(n)]
        
        # max_l[l][r] stores max_{k=l...r} (dp[l][k] + sum(l...k))
        max_l = [[0] * n for _ in range(n)]
        
        # max_r[l][r] stores max_{k=l...r} (dp[k][r] + sum(k...r))
        max_r = [[0] * n for _ in range(n)]
        
        # Base cases for single-element intervals
        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]
            
        # 3. Sliding pointer to find split intervals
        mid_ptr = [i for i in range(n)]
        
        # Process intervals by increasing length
        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                
                # Advance mid pointer until the left partition is >= right partition
                while mid_ptr[l] < r and (pref[mid_ptr[l] + 1] - pref[l]) < (pref[r + 1] - pref[mid_ptr[l] + 1]):
                    mid_ptr[l] += 1
                    
                m = mid_ptr[l]
                res = 0
                
                # Case 1: Split k lies in [l, m-1] -> Left partition is strictly smaller
                if m > l:
                    res = max(res, max_l[l][m - 1])
                    
                # Case 2: Split k lies in [m, r-1] -> Right partition is smaller or equal
                if m < r:
                    left_sum = pref[m + 1] - pref[l]
                    right_sum = pref[r + 1] - pref[m + 1]
                    
                    if left_sum == right_sum:
                        # Equal sums mean Alice can pick either side safely
                        res = max(res, max_l[l][m], max_r[m + 1][r])
                    else:
                        # Right side is strictly smaller for k = m
                        res = max(res, right_sum + dp[m + 1][r])
                        # Right side is smaller for k > m
                        if m + 1 < r:
                            res = max(res, max_r[m + 2][r])
                            
                # Update DP states for the current [l, r] window
                dp[l][r] = res
                max_l[l][r] = max(max_l[l][r - 1], dp[l][r] + pref[r + 1] - pref[l])
                max_r[l][r] = max(max_r[l + 1][r], dp[l][r] + pref[r + 1] - pref[l])
                
        return dp[0][n - 1]
