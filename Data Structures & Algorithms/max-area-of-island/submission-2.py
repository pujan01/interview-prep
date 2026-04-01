class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0 
        m = len(grid)
        n = len(grid[0])
        dirs = [(0,1), (1,0), (-1, 0), (0,-1)]
        visited = [[0 for _ in range(n)] for _ in range(m)]
        area = 0
        def dfs(r, c):
            if 0 <= r < m and 0 <= c < n and not visited[r][c] and grid[r][c]:
                visited[r][c] = 1
                area = 1
                for dx, dy in dirs:
                    area += dfs(r + dx, c + dy)
                return area
            return 0
        
        for i in range(m):
            for j in range(n):
                maxArea = max(maxArea, dfs(i,j))
        return maxArea

        

                