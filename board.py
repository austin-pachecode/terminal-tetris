from constants import BOARD_WIDTH, BOARD_HEIGHT

class Board:
    def __init__(self):
        self.grid = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]

    def is_valid_position(self, shape, x, y):
        for dy, row in enumerate(shape):
            for dx, cell in enumerate(row):
                if cell:
                    nx, ny = x + dx, y + dy
                    if ny >= BOARD_HEIGHT or nx < 0 or nx >= BOARD_WIDTH:
                        return False
                    if ny >= 0 and self.grid[ny][nx]:
                        return False
        return True

    def place(self, shape, x, y):
        for dy, row in enumerate(shape):
            for dx, cell in enumerate(row):
                if cell:
                    self.grid[y + dy][x + dx] = 1

    def clear_lines(self):
        new_grid = []
        cleared = 0
        for row in self.grid:
            if all(cell == 1 for cell in row):
                cleared += 1
            else:
                new_grid.append(row)

        for _ in range(cleared):
            new_grid.insert(0, [0] * BOARD_WIDTH)

        self.grid = new_grid
        return cleared