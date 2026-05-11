class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.text = []
        n = len(text1)
        m = len(text2)

        dp = {}
        ans = 0
        def recur(i, j):
            if i == n or j == m:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if text1[i] == text2[j]:
                ans = 1 + recur(i+1, j+ 1)
            else:
                ans = max(recur(i+1, j), recur(i, j+1))
            dp[(i,j)] = ans
            return dp[(i,j)] 

        return recur(0,0)
            

