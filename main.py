import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Invasión espacial")
icon = pygame.image.load("cohete.png")
pygame.display.set_icon(icon)
background = pygame.image.load("fondo_.jpg")

#* JUGADOR
#-------> tamaño del jugador
Widht_Player = 60
Heigth_Player = 60

#-------> importamos la imagen y la escalamos
Img_Original = pygame.image.load("astronave1.png")
Img_Gamer = pygame.transform.scale(Img_Original, (Widht_Player, Heigth_Player))

#-------> establecemos posición
Player_x = 370
Player_y = 530
Player_x_change = 0


#! ENEMIGO
#-------> tamaño del jugador
Widht_Enemy = 60
Heigth_Enemy = 60

#-------> importamos la imagen y la escalamos
Img_Original_Enemy = pygame.image.load("ovni.png")
Img_Enemy = pygame.transform.scale(Img_Original_Enemy, (Widht_Enemy, Heigth_Enemy))

#-------> establecemos posición
Enemy_x = random.randint(0, 736)
Enemy_y = random.randint(50,200)
Enemy_x_change = 0.2
Enemy_y_change = 25

#! DISPARO
#-------> tamaño del jugador
Widht_Shot = 60
Heigth_Shot = 60

#-------> importamos la imagen y la escalamos
Img_Original_Shot = pygame.image.load("disparo.png")
Img_Shot = pygame.transform.scale(Img_Original_Shot, (Widht_Shot, Heigth_Shot))

#-------> establecemos posición
shot_x = 0
shot_y = 530
shot_x_change = 0
shot_y_change = 0.5
shot_visible = False

def Player(x, y):
    ''',,,,,'''
    screen.blit(Img_Gamer, (x, y))

def Enemy(x, y):
    ''',,,,,'''
    screen.blit(Img_Enemy, (x, y))


def fire_shot(x, y):
    ''',,,,,'''
    global shot_visible
    shot_visible = True
    screen.blit(Img_Shot, (x , y + 10))


running = True
while running:

    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Player_x_change = -0.2
            if event.key == pygame.K_RIGHT:
                Player_x_change = 0.2
            if event.key == pygame.K_SPACE:
                if not shot_visible:
                    shot_x = Player_x
                    fire_shot(shot_x, shot_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Player_x_change = 0
            

    Player_x += Player_x_change

    # mantener dentro de pantalla
    if Player_x <= 0:
        Player_x = 0
    elif Player_x >= 736:
        Player_x = 736
 

    Enemy_x += Enemy_x_change

    # mantener dentro de pantalla
    if Enemy_x <= 0:
        Enemy_x_change = 0.2
        Enemy_y += Enemy_y_change
    elif Enemy_x >= 736:
        Enemy_x_change = -0.3
        Enemy_y += Enemy_y_change


    if shot_y <= -60:
        shot_y = 530
        shot_visible = False

    if shot_visible:
        fire_shot(shot_x, shot_y)
        shot_y -= shot_y_change

    Player(Player_x, Player_y)
    Enemy(Enemy_x, Enemy_y)

    pygame.display.update()

