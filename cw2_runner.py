import pygame
from sys import exit

pygame.init()  #inicjalizacja biblioteki pygame
screen = pygame.display.set_mode((600, 400))  #rozmiar okna
pygame.display.set_caption("Moja pierwsza gra")  #nazwa okienka
# dodajemy framerate
clock = pygame.time.Clock()
game_active = True
font = pygame.font.SysFont("Arial", 24)

background_surface = pygame.image.load('images_PG/background.png').convert()

mushroom_surface = pygame.image.load('images_PG/mashroom.png').convert_alpha()
mushroom_rect = mushroom_surface.get_rect(midbottom=(500, 350))
# mushroom_pos_x = 500

player_surface = pygame.image.load('images_PG/girl_stay.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(50, 350))
player_gravity = 0

game_msg = font.render("Naciśnij spację, żeby zagrać dalej", 1, "White")
game_msg_rect = game_msg.get_rect(center=(300, 200))

while True:
    # 1. sprawdzanie inputu od użytkownika
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 350:
                    #print('nacisnieto spacje')
                    player_gravity = -20

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                mushroom_rect.left = 700

    if game_active:
        screen.blit(background_surface, (0, 0))

        mushroom_rect.x -= 5
        if mushroom_rect.x < -100:
            mushroom_rect.x = 700
        screen.blit(mushroom_surface, mushroom_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 350:
            player_rect.bottom = 350
        screen.blit(player_surface, player_rect)

        if player_rect.colliderect(mushroom_rect):
            #print('Zderzenie')
            # pygame.quit()
            # exit()
            game_active = False
    else:
        screen.fill("Black")
        screen.blit(game_msg, game_msg_rect)


    # 3. ciągły update ekranu
    pygame.display.update()
    clock.tick(60)  #ustawienie 60fps
