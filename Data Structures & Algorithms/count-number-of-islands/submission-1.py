class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        s = set()

        def dfs(r,c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return
            if grid[r][c] == '0' or (r, c) in s:
                return
            
            s.add((r,c))

            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)
        
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in s:
                    islands += 1
                    dfs(r, c)
        
        return islands
        