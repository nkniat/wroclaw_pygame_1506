import pygame
from sys import exit

pygame.init()  #inicjalizacja biblioteki pygame
screen = pygame.display.set_mode((800, 400))  #rozmiar okna
pygame.display.set_caption("Moja pierwsza gra")  #nazwa okienka
# dodajemy framerate
clock = pygame.time.Clock()

X, Y = 10, 10

while True:
    # 1. sprawdzanie inputu od użytkownika
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # 2a. rysowanie elementów
    #pygame.draw.rect(screen, "White", (X, Y, 10, 10))
    pygame.draw.line(screen, (255, 0, 0), (X, Y), (X, Y + 200), 5) # pion
    pygame.draw.line(screen, (0, 255, 0), (X, Y), (X + 200, Y), 5) # poziom
    # fraktale TODO

    # 2b. renderowanie czcionek
    # definicja czcionki
    font = pygame.font.SysFont('Arial', 24)
    # renderowanie napisu
    label = font.render('Hello World', 1, 'White')
    # wyswietlenie napisu na ekran
    screen.blit(label, (X + 50, Y + 50))

    # 3. ciągły update ekranu
    pygame.display.update()
    clock.tick(60)  #ustawienie 60fps
