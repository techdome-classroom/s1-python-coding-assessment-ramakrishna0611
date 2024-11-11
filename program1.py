class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(r, c):
            # Mark the current cell as visited
            grid[r][c] = 'W'  # We mark land as water to avoid revisiting it
            # Explore the four possible directions (up, down, left, right)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 'L':
                    dfs(nr, nc)
        
        island_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'L':  # Found a new island
                    island_count += 1
                    dfs(i, j)  # Use DFS to mark all land connected to this cell
        
        return island_count
