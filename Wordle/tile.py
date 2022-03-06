import random

class Tile:
    def __init__(self, txt: str, color=None):
        self.txt = txt
        self.color = random.randint(1, 4)

    def __str__(self):
        if self.color == 1:
            return f"\033[1;37;40m {self.txt}"
        elif self.color == 2:
            return f"\033[1;33;40m {self.txt}"
        elif self.color == 3:
            return f"\033[1;32;40m {self.txt}"

if __name__ == '__main__':
    tile = Tile(txt='e')
    print(tile)