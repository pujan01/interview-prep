class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))

        distance = 1

        while q:
            length = len(q)
            for _ in range(length):
                r, c = q.popleft()
                dirs = [(0,1), (1,0), (-1,0), (0,-1)]
                for x,y in dirs:
                    nr, nc = r +x, c + y
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = distance
                        q.append((nr, nc))
            distance += 1