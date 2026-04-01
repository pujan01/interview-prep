class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        maps = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i+1:]
                maps[key].append(word)
        adjList = defaultdict(list)
        for key,val in maps.items():
            if len(val) < 2: continue
            for i in range(len(val)):
                word = val[i]
                for j in range(len(val)):
                    if word != val[j]:
                        adjList[word].append(val[j])
        print(adjList)
        q = deque([beginWord])
        res = 1
        visit = set([beginWord])
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res 
                for nei in adjList[word]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
            res += 1 
        return 0 
