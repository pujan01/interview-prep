class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(i, j, visited, prevValue):
            if 0 <= i < m and 0 <= j < n and (i,j) not in visited and heights[i][j] >= prevValue:
                visited.add((i,j))
                dirs = [(0,1), (1,0), (0,-1), (-1,0)]
                for r,c in dirs:
                    dfs(i+r, j+c, visited, heights[i][j])

        for i in range(m):
            dfs(i, 0, pacific, 0)
            dfs(i, n-1, atlantic, 0)

        for j in range(n):
            dfs(0, j, pacific, 0)
            dfs(m-1, j, atlantic, 0)
        
        res = []
        for x,y in pacific:
            if (x,y) in atlantic:
                res.append([x,y])
        return res
                
