import pygame
from random import randint
from file_for_images import *

#---------------------------------------------------
"""
Некит - музыка, текстуры, босс Назгул
Юра - босс волк, меню
Илья - босс орк, + магия для босса + магия для персонажа
абстраткный класс босса-?????????????
"""
#---------------------------------------------------

bonus_attack = 0
flag_ability = 1


# ---КЛАССЫ--------------------------------------------------------------------------------------------
class Character():
    count_animation = 0

    def __init__(self, Hp, Strong, Ability, Weapon, list_animation: list):
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

    def animation(self, surf: pygame.surface.Surface, symbol: str, x, y):
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
        return (player_x, player_y)

class Elf(Character):

    def __init__(self):
        Character.__init__(self,90,30, "has agility",Weapon("Bow",30),[Elf_left,Elf_right,Elf_up,Elf_down])

    def Attack(self):
        print("The Elf attack with damage", self.strong + self.weapon.damage)
        return self.strong + self.weapon.damage

    def Protect(self):
        a = 5 * randint(0, 1)
        self.hp = self.hp + a
        print("The Elf's protect give him a " + str(a) + " Hp")

    def Use_the_Ability(self):
        global flag_ability, Arrow_How
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
            bonus_attack += randint(20, 35)
        flag_ability = 0

class Hobbit(Character):

    def __init__(self):
        Character.__init__(self,50,70, 'can a hide', Weapon('Arnors knife', 15),[Hobba_left,Hobba_right,Hobba_up,Hobba_down])

    def Attack(self):
        print("The Hobbit attack with damage", self.strong + self.weapon.damage)
        return self.strong + self.weapon.damage

    def Protect(self):
        a = randint(0, 1) * randint(1, 5) * 5
        self.hp = self.hp + a
        print("The Hobbit's  protect give him a " + str(a) + ' Hp')

    def Use_the_Ability(self):
        global flag_ability
        if flag_ability != 0:
            print(" The Hobbit was able to hide")
            self.hp += 15
        flag_ability = 0

class Weapon:
    def __init__(self, Name, Damage):
        self.name = Name
        self.damage = Damage

class Magic:
    def __init__(self, name, dmg):
        self.name = name
        self.damage = dmg


class Monster:
    def __init__(self, Hp, Armor, X, Y, Damage, Weapon, anim):  # надо найти текстуры как для персонажа (list_animation)
        self.anim = anim
        self.hp = Hp
        self.armor = Armor
        self.damage = Damage
        self.weapon = Weapon
        self.x = X
        self.y = Y
        # self.la=list_animation

    def Attack(self):
        return self.damage + self.weapon.damage

    def Protect(self, dmg):
        a = randint(0, 1)
        self.hp = self.hp - dmg + dmg * a * a


class Nazgul(Monster):
    def __init__(self, anim):
        self.anim = anim
        Monster.__init__(self, randint(20, 50), randint(5, 20), 250, -100, randint(1, 15),
                         Weapon("Morgul's knife", randint(5, 10)), 0)

    def Attack(self):
        print('Nazgul attack with damage', self.damage + self.weapon.damage)
        return self.damage + self.weapon.damage

    def Protect(self, dmg):
        print('Nazgul try to protect')
        b = dmg
        self.hp = self.hp - dmg + (b * randint(0, 1) * randint(0, 1))


class Warg(Monster):
    def __init__(self,flag1,flag2,flag3,flag4):
        self.flag1 = flag1
        self.flag2 = flag2
        self.flag3 = flag3
        self.flag4 = flag4
        Monster.__init__(self, randint(30, 90), randint(0, 20), 250, -100, randint(5, 15),
                         Weapon('claws', randint(10, 15)), 0)

    def Attack(self):
        print('The Warg Attack with damage', self.damage + self.weapon.damage)
        return self.damage + self.weapon.damage

    def Protect(self, dmg):
        print('The Warg try to protect')
        a = randint(0, 1)
        b = dmg

        self.hp = self.hp - dmg + (b * a)


class Ork(Monster):
    def __init__(self, anim):
        self.anim = anim
        Monster.__init__(self, randint(50, 100), randint(1, 20), 0, 0, randint(20, 50),
                         Weapon("Pushka", randint(5, 100)), 0)

    def Attack(self):
        print('Ork attack with damage', self.damage + self.weapon.damage)
        return self.damage + self.weapon.damage

    def Protect(self, dmg):
        print('Ork try to protect')
        b = dmg
        self.hp = self.hp - dmg + (b * randint(0, 1) * randint(0, 1))


class Boss:
    def __init__(self, hp, armor, dmg, weapon, utility):
        self.hp = hp
        self.armor = armor
        self.dmg = dmg
        self.weapon = weapon
        self.utility = utility

    def base_attack(self):
        return self.dmg


class BossOrkConqueror(Boss):
    def __init__(self, hp, armor, dmg, weapon, magic, cry, coord_x, coord_y, heal_boss):
        Boss.__init__(self, hp, armor, dmg, weapon, magic)
        self.cry = cry
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.heal = heal_boss
        self.flag_go_to_center = True
        self.anim = 0
        self.flag_orc_cry = True
        self.flag_boss_to_heal = True

    def healing(self):
        if self.heal > 0:
            self.heal -= 1
            self.heal += 100

    def standart_attack(self):
        return self.dmg + self.weapon.damage


class Boss_warg(Boss):
    def __init__(self,x,y,anim):
        self.anim = anim
        self.x = x
        self.y = y
        Boss.__init__(self,250,50,30,Weapon("Bloody claws",70),Magic('Growl',5,))

    def base_attack(self):
        print('The Alpha Warg attack with damage', self.dmg + self.weapon.damage)
        return self.dmg + self.weapon.damage

    def special_ability(self):
        print('The Alpha Warg try to heal...')
        warg_list_in_the_game.append(Warg(True,False,False,False))
        self.hp += 20



    def Protect(self,dmg):
        print('The Alpha Warg try dto protect')
        b = dmg * randint(0,1) * randint(0,1)
        if b != 0:
            self.hp += 15
        self.hp = self.hp - dmg + b







