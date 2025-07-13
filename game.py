import curses
from tetromino import Tetromino
from board import Board
from input import handle_input
from constants import BOARD_WIDTH, BOARD_HEIGHT

def calculate_score(lines_cleared):
    if lines_cleared == 1:
        return 100
    elif lines_cleared == 2:
        return 300
    elif lines_cleared == 3:
        return 500
    elif lines_cleared >= 4:
        return 800
    return 0

def draw_board(stdscr, board, tetromino):
    offset_x = 2
    offset_y = 1

    width = BOARD_WIDTH
    height = BOARD_HEIGHT

    # Draw top border
    stdscr.addstr(offset_y - 1, offset_x - 2, "╔" + "══" * width + "╗")

    # Draw sides and content
    for y in range(height):
        stdscr.addstr(offset_y + y, offset_x - 2, "║")
        for x in range(width):
            cell = board.grid[y][x]
            content = "[]" if cell else "  "
            stdscr.addstr(offset_y + y, offset_x + x * 2, content)
        stdscr.addstr(offset_y + y, offset_x + width * 2, "║")

    # Draw bottom border
    stdscr.addstr(offset_y + height, offset_x - 2, "╚" + "══" * width + "╝")

    # Draw falling tetromino
    for dy, row in enumerate(tetromino.shape):
        for dx, cell in enumerate(row):
            if cell:
                y = tetromino.y + dy + offset_y
                x = (tetromino.x + dx) * 2 + offset_x
                stdscr.addstr(y, x, "[]")

def run(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(150)

    board = Board()
    tetromino = Tetromino()
    score = 0

    while True:
        stdscr.clear()
        draw_board(stdscr, board, tetromino)
        stdscr.addstr(0, BOARD_WIDTH * 2 + 2, f"Score: {score}")
        stdscr.refresh()

        key = stdscr.getch()
        handle_input(key, tetromino, board)

        if board.is_valid_position(tetromino.shape, tetromino.x, tetromino.y + 1):
            tetromino.y += 1
        else:
            board.place(tetromino.shape, tetromino.x, tetromino.y)
            lines = board.clear_lines()
            score += calculate_score(lines)
            tetromino = Tetromino()
            if not board.is_valid_position(tetromino.shape, tetromino.x, tetromino.y):
                stdscr.addstr(BOARD_HEIGHT // 2, BOARD_WIDTH, "GAME OVER")
                stdscr.refresh()
                stdscr.nodelay(False)
                stdscr.getch()
                break