class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        buckets = [[] for _ in range(len(nums)+1)]
        for num, count in freq.items():
            buckets[count].append(num)
        res = []
        for i in range(len(buckets) -1 , -1 ,-1):
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
                if len(res) == k:
                    return res 
        
