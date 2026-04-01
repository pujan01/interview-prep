class Solution:
    def isValid(self, s: str) -> bool:
        begin = [ '(', '[', '{'];
        end = [ ')', '}', ']'];
        myMap = {')': '(', ']': '[', '}': '{'}
        procs = [1 for x in range(len(s))]
        print(procs)
        index = 0
        for char in s: 
            if char in begin:
                procs[index] = char
                index = index + 1
            if char in end:
                if procs[index-1] != myMap.get(char):
                    return False
                index -= 1
        if (index == 0):
            return True
        return False

                
