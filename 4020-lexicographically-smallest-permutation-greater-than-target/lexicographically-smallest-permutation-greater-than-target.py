from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        
        def check(i, strict):
            if i == n:
                return not strict
            
            nonlocal cnt
            for c_code in range(ord('a'), ord('z') + 1):
                c = chr(c_code)
                if cnt[c] > 0:
                    if strict and c < target[i]:
                        continue
                    
                    cnt[c] -= 1
                    
                    next_strict = strict and (c == target[i])
                    
                    if not next_strict:
                        ans[i] = c
                        j = i + 1
                        for ch_code in range(ord('a'), ord('z') + 1):
                            ch = chr(ch_code)
                            while cnt[ch] > 0:
                                ans[j] = ch
                                j += 1
                                cnt[ch] -= 1
                        return True
                    
                    if check(i + 1, next_strict):
                        ans[i] = c
                        return True
                        
                    cnt[c] += 1
            return False

        ans = [""] * n
        if check(0, True):
            return "".join(ans)
        return ""
