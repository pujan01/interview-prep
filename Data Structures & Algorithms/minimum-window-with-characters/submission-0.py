class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = {}
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1
        window = {}
        l = 0
        minLength = 10000000 
        minSubstring = ""
        for r, c in enumerate(s):
            if c not in tCount and not window: 
                l += 1
                continue
            if c not in tCount:
                window[c] = window.get(c, 0) + 1
                continue
            window[c] = window.get(c, 0) + 1
            while self.checkValuesOfCounters(tCount, window):
                if minLength > r - l + 1:
                    minLength = r - l + 1
                    minSubstring = s[l:r+1]
                window[s[l]] = window.get(s[l], 0) - 1
                l+= 1 
        return minSubstring
                
    def checkValuesOfCounters(self, counter1, counter2):
        # if all values of counter1 are in counter2, then return true 
        print(counter1, counter2)
        for key in counter1:
            if counter1[key] > counter2.get(key, -1):
                return False
        return True