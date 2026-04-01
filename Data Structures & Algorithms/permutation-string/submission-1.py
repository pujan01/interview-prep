class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 
        s1Chars = {}
        for c in s1:
            s1Chars[c] = s1Chars.get(c, 0) + 1
        windowChars = {}
        for r, c in enumerate(s2):
            if c not in s1Chars:
                windowChars = {}
                l = r + 1
                continue
            windowChars[c] = windowChars.get(c, 0) + 1
            while r - l + 1 > len(s1):
                windowChars[s2[l]] -= 1
                if windowChars[s2[l]] == 0:
                    del windowChars[s2[l]]
                l += 1
            if r - l + 1 == len(s1) and s1Chars == windowChars:
                return True
            

        return False