#--------------------------------------------------------------------------------------------
def convert_list_of_images(a:list,n,m):
    for i in range(len(a)):
        for j in range(len(a[i])):
            res=pygame.transform.scale(a[i][j],(a[i][j].get_width()//n,a[i][j].get_height()//m))
            a[i][j]=res
#--- функции механики перемещения мобов ------------------ddw----------------------------------------------
def orc_mechanicks_go():
    global player_x, player_y, orc_list_in_the_game, orc_flag, gameplay
    if orc_list_in_the_game:
        for (i, elem) in enumerate(orc_list_in_the_game):
            orc_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 25)
            orc_heal_points = orc_label.render("Hp: " + str(elem.hp), False, "green")
            orc_armor = orc_label.render("Armor: " + str(elem.armor), False, "green")

            if abs(elem.x - player_x) <= 60 and abs(elem.y - player_y) <= 60:
                player_character.hp -= elem.Attack()
                player_y += 150
                if player_character.hp <= 0:
                    player_character.hp = 0
                    gameplay = False

            elif abs(elem.x - player_x) > abs(elem.y - player_y):
                orc_flag += 1
                if elem.x > player_x:
                    elem.x -= 4
                    elem.anim += 1
                    screen.blit(Orc_left[elem.anim % 3], (elem.x, elem.y))
                    screen.blit(orc_heal_points, (elem.x + 10, elem.y - 30))
                    screen.blit(orc_armor, (elem.x + 10, elem.y - 60))
                else:
                    elem.x += 4
                    elem.anim += 1
                    screen.blit(Orc_right[elem.anim % 3], (elem.x, elem.y))
                    screen.blit(orc_heal_points, (elem.x + 10, elem.y - 30))
                    screen.blit(orc_armor, (elem.x + 10, elem.y - 60))
            elif abs(elem.x - player_x) <= abs(elem.y - player_y):
                orc_flag = 0
                if elem.y > player_y:
                    elem.y -= 4
                    elem.anim += 1
                    screen.blit(Orc_up[elem.anim % 3], (elem.x, elem.y))
                    screen.blit(orc_heal_points, (elem.x + 10, elem.y - 30))
                    screen.blit(orc_armor, (elem.x + 10, elem.y - 60))
                else:
                    elem.y += 4
                    elem.anim += 1
                    screen.blit(Orc_down[elem.anim % 3], (elem.x, elem.y))
                    screen.blit(orc_heal_points, (elem.x + 10, elem.y - 30))
                    screen.blit(orc_armor, (elem.x + 10, elem.y - 60))


def nazgul_mechanicks_go():
    global player_x, player_y, n_list_it_the_game, n_flag, gameplay
    for (i, elem) in enumerate(n_list_it_the_game):
        n_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 25)
        n_heal_points = n_label.render("Hp: " + str(elem.hp), False, "green")
        n_armor = n_label.render("Armor: " + str(elem.armor), False, "green")

        if (abs(elem.x - player_x) <= 200) and (abs(elem.y - player_y) <= 200):

            if elem.x >= player_x:
                screen.blit(Nazgul_attack[0], (elem.x, elem.y))
                screen.blit(n_heal_points, (elem.x + 10, elem.y - 30))
                screen.blit(n_armor, (elem.x + 10, elem.y - 60))
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


def warg_mechanicks_go():
    global warg_list_in_the_game, player_y, player_x, player_character, warg_flag1
    global warg_flag2, warg_flag3, warg_flag4, warg_armor, gameplay
    for (i, elem1) in enumerate(warg_list_in_the_game):
        warg_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 25)
        warg_heal_points = warg_label.render("Hp: " + str(elem1.hp), False, "green")
        warg_armor = warg_label.render("Armor: " + str(elem1.armor), False, "green")

        if elem1.flag1 and elem1.y <= 1100:
            elem1.y += 15

            elem1.anim += 1
            screen.blit(Warg_Down[elem1.anim % 3], (elem1.x, elem1.y))
            screen.blit(warg_heal_points, (elem1.x + 10, elem1.y - 30))
            screen.blit(warg_armor, (elem1.x + 10, elem1.y - 60))

        if elem1.y > 1100 and elem1.flag1:
            a = player_character.Player_coordinate()
            elem1.x = -100
            elem1.y = a[1]
            elem1.flag1 = False
            elem1.flag2 = True

        if elem1.flag2 and elem1.x <= 900:
            elem1.x += 15

            elem1.anim += 1
            screen.blit(Warg_Right[elem1.anim % 2], (elem1.x, elem1.y))
            screen.blit(warg_heal_points, (elem1.x + 10, elem1.y - 30))
            screen.blit(warg_armor, (elem1.x + 10, elem1.y - 60))

        if elem1.x > 900 and elem1.flag2:
            a = player_character.Player_coordinate()
            elem1.x = a[0]
            elem1.y = 1100
            elem1.flag2 = False
            elem1.flag3 = True

        if elem1.flag3 and elem1.y >= -100:
            elem1.y -= 15

            elem1.anim += 1
            screen.blit(Warg_Up[elem1.anim % 2], (elem1.x, elem1.y))
            screen.blit(warg_heal_points, (elem1.x + 10, elem1.y - 30))
            screen.blit(warg_armor, (elem1.x + 10, elem1.y - 60))

        if elem1.y < -100 and elem1.flag3:
            a = player_character.Player_coordinate()
            elem1.x = 900
            elem1.y = a[1]
            elem1.flag3 = False
            elem1.flag4 = True

        if elem1.flag4 and elem1.x >= -100:
            elem1.x -= 15

            elem1.anim += 1
            screen.blit(Warg_Left[elem1.anim % 2], (elem1.x, elem1.y))
            screen.blit(warg_heal_points, (elem1.x + 10, elem1.y - 30))
            screen.blit(warg_armor, (elem1.x + 10, elem1.y - 60))

        if elem1.x < -100 and elem1.flag4:
            a = player_character.Player_coordinate()
            elem1.x = a[0]
            elem1.y = -100
            elem1.flag4 = False
            elem1.flag1 = True

        if abs(elem1.x - player_x) < 50 and abs(elem1.y - player_y) < 50:
            player_character.hp -= elem1.Attack()

            if player_x > elem1.x:
                player_x -= 50



            elif player_x < elem1.x:
                player_x += 50

            if player_y < elem1.y:
                player_y += 50

            elif player_y > elem1.y:
                player_y -= 50

            if player_character.hp <= 0:
                player_character.hp = 0
                gameplay = False


