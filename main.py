import pygame
from random import randint


#---------------------------------------------------
"""
Некит - текстуры player, всех мобов + подогнать, попробовать сделать арену
Юра - волк (класс)
Илья - орк (класс)


!!!!!!
*как-то реализовать protect персонажа player
*можно сделать тролля
"""
#---------------------------------------------------


bonus_attack = 0
flag_ability = 1

class Character():
    count_animation=0
    def __init__(self,Hp, Strong, Ability, Weapon, list_animation: list):
        self.strong = Strong
        self.hp = Hp
        self.ability = Ability
        self.weapon = Weapon
        self.la = list_animation
    def Attack(self):
        return (self.strong + self.weapon.damage)

    def Protect(self):
        print('Try to Protect')
        print()

    def Use_the_Ability(self):
        print("use ability: ", self.ability)
        print()
    def animation(self,surf: pygame.surface.Surface, symbol: str, x,y):
        if Character.count_animation == 0:
            Character.count_animation = 1
        else:
            Character.count_animation = 0
        if symbol == "l":
            ch = 0
        elif symbol == "r":
            ch = 1
        elif symbol == "u":
            ch = 2
        elif symbol == "d":
            ch = 3
        surf.blit(self.la[ch][Character.count_animation], (x, y))

    def Player_coordinate(self):
        return (player_x,player_y)

class Elf(Character):

    def __init__(self):
        Character.__init__(self,90,30, "has agility",Weapon("Bow",30),[Walk_left,Walk_right,Walk_Up,Walk_Down])


    def Attack(self):
        print("The Elf attack with damage", self.strong + self.weapon.damage)
        return self.strong + self.weapon.damage

    def Protect(self):
        a =  5 * randint(0,1)
        self.hp = self.hp + a
        print("The Elf's protect give him a " + str(a) + " Hp")

    def Use_the_Ability(self):
        global flag_ability,Arrow_How
        if flag_ability != 0:
            print("The Elf try to use him agility")
            Arrow_How += 15
        flag_ability = 0


class Human(Character):

    def __init__(self):
        Character.__init__(self,150,40, "is a tracker", Weapon("sword", 15),[Walk_left,Walk_right,Walk_Up,Walk_Down])

    def Attack(self):
        global bonus_attack
        print("The Human attack with damage", self.strong + bonus_attack + self.weapon.damage)
        a = self.strong + bonus_attack + self.weapon.damage
        bonus_attack = 0
        return a

    def Protect(self):
        a = randint(0, 1)
        self.hp = self.hp + a * 15
        print("the Human's protect give him a  " + str(a * 15) + " Hp")

    def Use_the_Ability(self):
        global flag_ability, bonus_attack
        if flag_ability != 0:
            print('The Human Find the vulnerability')
            bonus_attack += randint(20,35)
        flag_ability = 0

class Hobbit(Character):

    def __init__(self):
        Character.__init__(self,50,70, 'can a hide', Weapon('Arnors knife', 15),[Walk_left,Walk_right,Walk_Up,Walk_Down])

    def Attack(self):
        print( "The Hobbit attack with damage", self.strong + self.weapon.damage)
        return self.strong + self.weapon.damage

    def Protect(self):
        a = randint(0,1) * randint(1,5) * 5
        self.hp = self.hp + a
        print("The Hobbit's  protect give him a " + str(a) +' Hp')

    def Use_the_Ability(self):
        global flag_ability
        if flag_ability != 0:
            print( " The Hobbit was able to hide")
            self.hp += 15
        flag_ability = 0



class Weapon:
    def __init__(self, Name, Damage):
        self.name = Name
        self.damage = Damage


