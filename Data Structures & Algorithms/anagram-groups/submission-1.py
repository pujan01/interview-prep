class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        if not strs:
            return [[]]
        
        # get the letters in the word 
        for word in strs:
            counts = [0] * 26
            for c in word:
                counts[ord(c) - ord('a')] += 1 
            res[tuple(counts)].append(word)

        return list(res.values())

        