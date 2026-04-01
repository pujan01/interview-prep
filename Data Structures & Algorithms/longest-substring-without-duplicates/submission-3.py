from collections import OrderedDict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # abba
        # slow: 0
        # fast: 0
        # hashmap: {} 
        max_length = 0
        slow = 0 
        hashmap = OrderedDict()
        for fast in range(len(s)):
            if s[fast] in hashmap:
                new_slow = hashmap[s[fast]] + 1
                for _ in range(new_slow - slow):
                    hashmap.popitem(last = False)
                slow = new_slow
            hashmap[s[fast]] = fast
            max_length = max(max_length, fast - slow + 1)
        return max_length
