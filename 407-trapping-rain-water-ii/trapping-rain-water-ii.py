class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # Check if heightMap is empty
        if not heightMap:
            return 0

        # Get the dimensions of the heightMap
        m, n = len(heightMap), len(heightMap[0])

        # Define the maximum height possible
        max_height = 2 * 10**4

        # Define directions for neighboring cells
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Helper function to check if a cell is within the map
        def is_in_map(row, col):
            return 0 <= row < m and 0 <= col < n

        # Depth-first search (DFS) function to process water flow
        def dfs(row, col):
            if not is_in_map(row, col):
                return

            if heightMap[row][col] != 0:
                return

            for dir_row, dir_col in directions:
                next_row, next_col = row + dir_row, col + dir_col
                if not is_in_map(next_row, next_col) or heightMap[next_row][next_col] == -1:
                    nonlocal curr_water
                    curr_water -= 1
                    heightMap[row][col] = -1
                    break

            if heightMap[row][col] == 0:
                return

            for dir_row, dir_col in directions:
                next_row, next_col = row + dir_row, col + dir_col
                dfs(next_row, next_col)

        ans = 0
        curr_water = 0
        coordinates = {}

        # Create a dictionary to store coordinates of cells with the same height
        for row in range(m):
            for col in range(n):
                h = heightMap[row][col]
                if h not in coordinates:
                    coordinates[h] = []
                coordinates[h].append((row, col))

        # Iterate through possible heights
        for height in range(max_height + 1):
            if height in coordinates:
                for row, col in coordinates[height]:
                    heightMap[row][col] = 0
                    curr_water += 1
                    dfs(row, col)

            ans += curr_water

        return ans