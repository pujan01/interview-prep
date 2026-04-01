import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        minEatingRate = 9999999999
        while low <= high: 
            eatingRate = (low + high) // 2
            timeTaken = 0
            for pile in piles:
                timeTaken += math.ceil(pile / eatingRate) 
            print(low, high, eatingRate, timeTaken, h)
            if timeTaken <= h:
                minEatingRate = min(eatingRate, minEatingRate)
                high = eatingRate - 1
            else:
                low = eatingRate + 1
        return minEatingRate
        
            
            