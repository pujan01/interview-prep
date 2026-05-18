class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # odd length
            l = r = i
            window = 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if window > len(res):
                    res = s[l:r+1]
                window += 2
                l -= 1
                r += 1

            l, r = i, i + 1
            window = 2
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if window > len(res):
                    res = s[l:r+1]
                window += 2
                l -= 1
                r += 1
        return res
