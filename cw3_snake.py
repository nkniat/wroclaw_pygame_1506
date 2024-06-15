import pygame
pygame.init()

WIDTH, HEIGHT = 480, 480
GREEN = (0, 255, 0)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

SIZE = 20

class Snake():
    def __init__(self):
        self.__len = 1
        self.__position = [(WIDTH / 2, HEIGHT / 2)]
        self.__move_direction = UP
        self.__score = 0
        self.__color = GREEN

    def head_position(self):
        return self.__position[-1]  #ostatni element listy to głowa węża

    def direction(self, move_direction):
        if self.__len > 1:  # TODO
            return
        else:
            self.__move_direction = move_direction


    def move(self):
        head = self.head_position()
        x, y = self.__move_direction

        new_position = (((head[0] + (x * SIZE)) % WIDTH), (head[1] + (y * SIZE)) % HEIGHT)

        #kolizja sama ze sobą
        if len(self.__position) > 2 and new_position in self.__position[2:0]:
            self.reset()
        # kolizję ze ścianą
        elif (new_position[1] == 0 and y == 1) or (new_position[1] == 480 and y == -1):
            self.reset()
        elif (new_position[0] == 0 and x == 1) or (new_position[0] == 480 and x == -1):
            self.reset()
        else:
            self.__position.append(new_position)


    def reset(self):
        self.__len = 1
        self.__position = [(WIDTH / 2, HEIGHT / 2)]
        self.__move_direction = UP
        self.__score = 0

    def draw(self, win):
        for p in self.__position[::-1]:
            r = pygame.Rect((p[0], p[1]), (SIZE, SIZE))
            pygame.draw.rect(win, self.__color, r)

    def eat(self):
        self.__len += 1
        self.__score += 1


class Food():
    def __init__(self):
        pass

    def random_position(self):
        pass

    def draw(self):
        pass


def draw_board():
    pass


def main():
    pass


if __name__ == "__main__":
    main()
