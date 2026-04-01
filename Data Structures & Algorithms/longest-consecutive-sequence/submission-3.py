class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [0,3,2,5,4,6,1,1]
        # [1,2,2,1,4,6,1,1] 
        # [1,2,4,4,4,6,1,1] 4 is found (num + mp[num +1]), (num - mp[num -1] )
        # [1,2,2,1,4,5,1,1] 6 is found 
        # [1,2,2,1,4,5,1,1] 1 is found 

        longest = 0
        mp = defaultdict(int)

        for num in nums:
            print(mp)

            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                print(mp[num], mp[num+1], mp[num-1])
                print(num, num + mp[num + 1], num - mp[num - 1])
                mp[num + mp[num + 1]]= mp[num]
                mp[num - mp[num - 1]]= mp[num]
                longest = max(longest, mp[num])
        return longest        