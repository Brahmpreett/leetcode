class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            bit = n&1
            # shift the result left to make room, then put the new bit into that empty position.
            result = (result<<1) | bit
            n>>=1
        return result