def Boss_warg_mechanicks_go():
    global Boss_warg_list_in_the_game, player_y, player_x, player_character,heal_anim,n_timer,Boss_warg_ability_flag
    global  gameplay,Boss_warg_flag3,Boss_warg_flag1,Boss_warg_flag2,Boss_warg_flag4,Boss_warg_Heal_flag
    for (i,elem2) in enumerate(Boss_warg_list_in_the_game):
        Boss_warg_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 25)
        Boss_warg_name = Boss_warg_label.render("The Alpha Warg",False,"green")
        Boss_warg_heal_points = Boss_warg_label.render("Hp: " + str(elem2.hp), False, "green")
        Boss_warg_armor = Boss_warg_label.render("Armor: " + str(elem2.armor), False, "green")

        if Boss_warg_Heal_flag == False:
            if Boss_warg_flag1 and elem2.y <= 1100 and Boss_warg_Heal_flag == False:
                elem2.y += 20

                elem2.anim += 1
                screen.blit(Boss_warg_Down[elem2.anim % 3], (elem2.x, elem2.y))
                screen.blit(Boss_warg_heal_points, (elem2.x + 10, elem2.y - 30))
                screen.blit(Boss_warg_armor, (elem2.x + 10, elem2.y - 60))
                screen.blit(Boss_warg_name, (400, 20))

            if elem2.y > 1100 and Boss_warg_flag1:
                a = player_character.Player_coordinate()
                elem2.x = -100
                elem2.y = a[1]
                Boss_warg_flag1 = False
                Boss_warg_flag2 = True

                if elem2.hp <= 100:
                    Boss_warg_Heal_flag = True
                    elem2.x = -100
                    elem2.y = 200

            if Boss_warg_flag2 and elem2.x <= 900 and Boss_warg_Heal_flag == False:
                elem2.x += 20

                elem2.anim += 1
                screen.blit(Boss_warg_Left[elem2.anim % 2], (elem2.x, elem2.y))
                screen.blit(Boss_warg_heal_points, (elem2.x + 10, elem2.y - 30))
                screen.blit(Boss_warg_armor, (elem2.x + 10, elem2.y - 60))
                screen.blit(Boss_warg_name, (400, 20))

            if elem2.x > 900 and Boss_warg_flag2:
                a = player_character.Player_coordinate()
                elem2.x = a[0]
                elem2.y = 1100
                Boss_warg_flag2 = False
                Boss_warg_flag3 = True

                if elem2.hp <= 100:
                    Boss_warg_Heal_flag = True
                    elem2.x = -100
                    elem2.y = 200

            if Boss_warg_flag3 and elem2.y >= -100 and Boss_warg_Heal_flag == False:
                elem2.y -= 20

                elem2.anim += 1
                screen.blit(Boss_warg_Up[elem2.anim % 2], (elem2.x, elem2.y))
                screen.blit(Boss_warg_heal_points, (elem2.x + 10, elem2.y - 30))
                screen.blit(Boss_warg_armor, (elem2.x + 10, elem2.y - 60))
                screen.blit(Boss_warg_name, (400, 20))

            if elem2.y < -100 and Boss_warg_flag3:
                a = player_character.Player_coordinate()
                elem2.x = 900
                elem2.y = a[1]
                Boss_warg_flag3 = False
                Boss_warg_flag4 = True

                if elem2.hp <= 100:
                    Boss_warg_Heal_flag = True
                    elem2.x = -100
                    elem2.y = 200

            if Boss_warg_flag4 and elem2.x >= -100 and Boss_warg_Heal_flag == False:
                elem2.x -= 20

                elem2.anim += 1
                screen.blit(Boss_warg_Right[elem2.anim % 2], (elem2.x, elem2.y))
                screen.blit(Boss_warg_heal_points, (elem2.x + 10, elem2.y - 30))
                screen.blit(Boss_warg_armor, (elem2.x + 10, elem2.y - 60))
                screen.blit(Boss_warg_name, (400, 20))

            if elem2.x < -100 and Boss_warg_flag4:
                a = player_character.Player_coordinate()
                elem2.x = a[0]
                elem2.y = -100
                Boss_warg_flag4 = False
                Boss_warg_flag1 = True

                if elem2.hp <= 100:
                    Boss_warg_Heal_flag = True
                    elem2.x = -100
                    elem2.y = 200

            if abs(elem2.x - player_x) < 50 and abs(elem2.y - player_y) < 50:
                player_character.hp -= elem2.base_attack()

                if player_x > elem2.x:
                    player_x -= 50

                elif player_x < elem2.x:
                    player_x += 50

                if player_y < elem2.y:
                    player_y += 50

                elif player_y > elem2.y:
                    player_y -= 50

                if player_character.hp <= 0:
                    player_character.hp = 0
                    gameplay = False



        if elem2.hp > 150:
           Boss_warg_Heal_flag = False
           heal_anim = 0
           Boss_warg_ability_flag = False

        if Boss_warg_Heal_flag:
            elem2.anim += 1

            if elem2.x < 250:
                elem2.x += 10
                screen.blit(Boss_warg_Left[elem2.anim % 2], (elem2.x, elem2.y))
                screen.blit(Boss_warg_heal_points, (elem2.x + 10, elem2.y - 30))
                screen.blit(Boss_warg_armor, (elem2.x + 10, elem2.y - 60))
                screen.blit(Boss_warg_name, (400, 20))

            else:
                if heal_anim != 3:
                    screen.blits(Boss_warg_Heal[heal_anim], (elem2.x, elem2.y))
                    screen.blit(Boss_warg_heal_points, (elem2.x + 10, elem2.y - 30))
                    screen.blit(Boss_warg_armor, (elem2.x + 10, elem2.y - 60))
                    screen.blit(Boss_warg_name, (400, 20))
                    heal_anim += 1
                else:
                    screen.blit(Boss_warg_Heal[3], (elem2.x, elem2.y))
                    screen.blit(Boss_warg_heal_points, (elem2.x + 10, elem2.y - 30))
                    screen.blit(Boss_warg_armor, (elem2.x + 10, elem2.y - 60))
                    screen.blit(Boss_warg_name, (400, 20))
                    Boss_warg_ability_flag = True






