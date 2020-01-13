def minimumHours(rows, columns, grid):
    # holds (x, y) pairs for every server
    # that might be able to deliver the file to neighbors
    servers = set()
    for x in range(rows):
        for y in range(columns):
            if grid[x][y] == 1:
                servers.add((x, y))

    hours = -1

    # iterating while there are servers
    # that might be able to deliver the file to neighbors
    while len(servers) > 0:
        hours += 1

        # duplicating grid for atomic update
        new_grid = grid.copy()
        new_servers = set()

        for (x, y) in servers:
            adjacent = [
                (x + 1, y),
                (x - 1, y),
                (x, y + 1),
                (x, y - 1)
            ]

            # checking every adjacent cell of this server
            for (ax, ay) in adjacent:
                if ax < 0 or ax >= rows or ay < 0 or ay >= columns:
                    continue

                if grid[ax][ay] == 0:
                    # delivering the file here
                    # and saving the adjacent server for next step
                    new_grid[ax][ay] = 1
                    new_servers.add((ax, ay))

        # updating the grid in one step
        grid = new_grid
        servers = new_servers

    return hours


print(minimumHours(2, 2, [[1, 0], [0, 0]]))
print(minimumHours(4, 4, [[0, 1, 1, 0, 1], [0, 1, 0, 1, 0], [0, 0, 0, 0, 1], [0, 1, 0, 0, 0]]))