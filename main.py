from Monster import *
import pygame
from random import randint


clock = pygame.time.Clock()


pygame.init()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("The Hobbit: Pyton's Adventure")
#icon = pygame.image.load("I-ICON.png")
#pygame.display.set_icon(icon)

bg = pygame.image.load("images/Back.png")
#player = pygame.image.load("I-ICON.png")

Walk_right = [pygame.image.load('images/Right-1.png'),pygame.image.load('images/Right-2.png')]
Walk_left  = [pygame.image.load('images/Left-1.png'),pygame.image.load('images/Left-2.png')]
Walk_Up = [pygame.image.load('images/Up-1.png'),pygame.image.load("images/Up-2.png")]
Walk_Down = [pygame.image.load('images/Down_-_1.png'),pygame.image.load('images/Down-2.png')]

Nazgul_right = [pygame.image.load("images/Nazgul-2-1.png"),pygame.image.load("images/Nazgul-2-1-right-eyes.png")]
Nazgul_left = [pygame.image.load("images/Nazgul-2-1-left.png"),pygame.image.load("images/Nazgul-2-1-left-eyes.png")]
Nazgul_attack_left = pygame.image.load("images/Nazgul-3-left.png")
Nazgul_attack_right = pygame.image.load("images/Nazgul-3-rigt.png")



n_flag = True
n_timer = pygame.USEREVENT + 1
pygame.time.set_timer(n_timer,10000)
n_list_it_the_game = []
n_animation_count = 0


Player_animation_count = 0
bg_y = 0


player_hp = 50
player_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 30)

player_speed = 15
player_x = 300
player_y = 250
flag_animation = True
Type_anim = 0

gameplay = True
the_end_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 50)
loose_label = the_end_label.render('You died', False, (12, 12, 12))
restart_label = the_end_label.render("Start again", False, (35, 234, 32))
restart_label_rect = restart_label.get_rect(topleft=(250, 400))

Arrow = pygame.image.load("images/Arrow.png")
Arrow_list = []
Arrow_How = 100
Arrow_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 20)


