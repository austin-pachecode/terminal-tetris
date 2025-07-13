import random
from constants import TETROMINO_SHAPES

class Tetromino:
    def __init__(self):
        self.type = random.choice(list(TETROMINO_SHAPES.keys()))
        self.shape = TETROMINO_SHAPES[self.type]
        self.x = 3
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]