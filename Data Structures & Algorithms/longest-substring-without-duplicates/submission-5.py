class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0 
        l = 0 
        maps = {}
        for r in range(len(s)):
            c = s[r]
            if c in maps:
                l = max(l, maps[c] + 1)
            res = max(res, r - l + 1)
            maps[c] = r
        return res

            