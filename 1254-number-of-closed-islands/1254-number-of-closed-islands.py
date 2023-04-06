class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        visit = [[False for _ in range(n)] for _ in range(m)]
        
        def dfs(x, y):
            nonlocal m, n, grid, visit
            
            if x < 0 or x >= m or y < 0 or y >= n:
                return False
            if grid[x][y] == 1 or visit[x][y]:
                return True
            
            visit[x][y] = True
            isClosed = True
            dirx = [0, 1, 0, -1]
            diry = [-1, 0, 1, 0]
            
            for i in range(4):
                r = x + dirx[i]
                c = y + diry[i]
                if not dfs(r, c):
                    isClosed = False
                    
            return isClosed
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not visit[i][j] and dfs(i, j):
                    count += 1
        
        return count