#!/usr/bin/python3
"""alx interview island perimiter"""


def island_perimeter(grid):
    """function that returns perimiter
    Args:
        grid: list of a list.
    """
    visited = set()

    def dfs(i, j):
        """dfs search algorithm"""
        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 \
                or grid[i][j] == 0:
            return 1
        if (i, j) in visited:
            return 0

        visited.add((i, j))
        per = dfs(i + 1, j)
        per += dfs(i - 1, j)
        per += dfs(i, j + 1)
        per += dfs(i, j - 1)
        return per

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return dfs(i, j)
    return 0

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]

    grid2 = [
        [0,0,0,0,0,0],
        [0,1,1,1,0,0],
        [0,1,1,1,0,0],
        [0,1,1,1,0,0]
    ]

    grid3 = [[0], [0], [0]]

    print(island_perimeter(grid))
    print(island_perimeter(grid2))
    print(island_perimeter(grid3))
