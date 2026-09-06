class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        res = 0
        for r in range(len(s)):
            c = s[r]
            while c in chars:
                chars.remove(s[l])
                l += 1
            chars.add(c)
            res = max(res, r - l + 1)
        return res
            





                
