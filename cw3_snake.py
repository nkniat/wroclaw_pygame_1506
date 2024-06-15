import pygame
import random

WIDTH, HEIGHT = 500, 500
GREEN = (0, 255, 0)
RED = (255, 0, 0)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

SIZE = 20
WIDTH_BOX = WIDTH // SIZE
HEIGHT_BOX = HEIGHT // SIZE

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
        self.position = (0,0)
        self.color = RED
        self.random_position()

    def random_position(self):
        self.position = (random.randint(0, WIDTH_BOX - 1) * SIZE, random.randint(0, HEIGHT_BOX - 1) * SIZE)

    def draw(self, win):
        r = pygame.Rect((self.position[0], self.position[1]), (SIZE, SIZE))
        pygame.draw.rect(win, self.color, r)


def draw_board(win):
    win.fill("Black")
    for i in range(0, WIDTH_BOX):
        pygame.draw.line(win, (128, 128, 128), (0, i * SIZE), (WIDTH, i * SIZE))

    for j in range(0, HEIGHT_BOX):
        pygame.draw.line(win, (128, 128, 128), (j * SIZE, 0), (j * SIZE, HEIGHT))


def main():
    pygame.init()

    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")

    draw_board(win)

    snake = Snake()
    food = Food()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.direction(UP)
                if event.key == pygame.K_DOWN:
                    snake.direction(DOWN)
                if event.key == pygame.K_LEFT:
                    snake.direction(LEFT)
                if event.key == pygame.K_RIGHT:
                    snake.direction(RIGHT)

        snake.move()

        if snake.head_position() == food.position:
            snake.eat()
            food.random_position()

        draw_board(win)
        snake.draw(win)
        food.draw(win)
        #win.blit(win, (0,0))

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
