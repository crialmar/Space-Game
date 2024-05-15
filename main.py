import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Invasión espacial")
icon = pygame.image.load("cohete.png")
pygame.display.set_icon(icon)

#* JUGADOR
#-------> tamaño del jugador
Widht_Player = 60
Heigth_Player = 60

#-------> importamos la imagen y la escalamos
Img_Original = pygame.image.load("astronave1.png")
Img_Gamer = pygame.transform.scale(Img_Original, (Widht_Player, Heigth_Player))

#-------> establecemos posición
player_x = 370
player_y = 530
player_x_change = 0


#! ENEMIGO
#-------> tamaño del jugador
Widht_Enemy = 60
Heigth_Enemy = 60

#-------> importamos la imagen y la escalamos
Img_Original_Enemy = pygame.image.load("ovni.png")
Img_Enemy = pygame.transform.scale(Img_Original_Enemy, (Widht_Enemy, Heigth_Enemy))

#-------> establecemos posición
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50,200)
enemy_x_change = 0.2
enemy_y_change = 25


def player(x, y):
    ''',,,,,'''
    screen.blit(Img_Gamer, (x, y))

def enemy(x, y):
    ''',,,,,'''
    screen.blit(Img_Enemy, (x, y))


running = True
while running:

    screen.fill((81, 22, 147))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.2
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0


    player_x += player_x_change

    # mantener dentro de pantalla
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736
 

    enemy_x += enemy_x_change

    # mantener dentro de pantalla
    if enemy_x <= 0:
        enemy_x_change = 0.2
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -0.3
        enemy_y += enemy_y_change


    player(player_x, player_y)
    enemy(enemy_x, enemy_y)

    pygame.display.update()

