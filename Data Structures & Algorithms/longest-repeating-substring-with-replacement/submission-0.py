class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # AAABABBBBC
        l = 0 
        chars = {}
        maxChar = 0
        max_frequency = 0 
        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1
            max_frequency = max(max_frequency, chars[s[r]])
            while ( r - l  + 1 ) - max_frequency > k:
                chars[s[l]] -= 1
                l += 1
                max_frequency = max(chars.values()) if chars else 0 
            maxChar = max(maxChar, r - l + 1)
        return maxChar


        
