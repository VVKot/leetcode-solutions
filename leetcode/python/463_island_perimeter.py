"""
T: O(R*C)
S: O(1)

One of the multiple ways to solve this problem in constant space.
We count the total number of parts of the island and their neighbors to the
right and to the bottom. Each island part has a perimeter of four, and
connection takes up two units of length.
"""

from typing import List


class Solution:

    WATER, LAND = range(2)
    EDGES_PER_CELL = 4
    EDGES_PER_NEIGHBOR_CONNECTION = 2

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        land_count = neighbor_count = 0
        rows = len(grid)
        cols = len(grid[0])
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == self.LAND:
                    land_count += 1
                    if y < rows - 1:
                        if grid[y + 1][x] == self.LAND:
                            neighbor_count += 1
                    if x < cols - 1:
                        if grid[y][x + 1] == self.LAND:
                            neighbor_count += 1
        return land_count * self.EDGES_PER_CELL - \
            neighbor_count * self.EDGES_PER_NEIGHBOR_CONNECTION
