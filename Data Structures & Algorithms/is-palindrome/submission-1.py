class Solution:
    def isPalindrome(self, s: str) -> bool: 
        i =  0 
        j = len(s) - 1
        while i < j:
            print(s[i], s[j])
            while i < j and not self.isAlphaNumeric(s[i]):
                i += 1
            while i < j and not self.isAlphaNumeric(s[j]):
                j -= 1    
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

    def isAlphaNumeric(self, c):
        return (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord("Z")) or (ord(c) >= ord('0') and ord(c) <= ord("9"))