# ---функция отображения хп игрока-------------------------------------------------------------------------
def visual_health(player):
    global health_model, Fullhp, screen
    health = player.hp
    section = Fullhp // 9
    level_hp = health // section
    if level_hp == 9:
        screen.blit(health_model[0], (100, 50))
        screen.blit(health_model[0], (150, 50))
        screen.blit(health_model[0], (200, 50))
    elif level_hp == 8:
        screen.blit(health_model[0], (100, 50))
        screen.blit(health_model[0], (150, 50))
        screen.blit(health_model[1], (200, 50))
    elif level_hp == 7:
        screen.blit(health_model[0], (100, 50))
        screen.blit(health_model[0], (150, 50))
        screen.blit(health_model[2], (200, 50))
    elif level_hp == 6:
        screen.blit(health_model[0], (100, 50))
        screen.blit(health_model[0], (150, 50))

    elif level_hp == 5:
        screen.blit(health_model[0], (100, 50))
        screen.blit(health_model[1], (150, 50))

    elif level_hp == 4:
        screen.blit(health_model[0], (100, 50))
        screen.blit(health_model[2], (150, 50))

    elif level_hp == 3:
        screen.blit(health_model[0], (100, 50))

    elif level_hp == 2:
        screen.blit(health_model[1], (100, 50))

    elif level_hp == 1 or health > 0:
        screen.blit(health_model[2], (100, 50))

# -------------------------------------------------------------------------------------------------------


clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("The Hobbit: Pyton's Adventure")
#icon = pygame.image.load("I-ICON.png")
#pygame.display.set_icon(icon)
# ---Подключение изображений--------------------------------------------------------------
bg = pygame.image.load("images/Back.png")
bg = pygame.transform.scale(bg, (1000, 800))
# player = pygame.image.load("I-ICON.png")

"""Walk_right = [pygame.image.load('images/Right-1.png'),pygame.image.load('images/Right-2.png')]
Walk_left = [pygame.image.load('images/Left-1.png'),pygame.image.load('images/Left-2.png')]
Walk_Up = [pygame.image.load('images/Up-1.png'),pygame.image.load("images/Up-2.png")]
Walk_Down = [pygame.image.load('images/Down_-_1.png'),pygame.image.load('images/Down-2.png')]

Elf_left=[pygame.image.load("images/elf/elf_left.png").convert_alpha(),pygame.image.load("images/elf/elf_left1.png").convert_alpha()]
Elf_right=[pygame.image.load("images/elf/elf_right.png").convert_alpha(),pygame.image.load("images/elf/elf_right1.png").convert_alpha()]
Elf_up=[pygame.image.load("images/elf/elf_up.png").convert_alpha(),pygame.image.load("images/elf/elf_up1.png").convert_alpha()]
Elf_down=[pygame.image.load("images/elf/elf_down.png").convert_alpha(),pygame.image.load("images/elf/elf_down1.png").convert_alpha()]

Hobba_left=[pygame.image.load("images/hobba/hobba_left3.png"),pygame.image.load("images/hobba/hobba_left1.png")]
Hobba_right=[pygame.image.load("images/hobba/hobba_right3.png"),pygame.image.load("images/hobba/hobba_right1.png")]
Hobba_up=[pygame.image.load("images/hobba/hobba_up1.png"),pygame.image.load("images/hobba/hobba_up2.png"),pygame.image.load("images/hobba/hobba_up3.png")]
Hobba_down=[pygame.image.load("images/hobba/hobba_down1.png"),pygame.image.load("images/hobba/hobba_down2.png"),pygame.image.load("images/hobba/hobba_down3.png")]

Nazgul_right = [pygame.image.load("images/Nazgul-2-1.png"),pygame.image.load("images/Nazgul-2-1-right-eyes.png")]
Nazgul_left = [pygame.image.load("images/Nazgul-2-1-left.png"),pygame.image.load("images/Nazgul-2-1-left-eyes.png")]
Nazgul_attack_left = pygame.image.load("images/Nazgul-3-left.png")
Nazgul_attack_right = pygame.image.load("images/Nazgul-3-rigt.png")
Nazgul_attack =[pygame.image.load("images/Nazgul-3-left.png"),pygame.image.load("images/Nazgul-3-rigt.png")]

Orc_right = [pygame.image.load('images/orcs/orc_right1.png'), pygame.image.load('images/orcs/orc_right2.png'),
             pygame.image.load('images/orcs/orc_right3.png')]
Orc_left = [pygame.image.load('images/orcs/orc_left1.png'), pygame.image.load('images/orcs/orc_left2.png'),
            pygame.image.load('images/orcs/orc_left3.png')]
Orc_up = [pygame.image.load('images/orcs/orc_up1.png'), pygame.image.load('images/orcs/orc_up2.png'),
          pygame.image.load('images/orcs/orc_up3.png')]
Orc_down = [pygame.image.load('images/orcs/orc_down1.png'), pygame.image.load('images/orcs/orc_down2.png'),
            pygame.image.load('images/orcs/orc_stay.png')]

Orc_conqueror_right = [pygame.image.load('images/orcs/orc_conqueror_right1.png'),
                       pygame.image.load('images/orcs/orc_conqueror_right2.png'),
                       pygame.image.load('images/orcs/orc_conqueror_right3.png')]
Orc_conqueror_left = [pygame.image.load('images/orcs/orc_conqueror_left1.png'),
                      pygame.image.load('images/orcs/orc_conqueror_left2.png'),
                      pygame.image.load('images/orcs/orc_conqueror_left3.png')]
Orc_conqueror_up = [pygame.image.load('images/orcs/orc_conqueror_up1.png'),
                    pygame.image.load('images/orcs/orc_conqueror_up2.png'),
                    pygame.image.load('images/orcs/orc_conqueror_up3.png')]
Orc_conqueror_down = [pygame.image.load('images/orcs/orc_conqueror_down1.png'),
                      pygame.image.load('images/orcs/orc_conqueror_down2.png'),
                      pygame.image.load('images/orcs/orc_conqueror_down3.png')]

Warg_Up = [pygame.image.load("images/Warg_Up_1.png"), pygame.image.load("images/Warg_Up_2.png")]
Warg_Down = [pygame.image.load("images/Warg_Down_1.png"), pygame.image.load("images/Warg_Down_2.png"),
             pygame.image.load('images/Warg_Down_3.png')]
Warg_Left = [pygame.image.load("images/Warg_Left_1.png"), pygame.image.load("images/Warg_Left_2.png")]
Warg_Right = [pygame.image.load("images/Warg_Right_1.png"), pygame.image.load("images/Warg_Right_2.png")]
picture_list = [Walk_left, Walk_right, Walk_Up, Walk_Down, Nazgul_left, Nazgul_right, Nazgul_attack]

health_model = [pygame.image.load('images/health1.png'), pygame.image.load('images/health2.png'), pygame.image.load('images/health3.png')]

Arrow = [pygame.image.load("images/Arrow_Up.png"),pygame.image.load('images/Arrow_Down.png'), pygame.image.load('images/Arrow_Left.png'),pygame.image.load('images/Arrow_Right.png')]
for j in range(len(Arrow)):
    Arrow[j] = pygame.transform.scale(Arrow[j], (Arrow[j].get_width() // 3, Arrow[j].get_height() // 3))
for i in range(len(health_model)):
    health_model[i] = pygame.transform.scale(health_model[i], (health_model[i].get_width() // 2, health_model[i].get_height() // 2))
warg_picture_list =[Warg_Left,Warg_Up,Warg_Right,Warg_Down]
picture_list=convert_list_of_images(picture_list,3,3)
warg_picture_list=convert_list_of_images(warg_picture_list,1/2,1/2)
for i in range(len(picture_list)):
    for j in range(len(picture_list[i])):
        a=pygame.transform.scale(picture_list[i][j],(picture_list[i][j].get_width()//3,picture_list[i][j].get_height()//3))
        picture_list[i][j]=a
for i in range(len(warg_picture_list)):
    for j in range(len(warg_picture_list[i])):
        b = pygame.transform.scale(warg_picture_list[i][j], (warg_picture_list[i][j].get_width()* 2,warg_picture_list[i][j].get_height()*2))
        warg_picture_list[i][j] = b"""

