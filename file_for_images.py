import pygame
def convert_list_of_images(a:list,n,m):
    for i in range(len(a)):
        for j in range(len(a[i])):
            res=pygame.transform.scale(a[i][j],(a[i][j].get_width()//n,a[i][j].get_height()//m))
            a[i][j]=res
Walk_right = [pygame.image.load('images/Right-1.png'),pygame.image.load('images/Right-2.png')]
Walk_left = [pygame.image.load('images/Left-1.png'),pygame.image.load('images/Left-2.png')]
Walk_Up = [pygame.image.load('images/Up-1.png'),pygame.image.load("images/Up-2.png")]
Walk_Down = [pygame.image.load('images/Down_-_1.png'),pygame.image.load('images/Down-2.png')]

Elf_left=[pygame.image.load("images/elf/elf_left.png"),pygame.image.load("images/elf/elf_left1.png")]
Elf_right=[pygame.image.load("images/elf/elf_right.png"),pygame.image.load("images/elf/elf_right1.png")]
Elf_up=[pygame.image.load("images/elf/elf_up.png"),pygame.image.load("images/elf/elf_up1.png")]
Elf_down=[pygame.image.load("images/elf/elf_down.png"),pygame.image.load("images/elf/elf_down1.png")]

Hobba_left=[pygame.image.load("images/hobba/hobba_left3.png"),pygame.image.load("images/hobba/hobba_left1.png")]
Hobba_right=[pygame.image.load("images/hobba/hobba_right3.png"),pygame.image.load("images/hobba/hobba_right1.png")]
Hobba_up=[pygame.image.load("images/hobba/hobba_up1.png"),pygame.image.load("images/hobba/hobba_up2.png"),pygame.image.load("images/hobba/hobba_up3.png")]
Hobba_down=[pygame.image.load("images/hobba/hobba_down1.png"),pygame.image.load("images/hobba/hobba_down2.png"),pygame.image.load("images/hobba/hobba_down3.png")]

Nazgul_right = [pygame.image.load("images/Nazgul-2-1.png"),pygame.image.load("images/Nazgul-2-1-right-eyes.png")]
Nazgul_left = [pygame.image.load("images/Nazgul-2-1-left.png"),pygame.image.load("images/Nazgul-2-1-left-eyes.png")]
"""Nazgul_attack_left = pygame.image.load("images/Nazgul-3-left.png")
Nazgul_attack_right = pygame.image.load("images/Nazgul-3-rigt.png")"""
Nazgul_attack =[pygame.image.load("images/Nazgul-3-left.png"),pygame.image.load("images/Nazgul-3-rigt.png")]

Orc_right = [pygame.image.load('images/orcs/orc_right1.png'), pygame.image.load('images/orcs/orc_right2.png'), pygame.image.load('images/orcs/orc_right3.png')]
Orc_left = [pygame.image.load('images/orcs/orc_left1.png'), pygame.image.load('images/orcs/orc_left2.png'), pygame.image.load('images/orcs/orc_left3.png')]
Orc_up = [pygame.image.load('images/orcs/orc_up1.png'), pygame.image.load('images/orcs/orc_up2.png'), pygame.image.load('images/orcs/orc_up3.png')]
Orc_down = [pygame.image.load('images/orcs/orc_down1.png'), pygame.image.load('images/orcs/orc_down2.png'), pygame.image.load('images/orcs/orc_stay.png')]

Orc_conqueror_right = [pygame.image.load('images/orcs/orc_conqueror_right1.png'),pygame.image.load('images/orcs/orc_conqueror_right2.png'),pygame.image.load('images/orcs/orc_conqueror_right3.png')]
Orc_conqueror_left = [pygame.image.load('images/orcs/orc_conqueror_left1.png'),pygame.image.load('images/orcs/orc_conqueror_left2.png'),pygame.image.load('images/orcs/orc_conqueror_left3.png')]
Orc_conqueror_up = [pygame.image.load('images/orcs/orc_conqueror_up1.png'),pygame.image.load('images/orcs/orc_conqueror_up2.png'),pygame.image.load('images/orcs/orc_conqueror_up3.png')]
Orc_conqueror_down = [pygame.image.load('images/orcs/orc_conqueror_down1.png'),pygame.image.load('images/orcs/orc_conqueror_down2.png'),pygame.image.load('images/orcs/orc_conqueror_down3.png')]

Warg_Up = [pygame.image.load("images/Warg_Up_1.png"),pygame.image.load("images/Warg_Up_2.png")]
Warg_Down = [pygame.image.load("images/Warg_Down_1.png"),pygame.image.load("images/Warg_Down_2.png"),pygame.image.load('images/Warg_Down_3.png')]
Warg_Left = [pygame.image.load("images/Warg_Left_1.png"),pygame.image.load("images/Warg_Left_2.png")]
Warg_Right = [pygame.image.load("images/Warg_Right_1.png"),pygame.image.load("images/Warg_Right_2.png")]
picture_list=[Walk_left,Walk_right,Walk_Up,Walk_Down,Nazgul_left,Nazgul_right,Nazgul_attack]
warg_picture_list =[Warg_Left,Warg_Up,Warg_Right,Warg_Down]
hobba_picture_list=[Hobba_up,Hobba_down,Hobba_right,Hobba_left]
hobba_picture_list=convert_list_of_images(hobba_picture_list,7,7)
health_model = [pygame.image.load('images/health1.png'), pygame.image.load('images/health2.png'), pygame.image.load('images/health3.png')]

Arrow = [pygame.image.load("images/Arrow_Up.png"),pygame.image.load('images/Arrow_Down.png'), pygame.image.load('images/Arrow_Left.png'),pygame.image.load('images/Arrow_Right.png')]
for j in range(len(Arrow)):
    Arrow[j] = pygame.transform.scale(Arrow[j], (Arrow[j].get_width() // 3, Arrow[j].get_height() // 3))
for i in range(len(health_model)):
    health_model[i] = pygame.transform.scale(health_model[i], (health_model[i].get_width() // 2, health_model[i].get_height() // 2))
picture_list=convert_list_of_images(picture_list,3,3)
warg_picture_list=convert_list_of_images(warg_picture_list,1/2,1/2)
