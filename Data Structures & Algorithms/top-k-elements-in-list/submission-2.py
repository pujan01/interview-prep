class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        # {7:2}
        buckets = [[] for _ in range(len(nums)+1)]
        for values, count in counts.items():
            buckets[count].append(values)

        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
                if len(res) == k:
                    return res
        