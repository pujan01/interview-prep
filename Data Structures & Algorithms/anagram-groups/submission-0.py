class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a hashmap; key[sorted tuple chars], value:[actual strings]
        mapOfAnagrams = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            mapOfAnagrams[tuple(count)].append(s);

        res = []
        print(mapOfAnagrams)
        for val in mapOfAnagrams.values():
            res.append(val)
        return res

