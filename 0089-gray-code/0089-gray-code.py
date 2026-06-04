class Solution:
    def grayCode(self, n: int):
        return [i ^ (i >> 1) for i in range(1 << n)]