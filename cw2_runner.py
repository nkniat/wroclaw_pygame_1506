import pygame
from sys import exit


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = font.render(f'{current_time}', 1, "White")
    score_rect = score_surface.get_rect(center=(300, 50))
    screen.blit(score_surface, score_rect)
    # TODO return - score


def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 350:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]


pygame.init()  #inicjalizacja biblioteki pygame
screen = pygame.display.set_mode((600, 400))  #rozmiar okna
pygame.display.set_caption("Moja pierwsza gra")  #nazwa okienka
# dodajemy framerate
clock = pygame.time.Clock()
game_active = True
start_time = 0
font = pygame.font.SysFont("Arial", 24)

background_surface = pygame.image.load('images_PG/background.png').convert()

mushroom_surface = pygame.image.load('images_PG/mashroom.png').convert_alpha()
mushroom_rect = mushroom_surface.get_rect(midbottom=(500, 350))
# mushroom_pos_x = 500

# player_surface = pygame.image.load('images_PG/girl_stay.png').convert_alpha()
# player_rect = player_surface.get_rect(midbottom=(50, 350))
player_gravity = 0

player_jump = pygame.image.load('images_PG/girl_jump.png')
prayer_walk_1 = pygame.image.load('images_PG/girl_walk.png')
prayer_walk_2 = pygame.image.load('images_PG/girl_walk2.png')
player_walk = [prayer_walk_1, prayer_walk_2]
player_index = 0

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(50, 350))

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

        else:  #restart gry
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                mushroom_rect.left = 700
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(background_surface, (0, 0))
        display_score()

        mushroom_rect.x -= 5
        if mushroom_rect.x < -100:
            mushroom_rect.x = 700
        screen.blit(mushroom_surface, mushroom_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 350:
            player_rect.bottom = 350
        player_animation()
        screen.blit(player_surf, player_rect)


        if player_rect.colliderect(mushroom_rect):
            #print('Zderzenie')
            # pygame.quit()
            # exit()
            game_active = False
    else:
        screen.fill("Black")
        screen.blit(game_msg, game_msg_rect)
        # TODO > wyswietl aktualny wynik

    # 3. ciągły update ekranu
    pygame.display.update()
    clock.tick(60)  #ustawienie 60fps
