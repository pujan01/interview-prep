class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #  wordList = ["bat","bag","sag","dag","dot"]
        # 
        if endWord not in wordList:
            return 0
        patDict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                patDict[pattern].append(word)
        q = collections.deque([beginWord])
        res = 1
        visited = set(beginWord)
        while q:
            for j in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res 
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in patDict[pattern]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(word)
            res += 1 
        return 0