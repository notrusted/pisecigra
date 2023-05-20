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

boss_nazgul_left = [pygame.image.load("images/nazgul_boss/nazgul_left1.png"),pygame.image.load("images/nazgul_boss/nazgul_left2.png")]
boss_nazgul_right = [pygame.image.load("images/nazgul_boss/nazgul_right1.png"),pygame.image.load("images/nazgul_boss/nazgul_right2.png")]
boss_nazgul_up = [pygame.image.load("images/nazgul_boss/nazgul_up1.png"),pygame.image.load("images/nazgul_boss/nazgul_up2.png")]
boss_nazgul_down = [pygame.image.load("images/nazgul_boss/nazgul_down1.png"),pygame.image.load("images/nazgul_boss/nazgul_down2.png")]
invic_boss_nazgul=[pygame.image.load("images/nazgul_boss/invic.png")]

Rings = [pygame.image.load("images/Ring.png"),pygame.image.load("images/Ring_blue.png"),pygame.image.load("images/Ring_Green.png")]
Rings_active = [pygame.image.load("images/Ring_active.png"),pygame.image.load("images/Ring_Blue_active.png"),pygame.image.load("images/Ring_Green_active.png")]
health_model = [pygame.image.load('images/health/full.png'), pygame.image.load('images/health/half.png'), pygame.image.load('images/health/empty.png')]
Arrow = [pygame.image.load("images/Arrow_Up.png"),pygame.image.load('images/Arrow_Down.png'), pygame.image.load('images/Arrow_Left.png'),pygame.image.load('images/Arrow_Right.png')]

totem_picture=[pygame.image.load('images/totem.png')]

portal_png = [pygame.image.load('images/portal/portal1.png'), pygame.image.load('images/portal/portal2.png'), pygame.image.load('images/portal/portal3.png'), pygame.image.load('images/portal/portal4.png')]

for i in range(len(portal_png)):
    portal_png[i] = pygame.transform.scale(portal_png[i], (portal_png[i].get_width() // 5, portal_png[i].get_height() // 5))

Boss_warg_picture_list = [Boss_warg_Up,Boss_warg_Down,Boss_warg_Left,Boss_warg_Right,Boss_warg_Heal]
picture_list=[Walk_left,Walk_right,Walk_Up,Walk_Down,Nazgul_left,Nazgul_right,Nazgul_attack]
warg_picture_list =[Warg_Left,Warg_Up,Warg_Right,Warg_Down]
hobba_picture_list=[Hobba_up,Hobba_down,Hobba_right,Hobba_left]
Rings_picture = [Rings,Rings_active]
boss_nazgul_picture_list=[boss_nazgul_up,boss_nazgul_left,boss_nazgul_down,boss_nazgul_right]
screen_saver = pygame.image.load('images/Back/Back.jpg')
screen_saver = pygame.transform.scale(screen_saver, (1000, 800))

protectiveDome = pygame.image.load("images/orcs/protective_dome.png")
protectiveDome = pygame.transform.scale(protectiveDome, (protectiveDome.get_width() // 3, protectiveDome.get_height() // 3))

button_play_up = pygame.image.load('images/buttons/play.png')
button_play_down = pygame.image.load('images/buttons/play_pressed.png')

button_options_up = pygame.image.load('images/buttons/options.png')
button_options_down = pygame.image.load('images/buttons/options_pressed.png')

button_quit_up = pygame.image.load('images/buttons/quit.png')
button_quit_down = pygame.image.load('images/buttons/quit_pressed.png')

button_R = pygame.image.load('images/buttons/R.png')

Punch_list = [pygame.image.load("images/Punch_1.png"),pygame.image.load("images/Punch_2.png"),pygame.image.load("images/Punch_3.png")]


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
convert_list_of_images(boss_nazgul_picture_list,1/3,1/3)
convert_list_of_images(totem_picture,3,3)
convert_list_of_images(Punch_list,1/2,1/2)
#convert_list_of_images(invic_boss_nazgul,1/3,1/3)



