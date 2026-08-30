class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        s = set()

        def dfs(r,c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            if (r,c) in s:
                return 0
            
            s.add((r,c))

            return 1 + dfs(r, c + 1) + dfs(r, c - 1) + dfs(r + 1, c) + dfs(r - 1, c)
        
        area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                area = max(area, dfs(r,c))
        
        return area