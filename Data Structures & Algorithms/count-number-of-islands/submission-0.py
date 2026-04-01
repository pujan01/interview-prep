class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and not visited[i][j] and int(grid[i][j]):
                visited[i][j] = 1 
                dirs= [(0,1), (1,0), (0,-1), (-1,0)]
                for x, y in dirs:
                    dfs(i+x, j+y)
                return 1 
            return 0
        
        count = 0 
        for i in range(m):
            for j in range(n):
                count += dfs(i,j)
        return count


                