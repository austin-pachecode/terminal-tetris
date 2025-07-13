def handle_input(key, tetromino, board):
    if key == ord('a'):
        if board.is_valid_position(tetromino.shape, tetromino.x - 1, tetromino.y):
            tetromino.x -= 1
    elif key == ord('d'):
        if board.is_valid_position(tetromino.shape, tetromino.x + 1, tetromino.y):
            tetromino.x += 1
    elif key == ord('s'):
        if board.is_valid_position(tetromino.shape, tetromino.x, tetromino.y + 1):
            tetromino.y += 1
    elif key == ord('w'):
        rotated = [list(row) for row in zip(*tetromino.shape[::-1])]
        if board.is_valid_position(rotated, tetromino.x, tetromino.y):
            tetromino.rotate()