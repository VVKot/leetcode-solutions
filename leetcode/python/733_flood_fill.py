"""
T: O(R*C)
S: O(R*C)

We check if the new color is the same - in this case, no action is needed.
After that, we do DFS from the starting point using old color as a way to tell
which nodes we should consider. No need to maintain a separate set of visited
nodes since we already know that by their color.
"""


from typing import List, Tuple


class Solution:

    def floodFill(self,
                  image: List[List[int]],
                  sr: int,
                  sc: int,
                  newColor: int) -> List[List[int]]:
        old_color = image[sr][sc]
        if old_color == newColor:
            return image
        stack = [(sr, sc)]
        while stack:
            r, c = stack.pop()
            if image[r][c] == old_color:
                image[r][c] = newColor
                nodes_near = self.get_near(image, r, c)
                stack.extend(nodes_near)
        return image

    def get_near(self,
                 image: List[List[int]],
                 row: int,
                 col: int) -> List[Tuple[int, int]]:
        R = len(image)
        C = len(image[0])
        nodes_near = []
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_r, new_c = row + dr, col + dc
            if 0 <= new_r < R and 0 <= new_c < C:
                nodes_near.append((new_r, new_c))
        return nodes_near