class Monster:
    def __init__(self, Hp, Armor, X,Y, Damage, Weapon,):#надо найти текстуры как для персонажа (list_animation)
        self.hp = Hp
        self.armor = Armor
        self.damage = Damage
        self.weapon = Weapon
        self.x = X
        self.y = Y
        #self.la=list_animation

    def Attack(self):
        return self.damage + self.weapon.damage

    def Protect(self, dmg):
        a = randint(0, 1)
        self.hp = self.hp - dmg + dmg * a * a
    """def animation(self,surf: pygame.surface.Surface, symbol: str, x,y):
        if Character.count_animation==0:
            Character.count_animation=1
        else:
            Character.count_animation=0
        if symbol=="l":
            ch=0
        elif symbol=="r":
            ch=1
        elif symbol=="u":
            ch=2
        elif symbol=="d":
            ch=3
        surf.blit(self.la[ch][Character.count_animation],(x,y))"""


class Nazgul(Monster):
    def __init__(self,anim):
        self.anim = anim
        Monster.__init__(self, randint(20, 50),  randint(5, 20), 250,-100,randint(1,15),Weapon("Morgul's knife",randint(5,10)))


    def Attack(self):
        print('Nazgul attack with damage', self.damage + self.weapon.damage)
        return self.damage + self.weapon.damage

    def Protect(self, dmg):
        print('Nazgul try to protect')
        b = dmg
        self.hp = self.hp - dmg + (b * randint(0, 1) * randint(0, 1))

class Ork(Monster):

    def __int__(self):
        Monster.__init__(self, randint(50, 70), randint(1, 10), 1, 250, randint(15, 20), Weapon("Dubina", randint(10, 20)))

    def Attack(self):
        print('Ork attack with damage', self.damage + self.weapon.damage)
        return self.damage+ self.weapon.damage

    def Protect(self, dmg):
        self.hp -= dmg


class Warg(Monster):
    def __init__(self,anim):
        self.anim = anim
        Monster.__init__(self, randint(30, 90), randint(0, 20), 250, -100, randint(5, 15), Weapon('claws', randint(10,15)))

    def Attack(self):
        print('The Warg Attack with damage', self.damage + self.weapon.damage)
        return self.damage + self.weapon.damage

    def Protect(self, dmg):
        print('The Warg try to protect')
        a = randint(0, 1)
        b = dmg

        self.hp = self.hp - dmg + (b * a)



clock = pygame.time.Clock()


pygame.init()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("The Hobbit: Pyton's Adventure")
#icon = pygame.image.load("I-ICON.png")
#pygame.display.set_icon(icon)
# ---Подключение изображений--------------------------------------------------------------
bg = pygame.image.load("images/Back.png")
bg = pygame.transform.scale(bg,(1000,800))
#player = pygame.image.load("I-ICON.png")

Walk_right = [pygame.image.load('images/Right-1.png'),pygame.image.load('images/Right-2.png')]
Walk_left  = [pygame.image.load('images/Left-1.png'),pygame.image.load('images/Left-2.png')]
Walk_Up = [pygame.image.load('images/Up-1.png'),pygame.image.load("images/Up-2.png")]
Walk_Down = [pygame.image.load('images/Down_-_1.png'),pygame.image.load('images/Down-2.png')]

Nazgul_right = [pygame.image.load("images/Nazgul-2-1.png"),pygame.image.load("images/Nazgul-2-1-right-eyes.png")]
Nazgul_left = [pygame.image.load("images/Nazgul-2-1-left.png"),pygame.image.load("images/Nazgul-2-1-left-eyes.png")]
"""Nazgul_attack_left = pygame.image.load("images/Nazgul-3-left.png")
Nazgul_attack_right = pygame.image.load("images/Nazgul-3-rigt.png")"""
Arrow = pygame.image.load("images/Arrow.png")
Nazgul_attack=[pygame.image.load("images/Nazgul-3-left.png"),pygame.image.load("images/Nazgul-3-rigt.png")]

Orc_right = [pygame.image.load('images/orcs/orc_right1.png'), pygame.image.load('images/orcs/orc_right2.png'), pygame.image.load('images/orcs/orc_right3.png')]
Orc_left = [pygame.image.load('images/orcs/orc_left1.png'), pygame.image.load('images/orcs/orc_left2.png'), pygame.image.load('images/orcs/orc_left3.png')]
Orc_up = [pygame.image.load('images/orcs/orc_up1.png'), pygame.image.load('images/orcs/orc_up2.png'), pygame.image.load('images/orcs/orc_up3.png')]
Orc_down = [pygame.image.load('images/orcs/orc_down1.png'), pygame.image.load('images/orcs/orc_down2.png'), pygame.image.load('images/orcs/orc_stay.png')]

