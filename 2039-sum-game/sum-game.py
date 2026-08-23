class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2
        left_sum = sum(int(c) for c in num[:mid] if c != '?')
        right_sum = sum(int(c) for c in num[mid:] if c != '?')
        
        left_q = num[:mid].count('?')
        right_q = num[mid:].count('?')
        return (right_sum - left_sum) * 2 != (left_q - right_q) * 9
