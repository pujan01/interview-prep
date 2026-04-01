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
        
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            area = 1 
            visited[r][c] = 1 
            while q:
                r,c = q.popleft()
                for dx, dy in dirs:
                    nr, nc = r + dx, c + dy
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc]:
                        q.append((nr, nc))
                        area += 1 
                        visited[nr][nc] = 1
            return area
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    maxArea = max(maxArea, bfs(i,j))
        return maxArea

        

                