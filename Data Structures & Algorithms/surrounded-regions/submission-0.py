class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = {}
        m = len(board)
        n = len(board[0])
        
        def dfs(x,y):
            if 0 <= x < m and 0 <= y < n and board[x][y] == "O":
                board[x][y] = "T"
                dfs(x-1, y)
                dfs(x+1, y)
                dfs(x, y-1)
                dfs(x, y+1)

        for i in range(m):
            dfs(i,0)
            dfs(i, n-1)

        for j in range(n):
            dfs(0,j)
            dfs(m-1,j)

        for x in range(m):
            for y in range(n):
                if board[x][y] == "O":
                    board[x][y] = "X"
                if board[x][y] == "T":
                    board[x][y] = "O"
                
