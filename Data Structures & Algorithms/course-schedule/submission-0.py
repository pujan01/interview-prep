class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        # adjList = {a:b, }
        indegree = defaultdict(int)

        for u, v in prerequisites:
            adjList[u].append(v)
            indegree[v] += 1
            indegree[u] += 0

        q = collections.deque()
        for key, val in indegree.items():
            if val == 0:
                q.append(key)

        totalCourses = len(indegree)
        while q:
            qLen = len(q)
            for _ in range(qLen):
                course = q.popleft()
                totalCourses -= 1
                for dep in adjList[course]:
                    indegree[dep] -= 1
                    if indegree[dep] == 0:
                        q.append(dep)
        
        return True if totalCourses == 0 else False
        
         

        
