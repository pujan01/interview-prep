class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort 
        # convert the prerequisites array to a graph first 
        if not prerequisites: return True
        prereq = defaultdict(list)
        depend = [0] * (numCourses)
        queue = collections.deque()
        for cr, pre in prerequisites:
            prereq[pre].append(cr) 
            depend[cr] += 1
        for i, dep in enumerate(depend):
            if dep == 0:
                queue.append(i)
        res = 0
        while queue:
            lenq = len(queue)
            for _ in range(lenq):
                cr = queue.popleft()
                res += 1
                for nei in prereq[cr]:
                    depend[nei] -= 1
                    if depend[nei] == 0:
                        queue.append(nei)
        return res == numCourses 

        