Warg_Up = [pygame.image.load("images/Warg_Up_1.png"),pygame.image.load("images/Warg_Up_2.png")]
Warg_Down = [pygame.image.load("images/Warg_Down_1.png"),pygame.image.load("images/Warg_Down_2.png"),pygame.image.load('images/Warg_Down_3.png')]
Warg_Left = [pygame.image.load("images/Warg_Left_1.png"),pygame.image.load("images/Warg_Left_2.png")]
Warg_Right = [pygame.image.load("images/Warg_Right_1.png"),pygame.image.load("images/Warg_Right_2.png")]
picture_list=[Walk_left,Walk_right,Walk_Up,Walk_Down,Nazgul_left,Nazgul_right,Nazgul_attack]



for i in range(len(picture_list)):
    for j in range(len(picture_list[i])):
        a=pygame.transform.scale(picture_list[i][j],(picture_list[i][j].get_width()//3,picture_list[i][j].get_height()//3))
        picture_list[i][j]=a
warg_picture_list =[Warg_Left,Warg_Up,Warg_Right,Warg_Down]
for i in range(len(warg_picture_list)):
    for j in range(len(warg_picture_list[i])):
        b = pygame.transform.scale(warg_picture_list[i][j],(warg_picture_list[i][j].get_width()* 2,warg_picture_list[i][j].get_height()*2))
        warg_picture_list[i][j] = b



#---------------------------------------------------------------------------------------------



n_flag = True
n_timer = pygame.USEREVENT + 1
pygame.time.set_timer(n_timer,10000)
n_list_it_the_game = []


warg_flag1 = True
warg_flag2 = False
warg_flag3 = False
warg_flag4 = False
warg_list_in_the_game = []



Player_animation_count = 0
bg_y = 0




player_speed = 15
player_x = 300
player_y = 250
flag_animation = True
Type_anim = 0

gameplay = True

#---Подключение шрифтов----------------------------------------------------
player_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 30)
the_end_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 50)
loose_label = the_end_label.render('You died', False, (12, 12, 12))
restart_label = the_end_label.render("Start again", False, (35, 234, 32))
restart_label_rect = restart_label.get_rect(topleft=(250, 400))
Arrow_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 20)
#--------------------------------------------------------------------------

Arrow_list = []
Arrow_How = 0
Attack_point = 0


Start_game_flag = True
entr = False #флаг на переключение экранов стартовый->выбор игрока


