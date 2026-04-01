
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Input: nums = [1,1,2,3,3,3, 3], k = 2
        # Output: [2,3]
        # how many 1, how many 2, how many 3, ... 
        buckets = [ [] for i in range(len(nums) + 1)]
        myMap = {}
        for n in nums:
            # {1:2, 2: 1, 3: 4}
            myMap[n] = myMap.get(n, 0) + 1

        index = 1
        for key, val in myMap.items():
            # {1:2, 2: 1, 3: 4, 4:1}
            # [0:0, 1:[2, 4], 2: [1], 3:[], 4:[3]]
            buckets[val].append(key)
        res = []
        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res


