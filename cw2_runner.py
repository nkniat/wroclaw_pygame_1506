import pygame
from sys import exit

pygame.init()  #inicjalizacja biblioteki pygame
screen = pygame.display.set_mode((600, 400))  #rozmiar okna
pygame.display.set_caption("Moja pierwsza gra")  #nazwa okienka
# dodajemy framerate
clock = pygame.time.Clock()

background_surface = pygame.image.load('images_PG/background.png').convert()

mushroom_surface = pygame.image.load('images_PG/mashroom.png').convert_alpha()
mushroom_rect = mushroom_surface.get_rect(midbottom=(500, 350))
# mushroom_pos_x = 500

player_surface = pygame.image.load('images_PG/girl_stay.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(50, 350))

while True:
    # 1. sprawdzanie inputu od użytkownika
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_surface, (0, 0))

    mushroom_rect.x -= 5
    screen.blit(mushroom_surface, mushroom_rect)
    screen.blit(player_surface, player_rect)

    if mushroom_rect.x < -100:
        mushroom_rect.x = 700

    # if player_rect.colliderect(mushroom_rect):
    #     print('Zderzenie')

    # 3. ciągły update ekranu
    pygame.display.update()
    clock.tick(60)  #ustawienie 60fps