running = True
while running:
    #---Стартовый экран-------------------------------------------------------
    if Start_game_flag:
        gameplay = False
        screen.fill("Black")
        label = pygame.font.Font('fonts/RobotoMono-VariableFont_wght.ttf', 20)
        Game_Name = label.render("The Hobbit: Pyton's Adventure", False, "Yellow")
        screen.blit(Game_Name,(250,400))
        Game_start = label.render("Press any to start...", False, "Yellow")
        screen.blit(Game_start, (250, 600))
    #-------------------------------------------------------------------------

    #---экран выбора героя----------------------------------------------------
        if entr:
            screen.fill("Black")
            Character_label = label.render("Choose your hero:", False, "Red")
            screen.blit(Character_label, (250, 200))
            Character_label_Elf = label.render("Forest Elf", False, "Yellow")
            screen.blit(Character_label_Elf, (250, 400))
            Character_label_Human = label.render("Human", False, "Yellow")
            screen.blit(Character_label_Human, (250, 500))
            Character_label_Hobbit = label.render("Hobbit", False, "Yellow")
            screen.blit(Character_label_Hobbit, (250, 600))

            Character_label_Elf_rect = Character_label_Elf.get_rect(topleft=(250, 400))
            Character_label_Human_rect = Character_label_Human.get_rect(topleft=(250, 500))
            Character_label_Hobbit_rect = Character_label_Hobbit.get_rect(topleft=(250, 600))

            mouse = pygame.mouse.get_pos()
            #реализация этого выбора
            if Character_label_Elf_rect.collidepoint(mouse) and pygame.mouse.get_pressed():
                gameplay = True
                print("Your choose is Elf")
                player_character = Elf()
                All_Hp = player_character.hp
                Arrow_How = 100
                Start_game_flag = False

            elif Character_label_Human_rect.collidepoint(mouse) and pygame.mouse.get_pressed():
                gameplay = True
                print("Your choose is Human")
                player_character = Human()
                All_Hp = player_character.hp
                Start_game_flag = False

            elif Character_label_Hobbit_rect.collidepoint(mouse) and pygame.mouse.get_pressed():
                gameplay = True
                print("Your choose is Hobbit")
                player_character = Hobbit()
                All_Hp = player_character.hp
                Start_game_flag = False


    #---процесс геймплея(арена)-------------------------------------------------------------------
    if gameplay :
        screen.blit(bg, (0, bg_y))
        screen.blit(bg, (0, bg_y - 800))
        if player_character.ability == "has agility":
            Arrow_label_how = Arrow_label.render("You have a " + str(Arrow_How) + " arrow's", False, "Brown")
            Arrow_label_press = Arrow_label.render("Press R...",False,"Brown")
            Character_label_Elf_ability = Arrow_label.render("You can" + (1 - flag_ability) * "'t" + " use " + "The ability: " +
                                                             str(player_character.ability), False, 'Brown')
            screen.blit(Arrow_label_how, (700, 30))
            screen.blit(Arrow_label_press, (700, 60))
            screen.blit(Character_label_Elf_ability, (500, 750))

        else:
            Arrow_label_how = Arrow_label.render("You can touch with  " + str(player_character.weapon.name), False, "Brown")
            Arrow_label_press = Arrow_label.render("Press F...", False, "Brown")
            Character_label_Hobbit_and_Human_ability = Arrow_label.render(
                "You can" + (1 - flag_ability) * "'t" + " use " + "The ability: " + str(player_character.ability),
                False, 'Brown')
            screen.blit(Arrow_label_how, (600, 30))
            screen.blit(Arrow_label_press, (600, 60))
            screen.blit(Character_label_Hobbit_and_Human_ability, (500, 750))

        #---реализация поведения и движения мобов-------------------------------------------

        if warg_list_in_the_game:
            for(i,elem1) in enumerate(warg_list_in_the_game):
                warg_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf",25)
                warg_heal_points = warg_label.render("Hp: " + str(elem1.hp),False,"green")
                warg_armor = warg_label.render("Armor: " + str(elem1.armor),False,"green")

                if warg_flag1 and elem1.y <= 1100:
                    elem1.y += 15

                    elem1.anim += 1
                    screen.blit(Warg_Down[elem1.anim % 3],(elem1.x,elem1.y))
                    screen.blit(warg_heal_points, (elem1.x + 10, elem1.y - 30))
                    screen.blit(warg_armor, (elem1.x + 10, elem1.y - 60))

                if elem1.y > 1100 and warg_flag1:
                    a = player_character.Player_coordinate()
                    elem1.x = -100
                    elem1.y = a[1]
                    warg_flag1 = False
                    warg_flag2 = True

                if warg_flag2 and elem1.x <= 900:
                    elem1.x += 15

                    elem1.anim += 1
                    screen.blit(Warg_Right[elem1.anim % 2],(elem1.x,elem1.y))
                    screen.blit(warg_heal_points, (elem1.x + 10, elem1.y - 30))
                    screen.blit(warg_armor, (elem1.x + 10, elem1.y - 60))

                if elem1.x > 900 and warg_flag2:
                    a = player_character.Player_coordinate()
                    elem1.x = a[0]
                    elem1.y = 1100
                    warg_flag2 = False
                    warg_flag3 = True

                if warg_flag3 and elem1.y >= -100 :
                    elem1.y -= 15

                    elem1.anim += 1
                    screen.blit(Warg_Up[elem1.anim % 2], (elem1.x, elem1.y))
                    screen.blit(warg_heal_points, (elem1.x + 10, elem1.y - 30))
                    screen.blit(warg_armor, (elem1.x + 10, elem1.y - 60))

                if elem1.y < -100 and warg_flag3:
                    a = player_character.Player_coordinate()
                    elem1.x = 900
                    elem1.y = a[1]
                    warg_flag3 = False
                    warg_flag4 = True

                if warg_flag4 and elem1.x >= -100:
                    elem1.x -= 15


                    elem1.anim += 1
                    screen.blit(Warg_Left[elem1.anim % 2], (elem1.x, elem1.y))
                    screen.blit(warg_heal_points, (elem1.x + 10, elem1.y - 30))
                    screen.blit(warg_armor, (elem1.x + 10, elem1.y - 60))

                if elem1.x < -100 and warg_flag4:
                    a = player_character.Player_coordinate()
                    elem1.x = a[0]
                    elem1.y = -100
                    warg_flag4 = False
                    warg_flag1 = True

                if abs(elem1.x - player_x) < 50 and abs(elem1.y - player_y) < 50:
                    player_character.hp -= elem1.Attack()

                    if player_x > elem1.x:
                        player_x -= 50



                    elif player_x < elem1.x :
                        player_x += 50



                    if player_y < elem1.y:
                        player_y += 50

                    elif player_y > elem1.y:
                        player_y -= 50

                    if player_character.hp <= 0:
                        player_character.hp = 0
                        gameplay = False


        if n_list_it_the_game:
            for (i, elem) in enumerate(n_list_it_the_game):
                n_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 25)
                n_heal_points = n_label.render("Hp: " + str(elem.hp), False, "green")
                n_armor = n_label.render("Armor: " + str(elem.armor), False, "green")

                if (abs(elem.x - player_x) <= 200) and (abs(elem.y - player_y) <= 200):

                    if elem.x >= player_x:
                        screen.blit(Nazgul_attack[0], (elem.x, elem.y))
                        screen.blit(n_heal_points, (elem.x + 10, elem.y - 30))
                        screen.blit(n_armor,(elem.x + 10, elem.y - 60))
                    if elem.x < player_x:
                        screen.blit(Nazgul_attack[1], (elem.x, elem.y))
                        screen.blit(n_heal_points, (elem.x + 10, elem.y - 30))
                        screen.blit(n_armor, (elem.x + 10, elem.y - 60))
                    n_flag = False

                else:
                    n_flag = True

                if elem.x < player_x:
                    elem.x += 2
                    if n_flag:

                        elem.anim += 1
                        screen.blit(Nazgul_right[elem.anim % 2], (elem.x, elem.y))
                        screen.blit(n_heal_points, (elem.x + 10, elem.y - 30))
                        screen.blit(n_armor, (elem.x + 10, elem.y - 60))

                if elem.x > player_x:
                    elem.x -= 2
                    if n_flag:

                        elem.anim += 1
                        screen.blit(Nazgul_left[elem.anim % 2], (elem.x, elem.y))
                        screen.blit(n_heal_points, (elem.x + 10, elem.y - 30))
                        screen.blit(n_armor, (elem.x + 10, elem.y - 60))

                if elem.y < player_y:
                    elem.y += 2

                if elem.y > player_y:
                    elem.y -= 2

                if abs(elem.x - player_x) < 50 and abs(elem.y - player_y) < 50:
                    player_character.hp -= elem.Attack()
                    player_y += 150
                    if player_character.hp <= 0:
                        player_character.hp = 0
                        gameplay = False