running = True
while running:
    if gameplay:
        screen.blit(bg, (0, bg_y))
        screen.blit(bg, (0, bg_y - 800))
        Arrow_label_how = Arrow_label.render("You have a " + str(Arrow_How) + " arrow's", False, "Brown")
        screen.blit(Arrow_label_how, (700, 30))

        if n_list_it_the_game:
            for (i, elem) in enumerate (n_list_it_the_game):
                n_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 25)
                n_heal_points = n_label.render("Hp: " + str(elem.hp), False, "green")
                n_armor = n_label.render("Armor: " + str(elem.armor), False, "green")

                if (abs(elem.x - player_x) <= 200) and (abs(elem.y - player_y) <= 200):

                    if elem.x > player_x:
                        screen.blit(Nazgul_attack_left, (elem.x, elem.y))
                        screen.blit(n_heal_points, (elem.x + 10, elem.y - 30))
                        screen.blit(n_armor, (elem.x + 10, elem.y - 60))
                    if elem.x < player_x:
                        screen.blit(Nazgul_attack_right, (elem.x, elem.y))
                        screen.blit(n_heal_points, (elem.x + 10, elem.y - 30))
                        screen.blit(n_armor, (elem.x + 10, elem.y - 60))
                    n_flag = False

                else:
                    n_flag = True

                if elem.x < player_x:
                    elem.x += 2
                    if n_flag:
                        if n_animation_count == 1:
                            n_animation_count = 0
                        else:
                            n_animation_count += 1
                        screen.blit(Nazgul_right[n_animation_count], (elem.x, elem.y))
                        screen.blit(n_heal_points, (elem.x + 10, elem.y - 30))
                        screen.blit(n_armor, (elem.x + 10, elem.y - 60))

                if elem.x > player_x:
                    elem.x -= 2
                    if n_flag:
                        if n_animation_count == 1:
                            n_animation_count = 0
                        else:
                            n_animation_count += 1
                        screen.blit(Nazgul_left[n_animation_count], (elem.x, elem.y))
                        screen.blit(n_heal_points, (elem.x + 10, elem.y - 30))
                        screen.blit(n_armor, (elem.x + 10, elem.y - 60))

                if elem.y < player_y:
                    elem.y += 2

                if elem.y > player_y:
                    elem.y -= 2

                if abs(elem.x - player_x) < 50 and abs(elem.y - player_y) < 50:
                    player_hp -= elem.damage
                    player_y += 150
                    if player_hp <= 0:
                        player_hp = 0
                        gameplay = False

        if flag_animation:
            player_heal_points = player_label.render("Hp: " + str(player_hp), False, "Red")
            if Type_anim == 0:
                screen.blit(Walk_Up[0], (player_x, player_y))
                screen.blit(player_heal_points, (player_x + 20, player_y - 30))
            elif Type_anim == 1:
                screen.blit(Walk_left[0], (player_x, player_y))
                screen.blit(player_heal_points, (player_x + 20, player_y - 30))
            elif Type_anim == 2:
                screen.blit(Walk_right[0], (player_x, player_y))
                screen.blit(player_heal_points, (player_x + 20, player_y - 30))
            elif Type_anim == 3:
                screen.blit(Walk_Down[0], (player_x, player_y))
                screen.blit(player_heal_points, (player_x + 20, player_y - 30))

        flag_animation = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and player_x < 800:
            screen.blit(Walk_right[Player_animation_count], (player_x, player_y))
            player_x += player_speed
            flag_animation = False
            Type_anim = 2

        elif keys[pygame.K_a] and player_x > 0:
            screen.blit(Walk_left[Player_animation_count], (player_x, player_y))
            player_x -= player_speed
            flag_animation = False
            Type_anim = 1

        elif keys[pygame.K_w]:
            screen.blit(Walk_Up[Player_animation_count], (player_x, player_y))
            player_y -= player_speed
            bg_y += 2
            Type_anim = 0
            flag_animation = False
            if player_y < -200:
                player_y = 690

        elif keys[pygame.K_s] and player_y < 700:
            screen.blit(Walk_Down[Player_animation_count], (player_x, player_y))
            player_y += player_speed
            bg_y -= 2
            Type_anim = 3
            flag_animation = False

        if Player_animation_count == 1:
            Player_animation_count = 0

        else:
            Player_animation_count += 1

        if bg_y == 800:
            bg_y = 0

        elif bg_y < 0:
            bg_y = 0

        if Arrow_list:
            for (i, ar) in enumerate(Arrow_list):
                screen.blit(Arrow, (ar.x, ar.y))
                ar.y -= 20

                if n_list_it_the_game:
                    for (j, elem) in enumerate(n_list_it_the_game):
                        if abs(ar.x - elem.x) < 100 and abs(ar.y - elem.y) < 100:
                            elem.y -= 50

                            if elem.armor > 0:
                                elem.armor -= 3
                                if elem.armor < 0:
                                    elem.armor = 0
                            else:
                                elem.hp -= 3

                            if elem.hp <= 0:
                                n_list_it_the_game.pop(j)

                            if Arrow_list:
                              Arrow_list.pop(i)

                        elif ar.y < -100:
                            Arrow_list.pop(i)

    else:
        screen.fill("White")
        screen.blit(loose_label, (250, 500))
        screen.blit(restart_label, (250, 400))
        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed():
            player_y = 500
            n_list_it_the_game.clear()
            Arrow_list.clear()
            gameplay = True

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False
            pygame.quit()

        if event.type == n_timer:
            n_list_it_the_game.append(Nazgul())

        if gameplay and event.type == pygame.KEYDOWN and event.key == pygame.K_r and Arrow_How > 0:
            Arrow_list.append(Arrow.get_rect(topleft=(player_x, player_y - 30)))
            Arrow_How -= 1

    clock.tick(20)
