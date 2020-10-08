"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally
or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        if not grid:
            return count

        rows = len(grid)
        cols = len(grid[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    count += 1
                    queue = [(row, col)]

                    while queue:
                        size = len(queue)

                        for _ in range(size):
                            # Must use name other than row and col
                            # Otherwise there will be collision
                            x, y = queue.pop(0)

                            for _x, _y in directions:
                                dx, dy = x + _x, y + _y

                                if (
                                    dx > rows - 1
                                    or dx < 0
                                    or dy > cols - 1
                                    or dy < 0
                                    or grid[dx][dy] != "1"
                                ):
                                    continue

                                grid[dx][dy] = 'visited'
                                queue.append((dx, dy))

        return count
