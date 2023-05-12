import pygame
def convert_list_of_images(a:list,n,m):
    if a==[]:
        return a
    if isinstance(a[0],list):
        return (convert_list_of_images(a[0],n,m)+convert_list_of_images(a[1:],n,m))
    for i in range(len(a)):
        res=pygame.transform.scale(a[i],(a[i].get_width()//n,a[i].get_height()//m))
        a[i]=res
    return a

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

Boss_warg_Up = [pygame.image.load("images/Boss_warg_Up_1.png"),pygame.image.load('images/Boss_warg_Up_2.png')]
Boss_warg_Down = [pygame.image.load("images/Boss_warg_Down_1.png"),pygame.image.load("images/Boss_warg_Down_2.png"),pygame.image.load('images/Boss_warg_Down_3.png')]
Boss_warg_Left =  [pygame.image.load("images/Boss_warg_Left.png"),pygame.image.load("images/Boss_warg_Left_2.png")]
Boss_warg_Right = [pygame.image.load("images/Boss_warg_Right.png"),pygame.image.load("images/Boss_warg_Right_2.png")]
Boss_warg_Heal = [pygame.image.load("images/Boss_warg_Heal_1.png"),pygame.image.load("images/Boss_warg_Heal_2.png"),pygame.image.load("images/Boss_warg_Heal_3.png"),pygame.image.load("images/Boss_warg_Heal_4.png")]

Rings = [pygame.image.load("images/Ring.png"),pygame.image.load("images/Ring_blue.png"),pygame.image.load("images/Ring_Green.png")]
Rings_active = [pygame.image.load("images/Ring_active.png"),pygame.image.load("images/Ring_Blue_active.png"),pygame.image.load("images/Ring_Green_active.png")]
health_model = [pygame.image.load('images/health1.png'), pygame.image.load('images/health2.png'), pygame.image.load('images/health3.png')]
Arrow = [pygame.image.load("images/Arrow_Up.png"),pygame.image.load('images/Arrow_Down.png'), pygame.image.load('images/Arrow_Left.png'),pygame.image.load('images/Arrow_Right.png')]

Boss_warg_picture_list = [Boss_warg_Up,Boss_warg_Down,Boss_warg_Left,Boss_warg_Right,Boss_warg_Heal]
picture_list=[Walk_left,Walk_right,Walk_Up,Walk_Down,Nazgul_left,Nazgul_right,Nazgul_attack]
warg_picture_list =[Warg_Left,Warg_Up,Warg_Right,Warg_Down]
hobba_picture_list=[Hobba_up,Hobba_down,Hobba_right,Hobba_left]
Rings_picture = [Rings,Rings_active]

"""for j in range(len(Arrow)):
    Arrow[j] = pygame.transform.scale(Arrow[j], (Arrow[j].get_width() // 3, Arrow[j].get_height() // 3))
for i in range(len(health_model)):
    health_model[i] = pygame.transform.scale(health_model[i], (health_model[i].get_width() // 2, health_model[i].get_height() // 2))"""
convert_list_of_images(Arrow,3,3)
convert_list_of_images(health_model,2,2)
convert_list_of_images(picture_list,3,3)
convert_list_of_images(warg_picture_list,1/2,1/2)
convert_list_of_images(hobba_picture_list,7,7)
convert_list_of_images(Boss_warg_picture_list,1/4,1/4)
convert_list_of_images(Rings_picture,6,6)
