class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        freshFruits = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    freshFruits += 1
                    
        time = 0 
        maxTime = 0 

        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        while q:
            length = len(q)
            for _ in range(length):
                r, c = q.popleft()
                dirs = [(0,1), (1,0), (-1,0), (0,-1)]
                for x,y in dirs:
                    nr, nc = r +x, c + y
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and not visited[nr][nc] and grid[nr][nc] == 1:
                        visited[nr][nc] = 1
                        q.append((nr, nc))
                        freshFruits -= 1
            maxTime = max(time, maxTime)
            time += 1 
        
        return maxTime if freshFruits == 0 else -1