Boss_warg_Up = [pygame.image.load("images/Boss_warg_Up_1.png"),pygame.image.load('images/Boss_warg_Up_2.png')]
Boss_warg_Down = [pygame.image.load("images/Boss_warg_Down_1.png"),pygame.image.load("images/Boss_warg_Down_2.png"),pygame.image.load('images/Boss_warg_Down_3.png')]
Boss_warg_Left =  [pygame.image.load("images/Boss_warg_Left.png"),pygame.image.load("images/Boss_warg_Left_2.png")]
Boss_warg_Right = [pygame.image.load("images/Boss_warg_Right.png"),pygame.image.load("images/Boss_warg_Right_2.png")]
Boss_warg_Heal = [pygame.image.load("images/Boss_warg_Heal_1.png"),pygame.image.load("images/Boss_warg_Heal_2.png"),pygame.image.load("images/Boss_warg_Heal_3.png"),pygame.image.load("images/Boss_warg_Heal_4.png")]
Boss_warg_picture_list = [Boss_warg_Up,Boss_warg_Down,Boss_warg_Left,Boss_warg_Right,Boss_warg_Heal]

for i in range(len(Boss_warg_picture_list)):
    for j in range(len(Boss_warg_picture_list[i])):
        b = pygame.transform.scale(Boss_warg_picture_list[i][j], (Boss_warg_picture_list[i][j].get_width()* 4,Boss_warg_picture_list[i][j].get_height()* 4))
        Boss_warg_picture_list[i][j] = b


# --------------------------------www-------------------------------------------------------------

wave_flag = True
num_mob = 0
wave_how = randint(1, 10)
wave_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 30)
how_villians = 0

n_flag = True
n_timer = pygame.USEREVENT + 1
pygame.time.set_timer(n_timer, 10000)
boss_timer_to_cry = pygame.USEREVENT + 1
boss_timer_to_heal = pygame.USEREVENT + 1
pygame.time.set_timer(boss_timer_to_cry, 1000)
pygame.time.set_timer(boss_timer_to_heal, 10000)


n_list_it_the_game = []

Boss_warg_list_in_the_game = []
Boss_warg_flag1 = True
Boss_warg_flag2 = False
Boss_warg_flag3 = False
Boss_warg_flag4 = False
Boss_warg_Heal_flag = False
Test_flag = True
heal_anim = 0
Boss_warg_ability_flag = False




warg_list_in_the_game = []

Player_animation_count = 0
bg_y = 0

orc_list_in_the_game = []
orc_flag = 0

player_speed = 15
player_x = 300
player_y = 250
flag_animation = True
Type_anim = 0

gameplay = True

# ---Подключение шрифтов----------------------------------------------------
player_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 30)
the_end_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 50)
loose_label = the_end_label.render('You died', False, (12, 12, 12))
restart_label = the_end_label.render("Start again", False, (35, 234, 32))
restart_label_rect = restart_label.get_rect(topleft=(250, 400))
Arrow_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 20)
# --------------------------------------------------------------------------

Arrow_list = []
Arrow_How = 0
Attack_point = 0

boss_list = []