#---перс при бездействии-------------------------------------------
        if flag_animation:
            player_heal_points = player_label.render("Hp: " + str(player_character.hp), False, "Red")
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
#---анимация персонажа-------------------------------------------
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and player_x < 800:
            player_character.animation(screen, "r", player_x, player_y)
            player_x += player_speed
            flag_animation = False
            Type_anim = 2

        elif keys[pygame.K_a] and player_x > 0:
            player_character.animation(screen, "l", player_x, player_y)
            player_x -= player_speed
            flag_animation = False
            Type_anim = 1

        elif keys[pygame.K_w]:
            player_character.animation(screen, "u", player_x, player_y)
            player_y -= player_speed
            bg_y += 2
            Type_anim = 0
            flag_animation = False
            if player_y < -200:
                player_y = 690

        elif keys[pygame.K_s] and player_y < 700:
            player_character.animation(screen, "d", player_x, player_y)
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
                                elem.armor -= Attack_point
                                if elem.armor < 0:
                                    elem.armor = 0
                            else:
                                elem.Protect(Attack_point)

                            if elem.hp <= 0:
                                n_list_it_the_game.pop(j)
                                print("the Nazgul is murdered...")
                                flag_ability = 1

                            if Arrow_list:
                              Arrow_list.pop(i)

                        if Arrow_list:
                           if ar.y < -100:
                              Arrow_list.pop(i)

                if warg_list_in_the_game:
                    for (j1,elem1) in enumerate(warg_list_in_the_game):
                        if abs(ar.x - elem1.x) < 100 and abs(ar.y - elem1.y) < 100:
                            elem1.y -= 50

                            if elem1.armor > 0:
                                elem1.armor -= Attack_point
                                if elem1.armor < 0:
                                    elem1.armor = 0
                            else:
                                elem1.Protect(Attack_point)

                            if elem1.hp <= 0:
                                warg_list_in_the_game.pop(j1)
                                print("the Warg is murdered...")
                                flag_ability = 1

                            if Arrow_list:
                                Arrow_list.pop(i)



    elif Start_game_flag == False:
        screen.fill("White")
        screen.blit(loose_label, (250, 500))
        screen.blit(restart_label, (250, 400))
        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed():
            player_y = 500
            n_list_it_the_game.clear()
            warg_list_in_the_game.clear()
            Arrow_list.clear()
            player_character.hp = All_Hp
            flag_ability = 1
            Arrow_How = 0
            Start_game_flag = True

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == n_timer:
            n_list_it_the_game.append(Nazgul(0))

        if event.type == n_timer:
            warg_list_in_the_game.append(Warg(0))

        if gameplay and event.type == pygame.KEYDOWN and event.key == pygame.K_r and Arrow_How > 0 and player_character.ability == "has agility":
            Arrow_list.append(Arrow.get_rect(topleft=(player_x, player_y - 30)))
            Arrow_How -= 1
            Attack_point = player_character.Attack()

        if Start_game_flag and event.type == pygame.KEYDOWN:
            entr = True

        if gameplay and (player_character.ability == "is a tracker" or player_character.ability == "can a hide") and event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            a = player_character.Attack()
            if Attack_point <= a:
                Attack_point = a
            if n_list_it_the_game:
                for (j,elem) in enumerate(n_list_it_the_game):
                    if abs(elem.x - player_x) < 70 and abs(elem.y - player_y) < 70:
                        elem.y -= 100

                        if elem.armor > 0:
                            elem.armor -= Attack_point
                            if elem.armor < 0:
                                elem.armor = 0
                        else:
                            elem.Protect(Attack_point)

                        Attack_point = 0

                        if elem.hp <= 0:
                            n_list_it_the_game.pop(j)
                            print("the Nazgul is murdered...")
                            flag_ability = 1


            if warg_list_in_the_game:
                for (j1,elem1) in enumerate(warg_list_in_the_game):
                    if abs(elem1.x - player_x) < 70 and abs(elem1.y - player_y) < 70:
                        elem1.y -= 100

                        if elem1.armor > 0:
                            elem1.armor -= Attack_point
                            if elem1.armor < 0:
                                elem1.armor = 0
                        else:
                            elem1.Protect(Attack_point)

                        Attack_point = 0

                        if elem1.hp <= 0:
                            warg_list_in_the_game.pop(j1)
                            print("the Warg is murdered...")
                            flag_ability = 1


        if gameplay and event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            player_character.Use_the_Ability()

    clock.tick(20)