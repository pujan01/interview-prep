class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.markIsland(grid, i, j, visited, m, n)
                    res += 1
        return res
        
    def markIsland(self, grid, i, j, visited, m, n):
        visited[i][j] = 1
        dirs = [(0,1), (0,-1), (-1,0), (1,0)]
        for x, y in dirs:
            nx, ny = i +x, j + y 
            if 0 <= nx < m and 0 <= ny < n and grid[i][j] == '1' and not visited[nx][ny]:
                self.markIsland(grid, nx, ny, visited, m,n)
        


                