Start_game_flag = True
entr = False  # флаг на переключение экранов стартовый->выбор игрока
Fullhp = 1
running = True
pygame.mixer.music.load("Sounds/Main theme.mp3")
pygame.mixer.music.play(-1)
flag_music = True
flag_create_the_boss = False
flag_win_the_boss = False
while running:
    # ---Стартовый экран-------------------------------------------------------
    if Start_game_flag:
        gameplay = False
        screen.fill("Black")
        label = pygame.font.Font('fonts/RobotoMono-VariableFont_wght.ttf', 20)
        Game_Name = label.render("The Hobbit: Pyton's Adventure", False, "Yellow")
        screen.blit(Game_Name, (250, 400))
        Game_start = label.render("Press any to start...", False, "Yellow")
        screen.blit(Game_start, (250, 600))
        # -------------------------------------------------------------------------

        # ---экран выбора героя----------------------------------------------------
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
            # реализация этого выбора
            if Character_label_Elf_rect.collidepoint(mouse) and pygame.mouse.get_pressed():
                gameplay = True
                print("Your choose is Elf")
                player_character = Elf()
                All_Hp = player_character.hp
                Fullhp = All_Hp
                Arrow_How = 100
                Start_game_flag = False

            elif Character_label_Human_rect.collidepoint(mouse) and pygame.mouse.get_pressed():
                gameplay = True
                print("Your choose is Human")
                player_character = Human()
                All_Hp = player_character.hp
                Fullhp = All_Hp
                Start_game_flag = False

            elif Character_label_Hobbit_rect.collidepoint(mouse) and pygame.mouse.get_pressed():
                gameplay = True
                print("Your choose is Hobbit")
                player_character = Hobbit()
                All_Hp = player_character.hp
                Fullhp = All_Hp
                Start_game_flag = False

    # ---процесс геймплея(арена)-------------------------------------------------------------------
    if gameplay:
        if flag_music:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("sounds/Alternative 2.mp3")
            pygame.mixer.music.play(-1)
            flag_music = False
        screen.blit(bg, (0, bg_y))
        screen.blit(bg, (0, bg_y - 800))

        wave_view_label = wave_label.render("You have a " + str(wave_how) + " Wave's", False, "Brown")
        wave_villians_label = wave_label.render("Villian's: " + str(num_mob), False, "Brown")
        screen.blit(wave_view_label, (20, 660))
        screen.blit(wave_villians_label, (20, 700))

        if player_character.ability == "has agility":
            Arrow_label_how = Arrow_label.render("You have a " + str(Arrow_How) + " arrow's", False, "Brown")
            Arrow_label_press = Arrow_label.render("Press R...", False, "Brown")
            Character_label_Elf_ability = Arrow_label.render(
                "You can" + (1 - flag_ability) * "'t" + " use " + "The ability: " +
                str(player_character.ability), False, 'Brown')
            screen.blit(Arrow_label_how, (700, 30))
            screen.blit(Arrow_label_press, (700, 60))
            screen.blit(Character_label_Elf_ability, (500, 750))

        else:
            Arrow_label_how = Arrow_label.render("You can touch with  " + str(player_character.weapon.name), False,
                                                 "Brown")
            Arrow_label_press = Arrow_label.render("Press F...", False, "Brown")
            Character_label_Hobbit_and_Human_ability = Arrow_label.render(
                "You can" + (1 - flag_ability) * "'t" + " use " + "The ability: " + str(player_character.ability),
                False, 'Brown')
            screen.blit(Arrow_label_how, (600, 30))
            screen.blit(Arrow_label_press, (600, 60))
            screen.blit(Character_label_Hobbit_and_Human_ability, (500, 750))

        # ---реализация поведения и движения мобов-------------------------------------------

        if warg_list_in_the_game:
            warg_mechanicks_go()

        if n_list_it_the_game:
            nazgul_mechanicks_go()

        if orc_list_in_the_game:
            orc_mechanicks_go()

        if Boss_warg_list_in_the_game:
            Boss_warg_mechanicks_go()
        # -----------------------------------------------------------------------------------
        if boss_list:

            for (i, elem) in enumerate(boss_list):
                label_Boss = pygame.font.Font('fonts/RobotoMono-VariableFont_wght.ttf', 50)
                name_label_boss = label_Boss.render('BOSSSSSS', True, 'Red')
                screen.blit(name_label_boss, (screen.get_width() // 2 - 100, 50))
                label_Boss = pygame.font.Font('fonts/RobotoMono-VariableFont_wght.ttf', 10)
                cry_label_boss = label_Boss.render(elem.cry, False, 'White')
                hp_boss = label_Boss.render("HP BOSS: " + str(elem.hp), True, 'Red')
                armor_boss = label_Boss.render("ARMOR BOSS: " + str(elem.armor), True, 'Red')
                screen.blit(hp_boss, (screen.get_width() // 2 - 100, 100))
                if elem.flag_go_to_center:
                    elem.coord_x -= 5
                    elem.anim += 1
                    screen.blit(Orc_conqueror_left[elem.anim % 3], (elem.coord_x, elem.coord_y))
                    if elem.coord_x - screen.get_width()//2 < 10:
                        elem.flag_go_to_center = False
                        pygame.time.set_timer(boss_timer_to_cry, 1000)
                elif elem.flag_orc_cry:
                    screen.blit(Orc_conqueror_down[1], (elem.coord_x, elem.coord_y))
                    screen.blit(cry_label_boss, (elem.coord_x + 5 + randint(-1, 1), elem.coord_y - 5 + randint(-1, 1)))

                elif elem.hp > 0:

                    if elem.hp < 50 and elem.heal > 0 and elem.flag_boss_to_heal:
                        #запускает щит и остаётся на месте
                        elem.heal -= 1
                        elem.healing()
                        elem.flag_boss_to_heal = False
                        pygame.time.set_timer(boss_timer_to_heal, 10000)
                    else:
                        if abs(elem.coord_x - player_x) <= 60 and abs(elem.coord_y - player_y) <= 60:
                            player_character.hp -= elem.standart_attack()
                            player_y += 150
                            if player_character.hp <= 0:
                                player_character.hp = 0
                                gameplay = False

                        elif abs(elem.coord_x - player_x) > abs(elem.coord_y - player_y):
                            if elem.coord_x > player_x:
                                elem.coord_x -= 4
                                elem.anim += 1
                                screen.blit(Orc_conqueror_left[elem.anim % 3], (elem.coord_x, elem.coord_y))

                            else:
                                elem.coord_x += 4
                                elem.anim += 1
                                screen.blit(Orc_conqueror_right[elem.anim % 3], (elem.coord_x, elem.coord_y))

                        elif abs(elem.coord_x - player_x) <= abs(elem.coord_y - player_y):
                            orc_flag = 0
                            if elem.coord_y > player_y:
                                elem.coord_y -= 4
                                elem.anim += 1
                                screen.blit(Orc_conqueror_up[elem.anim % 3], (elem.coord_x, elem.coord_y))

                            else:
                                elem.coord_y += 4
                                elem.anim += 1
                                screen.blit(Orc_conqueror_down[elem.anim % 3], (elem.coord_x, elem.coord_y))


        # ---перс при бездействии-------------------------------------------
        if flag_animation:
            player_heal_points = player_label.render("Hp: " + str(player_character.hp), False, "Red")
            if Type_anim == 0:
                screen.blit(player_character.la[2][0], (player_x, player_y))
                screen.blit(player_heal_points, (player_x + 20, player_y - 30))
            elif Type_anim == 1:
                screen.blit(player_character.la[0][0], (player_x, player_y))
                screen.blit(player_heal_points, (player_x + 20, player_y - 30))
            elif Type_anim == 2:
                screen.blit(player_character.la[1][0], (player_x, player_y))
                screen.blit(player_heal_points, (player_x + 20, player_y - 30))
            elif Type_anim == 3:
                screen.blit(player_character.la[3][0], (player_x, player_y))
                screen.blit(player_heal_points, (player_x + 20, player_y - 30))

        flag_animation = True
        # ---анимация персонажа-------------------------------------------
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
                if ar[1] == 0:
                    screen.blit(Arrow[0], (ar[0].x, ar[0].y))
                    ar[0].y -= 20

                elif ar[1] == 2:
                    screen.blit(Arrow[2], (ar[0].x, ar[0].y))
                    ar[0].x -= 20

                elif ar[1] == 3:
                    screen.blit(Arrow[3], (ar[0].x, ar[0].y))
                    ar[0].x += 20

                elif ar[1] == 1:
                    screen.blit(Arrow[1], (ar[0].x, ar[0].y))
                    ar[0].y += 20

                if n_list_it_the_game:
                    for (j, elem) in enumerate(n_list_it_the_game):
                        if abs(ar[0].x - elem.x) < 100 and abs(ar[0].y - elem.y) < 100:
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
                                num_mob -= 1
                                flag_ability = 1

                            if Arrow_list:
                                Arrow_list.pop(i)

                        if Arrow_list:
                            if ar[0].y < -100:
                                Arrow_list.pop(i)
                            elif ar[0].y > 1100:
                                Arrow_list.pop(i)
                            elif ar[0].x < - 100:
                                Arrow_list.pop(i)
                            elif ar[0].x > 1000:
                                Arrow_list.pop(i)
                                continue

                if warg_list_in_the_game:
                    for (j1, elem1) in enumerate(warg_list_in_the_game):
                        if abs(ar[0].x - elem1.x) < 100 and abs(ar[0].y - elem1.y) < 100:
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
                                num_mob -= 1
                                flag_ability = 1

                            if Arrow_list:
                                Arrow_list.pop(i)
                                continue

                if orc_list_in_the_game:
                    for (j, elem) in enumerate(orc_list_in_the_game):
                        if abs(ar[0].x - elem.x) < 100 and abs(ar[0].y - elem.y) < 100:
                            elem.y -= 50
                            if elem.armor > 0:
                                elem.armor -= Attack_point
                                if elem.armor < 0:
                                    elem.armor = 0
                            else:
                                elem.Protect(Attack_point)

                            if elem.hp <= 0:
                                orc_list_in_the_game.pop(j)
                                print("the Orc is murdered...")
                                num_mob -= 1
                                flag_ability = 1

                            if Arrow_list:
                                Arrow_list.pop(i)
                                continue
                if boss_list:
                    for (j, elem) in enumerate(boss_list):
                        if abs(ar[0].x - elem.coord_x) < 100 and abs(ar[0].y - elem.coord_y) < 100:
                            elem.coord_y -= 50
                            if elem.armor > 0:
                                elem.armor -= Attack_point
                                if elem.armor < 0:
                                    elem.armor = 0
                            else:
                                elem.hp -= Attack_point

                            if elem.hp <= 0:
                                boss_list.pop(j)
                                print("the Boss Orc Conqueror is murdered...")
                                flag_create_the_boss = False
                                flag_win_the_boss = True

                            if Arrow_list:
                                Arrow_list.pop(i)
                                continue

                if Boss_warg_list_in_the_game:
                    for (j1, elem2) in enumerate(Boss_warg_list_in_the_game):
                        if abs(ar[0].x - elem2.x) < 100 and abs(ar[0].y - elem2.y) < 100:
                            elem2.y -= 50

                            if elem2.armor > 0:
                                elem2.armor -= Attack_point
                                if elem2.armor < 0:
                                    elem2.armor = 0
                            else:
                                elem2.Protect(Attack_point)

                            if elem2.hp <= 0:
                                Boss_warg_list_in_the_game.pop(j1)
                                print("the Alpha Warg is murdered...")
                                num_mob -= 1
                                flag_ability = 1

                            if Arrow_list:
                                Arrow_list.pop(i)
                                continue


        visual_health(player_character)






    elif Start_game_flag == False:
        screen.fill("White")
        screen.blit(loose_label, (250, 500))
        screen.blit(restart_label, (250, 400))
        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed():
            player_y = 500
            n_list_it_the_game.clear()
            warg_list_in_the_game.clear()
            orc_list_in_the_game.clear()
            Arrow_list.clear()
            boss_list.clear()
            player_character.hp = All_Hp
            flag_ability = 1
            Arrow_How = 0
            Start_game_flag = True
            flag_create_the_boss = False
            flag_win_the_boss = False


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if wave_how > 0:
            if wave_flag:
                num_mob = randint(1, 3)
                how_villians = num_mob
                wave_flag = False


            if flag_create_the_boss:
                if event.type == boss_timer_to_cry:
                    boss_list[0].flag_orc_cry = False
                if event.type == boss_timer_to_heal:
                    boss_list[0].flag_boss_to_heal = True

            if how_villians > 0 and event.type == n_timer:
                num = randint(1, 3)
                how_villians -= 1

                if num == 1:
                    n_list_it_the_game.append(Nazgul(0))

                elif num == 2:
                    warg_list_in_the_game.append(Warg(True,False,False,False))

                elif num == 3:
                    orc_list_in_the_game.append(Ork(3))


                if Test_flag:
                    Boss_warg_list_in_the_game.append(Boss_warg(250,-100,0))
                    Test_flag = False


            if flag_win_the_boss:
                wave_how -= 1
                wave_flag = True
                flag_win_the_boss = False

            elif how_villians == 0 and num_mob == 0 and not flag_create_the_boss:
                boss_list.append(BossOrkConqueror(200, 100, 60, Weapon('Sword Orc Boss', 40), Magic('Protective Dome', 5),
                                        "AAAAAAARGHHH", screen.get_width() + 50, screen.get_height()//2, 3))


                flag_create_the_boss = True


        else:
            print("The end")
            pygame.quit()

        if event.type == n_timer and Boss_warg_ability_flag:
            if Boss_warg_list_in_the_game:
                for elem2 in Boss_warg_list_in_the_game:
                    elem2.special_ability()

        if gameplay and event.type == pygame.KEYDOWN and event.key == pygame.K_r and Arrow_How > 0 and player_character.ability == "has agility":
            if Type_anim == 0:
                side = 0
                Arrow_list.append((Arrow[0].get_rect(topleft=(player_x + 25, player_y - 40)), side))

            elif Type_anim == 1:
                side = 2
                Arrow_list.append((Arrow[2].get_rect(topleft=(player_x - 30, player_y)), side))

            elif Type_anim == 2:
                side = 3
                Arrow_list.append((Arrow[3].get_rect(topleft=(player_x + 30, player_y)), side))

            elif Type_anim == 3:
                side = 1
                Arrow_list.append((Arrow[1].get_rect(topleft=(player_x + 25, player_y + 20)), side))

            Arrow_How -= 1
            Attack_point = player_character.Attack()

        if Start_game_flag and event.type == pygame.KEYDOWN:
            entr = True

        if gameplay and (player_character.ability == "is a tracker" or player_character.ability == "can a hide") and event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            a = player_character.Attack()
            if Attack_point <= a:
                Attack_point = a
            if n_list_it_the_game:
                for (j, elem) in enumerate(n_list_it_the_game):
                    if abs(elem.x - player_x) < 70 and abs(elem.y - player_y) < 70:
                        elem.y -= 100

                        if elem.armor > 0:
                            elem.armor -= Attack_point
                            if elem.armor < 0:
                                elem.armor = 0
                        else:
                            elem.Protect(Attack_point)


                        if elem.hp <= 0:
                            n_list_it_the_game.pop(j)
                            print("the Nazgul is murdered...")
                            num_mob -= 1
                            flag_ability = 1

            if warg_list_in_the_game:
                for (j1, elem1) in enumerate(warg_list_in_the_game):
                    if abs(elem1.x - player_x) < 70 and abs(elem1.y - player_y) < 70:
                        elem1.y -= 100

                        if elem1.armor > 0:
                            elem1.armor -= Attack_point
                            if elem1.armor < 0:
                                elem1.armor = 0
                        else:
                            elem1.Protect(Attack_point)


                        if elem1.hp <= 0:
                            warg_list_in_the_game.pop(j1)
                            print("the Warg is murdered...")
                            num_mob -= 1
                            flag_ability = 1

            if orc_list_in_the_game:
                for (j, elem) in enumerate(orc_list_in_the_game):
                    if abs(elem.x - player_x) < 70 and abs(elem.y - player_y) < 70:
                        elem.y -= 100
                        if elem.armor > 0:
                            elem.armor -= Attack_point
                            if elem.armor < 0:
                                elem.armor = 0
                        else:
                            elem.Protect(Attack_point)


                        if elem.hp <= 0:
                            orc_list_in_the_game.pop(j)
                            print("the Ork is murdered...")
                            num_mob -= 1
                            flag_ability = 1
            if boss_list:
                for (j, elem) in enumerate(boss_list):
                    if abs(elem.coord_x - player_x) < 70 and abs(elem.coord_y - player_y) < 70:
                        elem.coord_y -= 100
                        if elem.armor > 0:
                            elem.armor -= Attack_point
                            if elem.armor < 0:
                                elem.armor = 0
                        else:
                            elem.hp -= Attack_point

                        if elem.hp <= 0:
                            boss_list.pop(j)
                            print("the Ork is murdered...")
                            flag_ability = 1
                            flag_create_the_boss = False
                            flag_win_the_boss = True

            if Boss_warg_list_in_the_game:
                for (j1, elem2) in enumerate(Boss_warg_list_in_the_game):
                    if abs(elem2.x - player_x) < 70 and abs(elem2.y - player_y) < 70:
                        elem2.y -= 100

                        if elem2.armor > 0:
                            elem2.armor -= Attack_point
                            if elem2.armor < 0:
                                elem2.armor = 0
                        else:
                            elem2.Protect(Attack_point)

                        Attack_point = 0

                        if elem2.hp <= 0:
                            Boss_warg_list_in_the_game.pop(j1)
                            print("the Alpha Warg is murdered...")
                            num_mob -= 1
                            flag_ability = 1

        if gameplay and event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            player_character.Use_the_Ability()

    clock.tick(20)
