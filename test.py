import pygame
from random import randint
from file_for_images import *
from file_for_class import *
#пуш для Некита
#---------------------------------------------------
"""
Некит - босс Назгул
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
        Character.__init__(self,190,30, "has agility",Weapon("Bow",30),[Elf_left,Elf_right,Elf_up,Elf_down])

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
        Character.__init__(self,200,40, "is a tracker", Weapon("sword", 15),[Walk_left,Walk_right,Walk_Up,Walk_Down])

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
        Character.__init__(self,150,70, 'can a hide', Weapon('Arnors knife', 15),[Hobba_left,Hobba_right,Hobba_up,Hobba_down])

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
#--- функции механики перемещения мобов ----------------------------------------------------------------
def orc_mechanicks_go():
    global player_x, player_y, orc_list_in_the_game, orc_flag, gameplay
    if orc_list_in_the_game:
        for (i, elem) in enumerate(orc_list_in_the_game):
            orc_label = pygame.font.Font("fonts/Fonts/RobotoMono-VariableFont_wght.ttf", 25)
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
        n_label = pygame.font.Font("fonts/Fonts/RobotoMono-VariableFont_wght.ttf", 25)
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
        warg_label = pygame.font.Font("fonts/Fonts/RobotoMono-VariableFont_wght.ttf", 25)
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

def Boss_nazgul_mechanicks():
    global totem_list,gameplay
    Boss_nazgul_label = pygame.font.Font("fonts/Fonts/RobotoMono-VariableFont_wght.ttf", 25)
    Boss_nazgul_name = Boss_nazgul_label.render("King of nazguls", False, "blue")
    Boss_nazgul_heal_points = Boss_nazgul_label.render("Hp: " + str(elem.hp), False, "green")
    Boss_nazgul_armor = Boss_nazgul_label.render("Armor: " + str(elem.armor), False, "green")

    #screen.blit(boss_nazgul_down[0],(screen.get_width()//2,200))

    if elem.hp>0:
        screen.blit(Boss_nazgul_heal_points, (elem.x + 10, elem.y - 30))
        screen.blit(Boss_nazgul_armor, (elem.x + 10, elem.y - 60))
        screen.blit(Boss_nazgul_name, (400, 20))
        if elem.flag_for_proza:
            elem.proza(screen)
        else:
            if elem.hp>50 and elem.flag_invicible==False:
                elem.go_to(screen,player_x,player_y)
                if abs(player_x-elem.x)<25 and abs(player_y-elem.y)<25:
                    player_character.hp-=(elem.standart_attack(screen,player_x,player_y))
            if elem.hp<=50:
                elem.flag_go_to_center=True
            if elem.flag_go_to_center:
                elem.go_to(screen,screen.get_width()//2,screen.get_height()//2)
                if elem.check==True:
                    elem.flag_invicible=True
                    elem.check=False
                    elem.flag_go_to_center=False
            if elem.flag_invicible:
                elem.invicible(screen)
                if elem.totem_spawn:
                    totem_list=[Totem(elem.x-200,elem.y-200),Totem(elem.x-200,elem.y+200),Totem(elem.x+200,elem.y-200),Totem(elem.x+200,elem.y+200)]
                    elem.totem_spawn=False
                for i in totem_list:
                    i.spawn(screen)
                    i.draw(screen)
                if elem.hp<100 and len(totem_list)!=0:
                    if elem.flag_heal:
                        elem.hp+=5
                        elem.flag_heal=False
                        pygame.time.set_timer(elem.time_heal,1000)
                else:
                    elem.flag_invicible=False
                    totem_list.clear()
                    elem.totem_spawn=True
            if player_character.hp <= 0:#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                player_character.hp = 0
                gameplay = False

def Boss_warg_mechanicks_go():
    global Boss_warg_list_in_the_game, player_y, player_x, player_character, heal_anim, n_timer, Boss_warg_ability_flag, \
        gameplay, Boss_warg_flag3, Boss_warg_flag1, Boss_warg_flag2, Boss_warg_flag4, Boss_warg_Heal_flag
    Boss_warg_label = pygame.font.Font("fonts/Fonts/RobotoMono-VariableFont_wght.ttf", 25)
    Boss_warg_name = Boss_warg_label.render("The Alpha Warg", False, "green")
    Boss_warg_heal_points = Boss_warg_label.render("Hp: " + str(elem.hp), False, "green")
    Boss_warg_armor = Boss_warg_label.render("Armor: " + str(elem.armor), False, "green")

    if Boss_warg_Heal_flag == False:
        if Boss_warg_flag1 and elem.y <= 1100 and Boss_warg_Heal_flag == False:
            elem.y += 20

            elem.anim += 1
            screen.blit(Boss_warg_Down[elem.anim % 3], (elem.x, elem.y))
            screen.blit(Boss_warg_heal_points, (elem.x + 10, elem.y - 30))
            screen.blit(Boss_warg_armor, (elem.x + 10, elem.y - 60))
            screen.blit(Boss_warg_name, (400, 20))

        if elem.y > 1100 and Boss_warg_flag1:
            a = player_character.Player_coordinate()
            elem.x = -100
            elem.y = a[1]
            Boss_warg_flag1 = False
            Boss_warg_flag2 = True

            if elem.hp <= 100:
                Boss_warg_Heal_flag = True
                elem.armor += 500
                elem.x = -100
                elem.y = 200

        if Boss_warg_flag2 and elem.x <= 900 and Boss_warg_Heal_flag == False:
            elem.x += 20

            elem.anim += 1
            screen.blit(Boss_warg_Left[elem.anim % 2], (elem.x, elem.y))
            screen.blit(Boss_warg_heal_points, (elem.x + 10, elem.y - 30))
            screen.blit(Boss_warg_armor, (elem.x + 10, elem.y - 60))
            screen.blit(Boss_warg_name, (400, 20))

        if elem.x > 900 and Boss_warg_flag2:
            a = player_character.Player_coordinate()
            elem.x = a[0]
            elem.y = 1100
            Boss_warg_flag2 = False
            Boss_warg_flag3 = True

            if elem.hp <= 100:
                Boss_warg_Heal_flag = True
                elem.armor += 500
                elem.x = -100
                elem.y = 200

        if Boss_warg_flag3 and elem.y >= -100 and Boss_warg_Heal_flag == False:
            elem.y -= 20

            elem.anim += 1
            screen.blit(Boss_warg_Up[elem.anim % 2], (elem.x, elem.y))
            screen.blit(Boss_warg_heal_points, (elem.x + 10, elem.y - 30))
            screen.blit(Boss_warg_armor, (elem.x + 10, elem.y - 60))
            screen.blit(Boss_warg_name, (400, 20))

        if elem.y < -100 and Boss_warg_flag3:
            a = player_character.Player_coordinate()
            elem.x = 900
            elem.y = a[1]
            Boss_warg_flag3 = False
            Boss_warg_flag4 = True

            if elem.hp <= 100:
                Boss_warg_Heal_flag = True
                elem.armor += 500
                elem.x = -100
                elem.y = 200

        if Boss_warg_flag4 and elem.x >= -100 and Boss_warg_Heal_flag == False:
            elem.x -= 20

            elem.anim += 1
            screen.blit(Boss_warg_Right[elem.anim % 2], (elem.x, elem.y))
            screen.blit(Boss_warg_heal_points, (elem.x + 10, elem.y - 30))
            screen.blit(Boss_warg_armor, (elem.x + 10, elem.y - 60))
            screen.blit(Boss_warg_name, (400, 20))

        if elem.x < -100 and Boss_warg_flag4:
            a = player_character.Player_coordinate()
            elem.x = a[0]
            elem.y = -100
            Boss_warg_flag4 = False
            Boss_warg_flag1 = True

            if elem.hp <= 100:
                Boss_warg_Heal_flag = True
                elem.armor += 500
                elem.x = -100
                elem.y = 200

        if abs(elem.x - player_x) < 50 and abs(elem.y - player_y) < 50:
            player_character.hp -= elem.base_attack()

            if player_x > elem.x:
                player_x -= 150

            elif player_x < elem.x:
                player_x += 150

            if player_y < elem.y:
                player_y += 150

            elif player_y > elem.y:
                player_y -= 150

            if player_character.hp <= 0:
                player_character.hp = 0
                gameplay = False

    if elem.hp > 150:
        Boss_warg_Heal_flag = False
        heal_anim = 0
        Boss_warg_ability_flag = False

    if Boss_warg_Heal_flag:
        elem.anim += 1

        if elem.x < 250:
            elem.x += 10
            screen.blit(Boss_warg_Left[elem.anim % 2], (elem.x, elem.y))
            screen.blit(Boss_warg_heal_points, (elem.x + 10, elem.y - 30))
            screen.blit(Boss_warg_armor, (elem.x + 10, elem.y - 60))
            screen.blit(Boss_warg_name, (400, 20))

        else:
            if heal_anim != 3:
                screen.blit(Boss_warg_Heal[heal_anim], (elem.x, elem.y))
                screen.blit(Boss_warg_heal_points, (elem.x + 10, elem.y - 30))
                screen.blit(Boss_warg_armor, (elem.x + 10, elem.y - 60))
                screen.blit(Boss_warg_name, (400, 20))
                heal_anim += 1
            else:
                screen.blit(Boss_warg_Heal[3], (elem.x, elem.y))
                screen.blit(Boss_warg_heal_points, (elem.x + 10, elem.y - 30))
                screen.blit(Boss_warg_armor, (elem.x + 10, elem.y - 60))
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
        screen.blit(health_model[2], (200, 50))

    elif level_hp == 5:
        screen.blit(health_model[0], (100, 50))
        screen.blit(health_model[1], (150, 50))
        screen.blit(health_model[2], (200, 50))

    elif level_hp == 4:
        screen.blit(health_model[0], (100, 50))
        screen.blit(health_model[2], (150, 50))
        screen.blit(health_model[2], (200, 50))

    elif level_hp == 3:
        screen.blit(health_model[0], (100, 50))
        screen.blit(health_model[2], (150, 50))
        screen.blit(health_model[2], (200, 50))

    elif level_hp == 2:
        screen.blit(health_model[1], (100, 50))
        screen.blit(health_model[2], (150, 50))
        screen.blit(health_model[2], (200, 50))

    elif level_hp == 1 or health > 0:
        screen.blit(health_model[2], (100, 50))
        screen.blit(health_model[2], (150, 50))
        screen.blit(health_model[2], (200, 50))



# -------------------------------------------------------------------------------------------------------


clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1000,800))
#print(screen.get_width()//2,screen.get_height()//2)
pygame.display.set_caption("The Hobbit: Pyton's Adventure")
bg = pygame.image.load("images/Back.png")
bg = pygame.transform.scale(bg, (1000, 800))

wave_flag = False
num_mob = 0
wave_how = randint(1, 10)
wave_label = pygame.font.Font("fonts/Fonts/RobotoMono-VariableFont_wght.ttf", 30)
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
heal_anim = 0
Boss_warg_ability_flag = False

attack_timer = pygame.USEREVENT + 1
pygame.time.set_timer(attack_timer, 1000)
attack_flag = True




#warg_list_in_the_game = []

Player_animation_count = 0
bg_y = 0

orc_list_in_the_game = []
orc_flag = 0
totem_list=[]
player_speed = 15
player_x = 300
player_y = 250
flag_animation = True
Type_anim = 0

gameplay = True

# ---Подключение шрифтов----------------------------------------------------
player_label = pygame.font.Font("fonts/Fonts/RobotoMono-VariableFont_wght.ttf", 30)
the_end_label = pygame.font.Font("fonts/Fonts/RobotoMono-VariableFont_wght.ttf", 50)
loose_label = the_end_label.render('YOU LOOSE!', False, "Red")
restart_label = the_end_label.render("Start again", False, "Black")
restart_label_rect = restart_label.get_rect(topleft=(250, 400))
Arrow_label = pygame.font.Font("fonts/Fonts/Angkor-Regular.ttf", 20)
# --------------------------------------------------------------------------

Arrow_list = []
Arrow_How = 0
Attack_point = 0

boss_list = []
portal_list = []

Start_game_flag = True
entr = False  # флаг на переключение экранов стартовый->выбор игрока
Fullhp = 1
running = True
pygame.mixer.music.load("Sounds/Main theme.mp3")
pygame.mixer.music.play(-1)
flag_music = True
flag_create_the_boss = False
flag_win_the_boss = False
flag_project_screen = True
timer_for_screensaver = pygame.USEREVENT + 1
pygame.time.set_timer(timer_for_screensaver, 4000)
while running:
    # ---Стартовый экран-------------------------------------------------------
    if Start_game_flag:
        gameplay = False
        screen.fill("Black")
        label = pygame.font.Font('fonts/Fonts/gwent_extrabold.ttf', 60)
        project_company = label.render("JIN Project", True, "White")
        if flag_project_screen:
            screen.blit(screen_saver, (0,0))
            screen.blit(project_company, (screen.get_width() // 2 - 150, screen.get_height() // 2))
        else:
            screen.blit(screen_saver, (0, 0))
            label = pygame.font.Font('fonts/Fonts/gwent_extrabold.ttf', 30)
            Game_Name = label.render("The Hobbit: Pyton's Adventure", False, "Black")
            screen.blit(Game_Name, (50, 50))
            button_play_rect = button_play_up.get_rect(topleft=(60, 100))
            if button_play_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed() == (1, 0, 0):
                screen.blit(button_play_down, (60, 100))
                entr = True
            else:
                screen.blit(button_play_up, (60, 100))
            Game_start = label.render("Press any to start...", False, "Yellow")
            screen.blit(Game_start, (250, 600))

        # -------------------------------------------------------------------------

        # ---экран выбора героя----------------------------------------------------
        if entr:
            screen.fill("Black")

            screen.blit(pygame.image.load("images/CHOICE_screen2.png"),(0,0))
            Character_label = label.render("Choose your hero:", False, "Red")
            screen.blit(Character_label, (400, 100))
            Character_label_Elf = label.render("Forest Elf", False, "Yellow")
            screen.blit(Character_label_Elf, (250, 200))
            Character_label_Human = label.render("Human", False, "Yellow")
            screen.blit(Character_label_Human, (250, 400))
            Character_label_Hobbit = label.render("Hobbit", False, "Yellow")
            screen.blit(Character_label_Hobbit, (250, 600))

            Character_label_Elf_rect = Character_label_Elf.get_rect(topleft=(250, 200))
            Character_label_Human_rect = Character_label_Human.get_rect(topleft=(250, 400))
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
                wave_how = randint(1, 10)
                wave_flag = True


            elif Character_label_Human_rect.collidepoint(mouse) and pygame.mouse.get_pressed():
                gameplay = True
                print("Your choose is Human")
                player_character = Human()
                All_Hp = player_character.hp
                Fullhp = All_Hp
                Start_game_flag = False
                wave_how = randint(1, 10)
                wave_flag = True


            elif Character_label_Hobbit_rect.collidepoint(mouse) and pygame.mouse.get_pressed():
                gameplay = True
                print("Your choose is Hobbit")
                player_character = Hobbit()
                All_Hp = player_character.hp
                Fullhp = All_Hp
                Start_game_flag = False
                wave_how = randint(1, 10)
                wave_flag = True


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
            Arrow_label_how = Arrow_label.render("You have a " + str(Arrow_How) + " arrow's", True, "Black")
            Arrow_label_press = Arrow_label.render("Press ", True, "Black")
            Character_label_Elf_ability = Arrow_label.render(
                "You can" + (1 - flag_ability) * "'t" + " use " + "The ability: " +
                str(player_character.ability), False, 'Brown')
            screen.blit(Arrow_label_how, (700, 30))
            screen.blit(Arrow_label_press, (700, 60))
            screen.blit(button_R, (780, 60))
            screen.blit(Character_label_Elf_ability, (500, 750))
            if (1 - flag_ability) == 1:
                screen.blit(Rings[0], (400, 710))
            else:
                screen.blit(Rings_active[0], (400, 710))

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
            if player_character.ability == "is a tracker":
                if (1 - flag_ability) == 1:
                    screen.blit(Rings[1], (400, 710))
                else:
                    screen.blit(Rings_active[1], (400, 710))

            else:
                if (1 - flag_ability) == 1:
                    screen.blit(Rings[2], (400, 710))
                else:
                    screen.blit(Rings_active[2], (400, 710))

        # ---реализация поведения и движения мобов-------------------------------------------

        if warg_list_in_the_game:
            warg_mechanicks_go()

        if n_list_it_the_game:
            nazgul_mechanicks_go()

        if orc_list_in_the_game:
            orc_mechanicks_go()

        """if Boss_warg_list_in_the_game:
            Boss_warg_mechanicks_go()"""
        # ---BOSSES--------------------------------------------------------------------------------
        if boss_list:
            for (i, elem) in enumerate(boss_list):
                if elem.name == "The Alpha Warg":
                    Boss_warg_mechanicks_go()
                if elem.name == "King of nazgul":
                    Boss_nazgul_mechanicks()
                if elem.name == "BossOrkConqueror":
                    label_Boss = pygame.font.Font('fonts/Fonts/RobotoMono-VariableFont_wght.ttf', 50)
                    name_label_boss = label_Boss.render('BOSSSSSS', True, 'Red')
                    screen.blit(name_label_boss, (screen.get_width() // 2 - 100, 50))
                    label_Boss = pygame.font.Font('fonts/Fonts/RobotoMono-VariableFont_wght.ttf', 10)
                    cry_label_boss = label_Boss.render(elem.cry, False, 'White')
                    hp_boss = label_Boss.render("HP BOSS: " + str(elem.hp), True, 'Red')
                    armor_boss = label_Boss.render("ARMOR BOSS: " + str(elem.armor), True, 'Red')
                    screen.blit(hp_boss, (screen.get_width() // 2 - 100, 100))

                    #screen.blit(protectiveDome, (elem.coord_x - 50, elem.coord_y - 50))
                    if elem.flag_go_to_center:
                        elem.coord_x -= 5
                        elem.anim += 1
                        screen.blit(Orc_conqueror_left[elem.anim % 3], (elem.coord_x, elem.coord_y))
                        if elem.coord_x - screen.get_width()//2 < 30:
                            elem.flag_go_to_center = False
                            pygame.time.set_timer(elem.time, 1000)
                            elem.time_definition = True
                    elif elem.flag_orc_cry:
                        screen.blit(Orc_conqueror_down[1], (elem.coord_x, elem.coord_y))
                        screen.blit(cry_label_boss, (elem.coord_x + 5 + randint(-1, 1), elem.coord_y - 5 + randint(-1, 1)))

                    elif elem.hp > 0:
                        if portal_list:
                            for port in portal_list:
                                if port.flag_to_visual:
                                    port.visual(screen, portal_png)
                        if elem.hp < 120:

                            #запускает щит и остаётся на месте
                            if elem.can_protectiveDome and elem.heal > 0:
                                print("elem.heal", elem.heal)
                                elem.can_protectiveDome = False
                                elem.flag_protective_dome_enable = True
                                elem.flag_protective_dome_unable = False
                                pygame.time.set_timer(elem.time_to_protective_enable, 5000)
                                elem.healing()
                                elem.time_to_protective_enable_DEFINITION = True


                        if abs(elem.coord_x - player_x) <= 60 and abs(elem.coord_y - player_y) <= 60:
                            player_character.hp -= elem.standart_attack()
                            player_y += 150
                            if player_character.hp <= 0:
                                 player_character.hp = 0
                                 gameplay = False

                        if abs(elem.coord_x - player_x) > 140 and abs(elem.coord_y - player_y) > 140 and elem.can_portal:
                            elem.can_portal = False
                            portal_list.append(Portal(elem.coord_x + 20, elem.coord_y, screen))
                            elem.portal1 = [elem.coord_x + 20, elem.coord_y]
                            portal_list.append(Portal(player_x, player_y, screen))
                            elem.portal2 = [player_x, player_y]
                            elem.flag_go_to_portal = True

                        if elem.flag_go_to_portal:
                            if elem.portal1[0] == elem.coord_x and elem.portal1[1] == elem.coord_y:
                                elem.flag_go_to_portal = False
                                elem.coord_x = elem.portal2[0]
                                elem.coord_y = elem.portal2[1]
                            else:
                                if abs(elem.coord_x - elem.portal1[0]) > abs(elem.coord_y - elem.portal1[1]):
                                    if elem.coord_x > elem.portal1[0]:
                                        elem.coord_x -= 4
                                        elem.anim += 1
                                        if elem.flag_protective_dome_enable:
                                            screen.blit(protectiveDome, (elem.coord_x - 50, elem.coord_y - 50))
                                        screen.blit(Orc_conqueror_left[elem.anim % 3], (elem.coord_x, elem.coord_y))
                                    else:
                                        elem.coord_x += 4
                                        elem.anim += 1
                                        if elem.flag_protective_dome_enable:
                                            screen.blit(protectiveDome, (elem.coord_x - 50, elem.coord_y - 50))
                                        screen.blit(Orc_conqueror_right[elem.anim % 3], (elem.coord_x, elem.coord_y))

                                elif abs(elem.coord_x - elem.portal1[0]) <= abs(elem.coord_y - elem.portal1[1]):
                                    if elem.coord_y > elem.portal1[1]:
                                        elem.coord_y -= 4
                                        elem.anim += 1
                                        if elem.flag_protective_dome_enable:
                                            screen.blit(protectiveDome, (elem.coord_x - 50, elem.coord_y - 50))
                                        screen.blit(Orc_conqueror_up[elem.anim % 3], (elem.coord_x, elem.coord_y))

                                    else:
                                        elem.coord_y += 4
                                        elem.anim += 1
                                        if elem.flag_protective_dome_enable:
                                            screen.blit(protectiveDome, (elem.coord_x - 50, elem.coord_y - 50))
                                        screen.blit(Orc_conqueror_down[elem.anim % 3], (elem.coord_x, elem.coord_y))

                        else:
                            if abs(elem.coord_x - player_x) > abs(elem.coord_y - player_y):
                                if elem.coord_x > player_x:
                                    elem.coord_x -= 4
                                    elem.anim += 1
                                    if elem.flag_protective_dome_enable:
                                        screen.blit(protectiveDome, (elem.coord_x - 50, elem.coord_y - 50))
                                    screen.blit(Orc_conqueror_left[elem.anim % 3], (elem.coord_x, elem.coord_y))
                                else:
                                    elem.coord_x += 4
                                    elem.anim += 1
                                    if elem.flag_protective_dome_enable:
                                      screen.blit(protectiveDome, (elem.coord_x - 50, elem.coord_y - 50))
                                    screen.blit(Orc_conqueror_right[elem.anim % 3], (elem.coord_x, elem.coord_y))

                            elif abs(elem.coord_x - player_x) <= abs(elem.coord_y - player_y):
                                if elem.coord_y > player_y:
                                    elem.coord_y -= 4
                                    elem.anim += 1
                                    if elem.flag_protective_dome_enable:
                                        screen.blit(protectiveDome, (elem.coord_x - 50, elem.coord_y - 50))
                                    screen.blit(Orc_conqueror_up[elem.anim % 3], (elem.coord_x, elem.coord_y))

                                else:
                                    elem.coord_y += 4
                                    elem.anim += 1
                                    if elem.flag_protective_dome_enable:
                                        screen.blit(protectiveDome, (elem.coord_x - 50, elem.coord_y - 50))
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
                if totem_list:
                    for (j, elem) in enumerate(totem_list):
                        if abs(ar[0].x - elem.x) < 100 and abs(ar[0].y - elem.y) < 100:
                            elem.Protect(Attack_point)
                            if elem.hp <= 0:
                                totem_list.pop(j)
                                print("Totem destroyed...")

                            if Arrow_list:
                                Arrow_list.pop(i)
                                continue
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
                        if elem.name == "King of nazgul" and elem.flag_go_to_center == False:
                            if abs(ar[0].x - elem.x) < 200 and abs(ar[0].y - elem.y) < 200 and elem.flag_invicible==False:
                                elem.y -= 50
                                if elem.armor > 0:
                                    elem.armor -= Attack_point
                                    if elem.armor < 0:
                                        elem.armor = 0
                                else:
                                    elem.hp -= Attack_point

                                if elem.hp <= 0:
                                    boss_list.pop(j)
                                    print("the King of nazgul is murdered...")
                                    num_mob -= 1
                                    wave_flag = True
                                    wave_how -= 1
                                    flag_ability = 1

                                if Arrow_list:
                                    Arrow_list.pop(i)
                                    continue
                        if elem.name == "BossOrkConqueror" and elem.flag_go_to_center == False and not elem.flag_protective_dome_enable:
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
                                    wave_flag = True
                                    wave_how -= 1

                                if Arrow_list:
                                    Arrow_list.pop(i)
                                    continue
                        elif elem.name == "BossOrkConqueror" and elem.flag_protective_dome_enable:
                            if abs(ar[0].x - elem.coord_x) < 20 and abs(ar[0].y - elem.coord_y) < 20:
                                if Arrow_list:
                                    Arrow_list.pop(i)

                        if elem.name == 'The Alpha Warg':

                            if abs(ar[0].x - elem.x) < 100 and abs(ar[0].y - elem.y) < 100:
                                if Boss_warg_Heal_flag == False:
                                    elem.y -= 50

                                if elem.armor > 0:
                                    elem.armor -= Attack_point
                                    if elem.armor < 0:
                                        elem.armor = 0
                                else:
                                    elem.Protect(Attack_point)

                                if elem.hp <= 0:
                                    boss_list.pop(j)
                                    print("the Alpha Warg is murdered...")
                                    num_mob -= 1
                                    wave_flag = True
                                    wave_how -= 1
                                    flag_ability = 1

                                if Arrow_list:
                                    Arrow_list.pop(i)
                                    continue

        visual_health(player_character)






    elif Start_game_flag == False:
        screen.fill("White")
        screen.blit(pygame.image.load("images/THE_END.png"),(0,0))
        screen.blit(loose_label, (320, 500))
        screen.blit(restart_label, (320, 400))
        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed():
            player_y = 500
            totem_list.clear()
            n_list_it_the_game.clear()
            warg_list_in_the_game.clear()
            orc_list_in_the_game.clear()
            Arrow_list.clear()
            boss_list.clear()
            Boss_warg_list_in_the_game.clear()
            player_character.hp = All_Hp
            flag_ability = 1
            Arrow_How = 0
            n_timer = pygame.USEREVENT + 1
            pygame.time.set_timer(n_timer, 10000)
            attack_timer = pygame.USEREVENT + 1
            pygame.time.set_timer(attack_timer, 1000)
            attack_flag = True
            Start_game_flag = True


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == timer_for_screensaver and flag_project_screen:
            flag_project_screen = False

        if wave_how > 0:
            if boss_list:
                for (i, elem) in enumerate(boss_list):
                    if elem.name == "BossOrkConqueror":
                        if event.type == elem.time_to_protective_enable and elem.time_to_protective_enable_DEFINITION:
                            print("внутри флага включающего щит")
                            elem.time_to_protective_enable_DEFINITION = False
                            elem.flag_protective_dome_unable = True
                            elem.flag_protective_dome_enable = False
                            pygame.time.set_timer(elem.time_to_protective_unable, 1000)
                            elem.time_to_protective_unable_DEFINITION = True

                        if event.type == elem.time_to_protective_unable and elem.time_to_protective_unable_DEFINITION:
                            print("elem.time_to_protective_Unable")
                            elem.time_to_protective_unable_DEFINITION = False
                            elem.can_protectiveDome = True


                        if elem.time_definition and event.type == elem.time:
                            print("зашел в чек клика")
                            elem.time_definition = False
                            elem.flag_orc_cry = False
                            elem.flag_boss_to_heal = True

                        if event.type == elem.time_reload_can_portal and not elem.can_portal:
                            elem.can_portal = True
                    if elem.name=="King of nazgul":
                        if event.type==elem.time_heal:
                            elem.flag_heal=True
            if portal_list:
                for (i, elem) in enumerate(portal_list):
                    if event.type == elem.time_to_visual and elem.flag_to_visual:
                        elem.flag_to_visual = False
                        portal_list.pop(i)

            if how_villians > 0:
                if event.type == n_timer:
                    num = randint(1, 3)
                    how_villians -= 1

                    if num == 1:
                        n_list_it_the_game.append(Nazgul(0))

                    elif num == 2:
                        warg_list_in_the_game.append(Warg(True,False,False,False))

                    elif num == 3:
                        orc_list_in_the_game.append(Ork(3))


            else:
                if wave_flag:
                    print("зашёл в wave_flag")
                    num_mob = randint(1, 1)
                    how_villians = num_mob
                    wave_flag = False
                    flag_create_the_boss = True

                if num_mob == 0 and flag_create_the_boss:
                    randomize_select = randint(3,3)
                    if randomize_select == 1:
                        boss_list.append(
                            BossOrkConqueror(300, 150, 70, Weapon('Boss Ork Sword', 50), Magic('Protective Dome', 5),
                                             'AAARRRRGHHH', screen.get_width() + 75, screen.get_height() // 2, 3))
                        print("create the boss")
                    elif randomize_select == 2:
                        boss_list.append(Boss_warg(100, 100, 3))
                        print("create the boss")
                    elif randomize_select==3:
                        boss_list.append(Nazgul_boss(screen.get_width()//2 + 15, 300))
                    flag_create_the_boss = False


        else:
            print("The end")
            pygame.quit()

        if event.type == n_timer and Boss_warg_ability_flag:

            if boss_list:
                for (i, elem) in enumerate(boss_list):
                    if elem.name == "The Alpha Warg":
                        elem.special_ability()

        if event.type == attack_timer:
            attack_flag = True

            attack_timer = pygame.USEREVENT + 1
            pygame.time.set_timer(attack_timer, 1000)


        if gameplay and event.type == pygame.KEYDOWN and event.key == pygame.K_r and Arrow_How > 0 and player_character.ability == "has agility" and attack_flag:
            attack_flag = False

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

        if gameplay and (player_character.ability == "is a tracker" or player_character.ability == "can a hide") and event.type == pygame.KEYDOWN and event.key == pygame.K_f and attack_flag:
            attack_flag = False
            a = player_character.Attack()
            if Attack_point <= a:
                Attack_point = a
            if totem_list:
                for (j,elem) in enumerate(totem_list):
                    if abs(elem.x - player_x) < 70 and abs(elem.y - player_y) < 70:
                        elem.Protect(Attack_point)
                    if elem.hp<=0:
                        totem_list.pop(j)
                        print("Totem destoyed...")
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
                    if elem.name == "BossOrkConqueror":
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
                                wave_flag = True
                                wave_how -= 1

                    if elem.name == "The Alpha Warg":
                        if abs(elem.x - player_x) < 70 and abs(elem.y - player_y) < 70:
                            if Boss_warg_Heal_flag == False:
                                elem.y -= 100

                            if elem.armor > 0:
                                elem.armor -= Attack_point
                                if elem.armor < 0:
                                    elem.armor = 0
                            else:
                                elem.Protect(Attack_point)

                            Attack_point = 0

                            if elem.hp <= 0:
                                boss_list.pop(j)
                                print("the Alpha Warg is murdered...")
                                flag_ability = 1
                                wave_flag = True
                                wave_how -= 1



        if gameplay and event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            player_character.Use_the_Ability()

    clock.tick(20)
