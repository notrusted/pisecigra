from random import randint
from file_for_images import *

def rand_spawn():
    rand_select = randint(1, 4)
    if rand_select == 1:
        x = randint(0, 1000)
        y = randint(-10, -2)
        return (x, y)
    elif rand_select == 2:
        x = randint(1000, 1010)
        y = randint(0, 800)
        return (x, y)
    elif rand_select == 3:
        x = randint(0, 1000)
        y = randint(1000, 1050)
        return (x, y)
    elif rand_select == 4:
        x = randint(-10, -2)
        y = randint(-10, 1000)
        return (x,y)


#-----КЛАССЫ КНОПОК------------------------------------------------------------------------------------
class Button():
    def __init__(self,Anim):
        self.anim = Anim

class Volume_button(Button):
    def __init__(self):
        self.anim = [pygame.image.load('images/buttons/Volume_on.png'),pygame.image.load('images/buttons/Volume_off.png')]
        self.rect = [self.anim[0].get_rect(topleft=(900, 720)),self.anim[1].get_rect(topleft=(900, 720))]
        self.music_mute = False
        self.timer = 0


    def music_config(self,screen):
        if self.music_mute == False:
            screen.blit(self.anim[0], (900, 720))
        else:
            screen.blit(self.anim[1], (900, 720))

    def music_disabled(self,mouse,light_button):
        if self.timer == 0:
            if self.rect[0].collidepoint(mouse) and self.music_mute == False and pygame.mouse.get_pressed() == (1, 0, 0):
                self.music_mute = True
                light_button.vol_1 = False
                light_button.vol_0_5 = False
                light_button.vol_0_2 = False
                self.timer = 5
                pygame.mixer.music.stop()

            elif self.rect[1].collidepoint(mouse) and self.music_mute and pygame.mouse.get_pressed() == (1, 0, 0):
                self.music_mute = False
                light_button.vol_1 = True
                self.timer = 5
                pygame.mixer.music.play(-1)
        else:
            self.timer = self.timer - 1



class light_button(Button):
    def __init__(self):
        self.anim = convert_list_of_images([pygame.image.load("images/buttons/Light_button.png"),pygame.image.load("images/buttons/Off_light_button.png")],1/3,1/3)
        self.rect = [self.anim[1].get_rect(topleft=(530,330)),self.anim[1].get_rect(topleft=(500,330)),self.anim[1].get_rect(topleft=(470,330))]
        self.vol_1 = True
        self.vol_0_5 = False
        self.vol_0_2 = False
        self.timer = 0


    def choice_of_level(self,Volume_button):
        if self.timer == 0:
            if self.rect[0].collidepoint(pygame.mouse.get_pos()) and Volume_button.music_mute == False and pygame.mouse.get_pressed() == (1, 0, 0) and self.vol_1 == False:
                pygame.mixer_music.set_volume(1)
                self.vol_1 = True
                self.vol_0_5 = False
                self.vol_0_2 = False
                self.timer = 10


            elif self.rect[1].collidepoint(pygame.mouse.get_pos()) and Volume_button.music_mute == False and pygame.mouse.get_pressed() == (1, 0, 0) and self.vol_0_5 == False:
                pygame.mixer_music.set_volume(0.5)
                self.vol_0_5 = True
                self.vol_1 = False
                self.vol_0_2 = False
                self.timer = 10


            elif self.rect[2].collidepoint(pygame.mouse.get_pos()) and Volume_button.music_mute == False and pygame.mouse.get_pressed() == (1, 0, 0) and self.vol_0_2 == False:
                pygame.mixer_music.set_volume(0.2)
                self.vol_0_2 = True
                self.vol_1 = False
                self.vol_0_5 = False
                self.timer = 10
        else:
            self.timer = self.timer - 1



    def level_config(self,screen):
        if self.vol_0_2:
            screen.blit(self.anim[0], (470, 330))
        else:
            screen.blit(self.anim[1], (470, 330))

        if self.vol_0_5:
            screen.blit(self.anim[0], (500, 330))
        else:
            screen.blit(self.anim[1], (500, 330))

        if self.vol_1:
            screen.blit(self.anim[0], (530, 330))
        else:
            screen.blit(self.anim[1], (530, 330))


#-------------------------------------------------------------------------------------------------------
class Weapon:
    def __init__(self, Name, Damage):
        self.name = Name
        self.damage = Damage

class Magic:
    def __init__(self, name, dmg):
        self.name = name
        self.damage = dmg
class Magic_pict:
    def __init__(self, name,spec_dmg, dmg,pict,x,y):
        self.name = name
        self.damage = dmg
        self.pict = pict
        self.x=x
        self.y=y
        self.sd=spec_dmg
    def special_attack(self,surf,x,y):
        if self.x-x>=7:
            self.x-=5
        else:
            self.x+=5
        if self.y-y>=7:
            self.y-=5
        else:
            self.y+=5
        surf.blit(*self.pict,(self.x,self.y))

class Portal(Magic):
    def __init__(self, x, y, surface):
        Magic.__init__(self, "Portal", 0)
        self.flag_to_visual = True
        self.time_to_visual = pygame.USEREVENT + 1
        pygame.time.set_timer(self.time_to_visual, 5000)
        self.x = x
        self.y = y
        self.surface = surface
        self.anim = 0

    def visual(self, surface, portal_vis: list):
        if self.flag_to_visual:
            self.anim += 1
            surface.blit(portal_vis[self.anim % 4], (self.x, self.y))


class Monster:
    def __init__(self, Hp, Armor, X, Y, Damage, Weapon, anim):
        self.anim = anim
        self.hp = Hp
        self.armor = Armor
        self.damage = Damage
        self.weapon = Weapon
        self.x = X
        self.y = Y

    def Attack(self):
        return self.damage + self.weapon.damage

    def Protect(self, dmg):
        a = randint(0, 1)
        self.hp = self.hp - dmg + dmg * a * a
class Duck(Monster):
    def __init__(self):
        Monster.__init__(self,10000,10000,0,0,10000,Weapon("Cry of Crya",1000),duck_list)
        self.char=randint(0,1)
        self.resize=1/randint(1,5)
        self.flag_duck=True
        self.animation_count=0
        self.anim=convert_list_of_images(duck_list,self.resize,self.resize)
    def spawn(self):
        if self.char==0:
            self.x=0
        if self.char==1:
            self.x=1000
        self.y=randint(100,700)
    def duck_go(self,surf):
        self.animation_count+=1
        if self.char==0:#вправо
            self.x+=5
            surf.blit(self.anim[self.animation_count%6],(self.x,self.y))
        if self.char==1:
            self.x-=5
            surf.blit(self.anim[(6-self.animation_count)%6],(self.x,self.y))
class Totem():
    def __init__(self,x,y):
        self.hp=100
        self.anim=totem_picture
        self.x=x
        self.y=y
        self.flag_spawn=True
    def spawn(self,surf):
        surf.blit(*self.anim,(self.x,self.y))
    def draw(self,surf):
        label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 25)
        heal_point = label.render("Hp: " + str(self.hp), False, "green")
        surf.blit(heal_point,(self.x,self.y-30))
    def Protect(self, dmg):
        b = dmg
        self.hp = self.hp - dmg
class Nazgul(Monster):
    count = 0
    def __init__(self, anim):
        self.anim = anim
        coord_rand = rand_spawn()
        Monster.__init__(self, randint(200, 240), randint(5, 20), coord_rand[0], coord_rand[1], randint(40, 45),
                         Weapon("Morgul's knife", randint(5, 10)), 0)
        Nazgul.count += 1

    def Attack(self):
        print('Nazgul attack with damage', self.damage + self.weapon.damage)
        return self.damage + self.weapon.damage

    def Protect(self, dmg):
        print('Nazgul try to protect')
        b = dmg
        self.hp = self.hp - dmg + (b * randint(0, 1) * randint(0, 1))


class Warg(Monster):
    count = 0
    def __init__(self,flag1,flag2,flag3,flag4):
        self.flag1 = flag1
        self.flag2 = flag2
        self.flag3 = flag3
        self.flag4 = flag4
        Monster.__init__(self, randint(130, 190), randint(0, 20), randint(100,700), -100, randint(30, 35),
                         Weapon('claws', randint(10, 15)), 0)
        Warg.count += 1

    def Attack(self):
        print('The Warg Attack with damage', self.damage + self.weapon.damage)
        return self.damage + self.weapon.damage

    def Protect(self, dmg):
        print('The Warg try to protect')
        a = randint(0, 1)
        b = dmg

        self.hp = self.hp - dmg + (b * a)


class Ork(Monster):
    count = 0

    def __init__(self, anim):
        self.anim = anim
        coord = rand_spawn()
        Monster.__init__(self, randint(150, 200), randint(1, 20), coord[0], coord[1], randint(20, 40),
                         Weapon("Pushka", randint(5, 10)), 0)
        Ork.count += 1

    def Attack(self):
        print('Ork attack with damage', self.damage + self.weapon.damage)
        return self.damage + self.weapon.damage

    def Protect(self, dmg):
        print('Ork try to protect')
        b = dmg
        self.hp = self.hp - dmg + (b * randint(0, 1) * randint(0, 1))

#------Механики мобов -------------------------------------------------------------------------------
class Mechanics_of_Mobs():
    def __init__(self,gameplay,player,screen):
        self.gameplay = gameplay
        self.player = player
        self.screen = screen

    def orc_mechanicks_go(self,orc_list_in_the_game,orc_flag,Character,player_x, player_y):
        if orc_list_in_the_game:

            for (i, elem) in enumerate(orc_list_in_the_game):
                orc_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 25)
                orc_heal_points = orc_label.render("Hp: " + str(elem.hp), False, "green")
                orc_armor = orc_label.render("Armor: " + str(elem.armor), False, "green")

                if abs(elem.x - player_x) <= 60 and abs(elem.y - player_y) <= 60:
                    self.player.hp -= elem.Attack()
                    player_y += 150
                    if self.player.hp <= 0:
                        self.player.hp = 0
                        self.gameplay = False

                elif Character.pred_rsp_hero[0] == player_x and player_y == Character.pred_rsp_hero[1]:
                    if abs(elem.x - player_x) > 5:
                        orc_flag += 1
                        if elem.x > player_x:
                            elem.x -= 4
                            elem.anim += 1
                            self.screen.blit(Orc_left[elem.anim % 3], (elem.x, elem.y))
                            self.screen.blit(orc_heal_points, (elem.x + 10, elem.y - 30))
                            self.screen.blit(orc_armor, (elem.x + 10, elem.y - 60))
                        else:
                            elem.x += 4
                            elem.anim += 1
                            self.screen.blit(Orc_right[elem.anim % 3], (elem.x, elem.y))
                            self.screen.blit(orc_heal_points, (elem.x + 10, elem.y - 30))
                            self.screen.blit(orc_armor, (elem.x + 10, elem.y - 60))
                    else:
                        orc_flag = 0
                        if elem.y > player_y:
                            elem.y -= 4
                            elem.anim += 1
                            self.screen.blit(Orc_up[elem.anim % 3], (elem.x, elem.y))
                            self.screen.blit(orc_heal_points, (elem.x + 10, elem.y - 30))
                            self.screen.blit(orc_armor, (elem.x + 10, elem.y - 60))
                        else:
                            elem.y += 4
                            elem.anim += 1
                            self.screen.blit(Orc_down[elem.anim % 3], (elem.x, elem.y))
                            self.screen.blit(orc_heal_points, (elem.x + 10, elem.y - 30))
                            self.screen.blit(orc_armor, (elem.x + 10, elem.y - 60))


                elif abs(elem.x - player_x) > abs(elem.y - player_y):
                    orc_flag += 1
                    if elem.x > player_x:
                        elem.x -= 4
                        elem.anim += 1
                        self.screen.blit(Orc_left[elem.anim % 3], (elem.x, elem.y))
                        self.screen.blit(orc_heal_points, (elem.x + 10, elem.y - 30))
                        self.screen.blit(orc_armor, (elem.x + 10, elem.y - 60))
                    else:
                        elem.x += 4
                        elem.anim += 1
                        self.screen.blit(Orc_right[elem.anim % 3], (elem.x, elem.y))
                        self.screen.blit(orc_heal_points, (elem.x + 10, elem.y - 30))
                        self.screen.blit(orc_armor, (elem.x + 10, elem.y - 60))
                elif abs(elem.x - player_x) <= abs(elem.y - player_y):
                    orc_flag = 0
                    if elem.y > player_y:
                        elem.y -= 4
                        elem.anim += 1
                        self.screen.blit(Orc_up[elem.anim % 3], (elem.x, elem.y))
                        self.screen.blit(orc_heal_points, (elem.x + 10, elem.y - 30))
                        self.screen.blit(orc_armor, (elem.x + 10, elem.y - 60))
                    else:
                        elem.y += 4
                        elem.anim += 1
                        self.screen.blit(Orc_down[elem.anim % 3], (elem.x, elem.y))
                        self.screen.blit(orc_heal_points, (elem.x + 10, elem.y - 30))
                        self.screen.blit(orc_armor, (elem.x + 10, elem.y - 60))
        x = self.player.Player_coordinate()

    def nazgul_mechanicks_go(self,n_list_it_the_game, n_flag,player_x, player_y):
        for (i, elem) in enumerate(n_list_it_the_game):
            n_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 25)
            n_heal_points = n_label.render("Hp: " + str(elem.hp), False, "green")
            n_armor = n_label.render("Armor: " + str(elem.armor), False, "green")

            if (abs(elem.x - player_x) <= 200) and (abs(elem.y - player_y) <= 200):

                if elem.x >= player_x:
                    self.screen.blit(Nazgul_attack[0], (elem.x, elem.y))
                    self.screen.blit(n_heal_points, (elem.x + 10, elem.y - 30))
                    self.screen.blit(n_armor, (elem.x + 10, elem.y - 60))
                if elem.x < player_x:
                    self.screen.blit(Nazgul_attack[1], (elem.x, elem.y))
                    self.screen.blit(n_heal_points, (elem.x + 10, elem.y - 30))
                    self.screen.blit(n_armor, (elem.x + 10, elem.y - 60))
                n_flag = False

            else:
                n_flag = True

            if elem.x - player_x <= 5:
                elem.x += 2
                if n_flag:
                    elem.anim += 1
                    self.screen.blit(Nazgul_right[elem.anim % 2], (elem.x, elem.y))
                    self.screen.blit(n_heal_points, (elem.x + 10, elem.y - 30))
                    self.screen.blit(n_armor, (elem.x + 10, elem.y - 60))

            if elem.x - player_x >= 5:
                elem.x -= 2
                if n_flag:
                    elem.anim += 1
                    self.screen.blit(Nazgul_left[elem.anim % 2], (elem.x, elem.y))
                    self.screen.blit(n_heal_points, (elem.x + 10, elem.y - 30))
                    self.screen.blit(n_armor, (elem.x + 10, elem.y - 60))

            if elem.y - player_y <= 5:
                elem.y += 2

            if elem.y - player_y >= 5:
                elem.y -= 2

            if abs(elem.x - player_x) < 50 and abs(elem.y - player_y) < 50:
                self.player.hp -= elem.Attack()
                player_y += 150
                if self.player.hp <= 0:
                    self.player.hp = 0
                    self.gameplay = False

    def warg_mechanicks_go(self,warg_list_in_the_game,player_x, player_y):

        for (i, elem1) in enumerate(warg_list_in_the_game):
            warg_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 25)
            warg_heal_points = warg_label.render("Hp: " + str(elem1.hp), False, "green")
            warg_armor = warg_label.render("Armor: " + str(elem1.armor), False, "green")

            if elem1.flag1 and elem1.y <= 1100:
                elem1.y += 15

                elem1.anim += 1
                self.screen.blit(Warg_Down[elem1.anim % 3], (elem1.x, elem1.y))
                self.screen.blit(warg_heal_points, (elem1.x + 10, elem1.y - 30))
                self.screen.blit(warg_armor, (elem1.x + 10, elem1.y - 60))

            if elem1.y > 1100 and elem1.flag1:
                a = self.player.Player_coordinate()
                elem1.x = -100
                elem1.y = a[1]
                elem1.flag1 = False
                elem1.flag2 = True

            if elem1.flag2 and elem1.x <= 900:
                elem1.x += 15

                elem1.anim += 1
                self.screen.blit(Warg_Right[elem1.anim % 2], (elem1.x, elem1.y))
                self.screen.blit(warg_heal_points, (elem1.x + 10, elem1.y - 30))
                self.screen.blit(warg_armor, (elem1.x + 10, elem1.y - 60))

            if elem1.x > 900 and elem1.flag2:
                a = self.player.Player_coordinate()
                elem1.x = a[0]
                elem1.y = 1100
                elem1.flag2 = False
                elem1.flag3 = True

            if elem1.flag3 and elem1.y >= -100:
                elem1.y -= 15

                elem1.anim += 1
                self.screen.blit(Warg_Up[elem1.anim % 2], (elem1.x, elem1.y))
                self.screen.blit(warg_heal_points, (elem1.x + 10, elem1.y - 30))
                self.screen.blit(warg_armor, (elem1.x + 10, elem1.y - 60))

            if elem1.y < -100 and elem1.flag3:
                a = self.player.Player_coordinate()
                elem1.x = 900
                elem1.y = a[1]
                elem1.flag3 = False
                elem1.flag4 = True

            if elem1.flag4 and elem1.x >= -100:
                elem1.x -= 15

                elem1.anim += 1
                self.screen.blit(Warg_Left[elem1.anim % 2], (elem1.x, elem1.y))
                self.screen.blit(warg_heal_points, (elem1.x + 10, elem1.y - 30))
                self.screen.blit(warg_armor, (elem1.x + 10, elem1.y - 60))

            if elem1.x < -100 and elem1.flag4:
                a = self.player.Player_coordinate()
                elem1.x = a[0]
                elem1.y = -100
                elem1.flag4 = False
                elem1.flag1 = True

            if abs(elem1.x - player_x) < 50 and abs(elem1.y - player_y) < 50:
                self.player.hp -= elem1.Attack()

                if player_x > elem1.x:
                    player_x -= 50



                elif player_x < elem1.x:
                    player_x += 50

                if player_y < elem1.y:
                    player_y += 50

                elif player_y > elem1.y:
                    player_y -= 50

                if self.player.hp <= 0:
                    self.player.hp = 0
                    self.gameplay = False

    def Boss_warg_mechanicks_go(self,Boss_warg,player_x,player_y):

        Boss_warg_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 25)
        Boss_warg_name = Boss_warg_label.render("The Alpha Warg", False, "green")
        Boss_warg_heal_points = Boss_warg_label.render("Hp: " + str(Boss_warg.hp), False, "green")
        Boss_warg_armor = Boss_warg_label.render("Armor: " + str(Boss_warg.armor), False, "green")

        if Boss_warg.Boss_warg_Heal_flag == False:
            if Boss_warg.Boss_warg_flag1 and Boss_warg.y <= 1100 and Boss_warg.Boss_warg_Heal_flag == False:
                Boss_warg.y += 20

                Boss_warg.anim += 1
                self.screen.blit(Boss_warg_Down[Boss_warg.anim % 3], (Boss_warg.x, Boss_warg.y))
                self.screen.blit(Boss_warg_heal_points, (Boss_warg.x + 10, Boss_warg.y - 30))
                self.screen.blit(Boss_warg_armor, (Boss_warg.x + 10, Boss_warg.y - 60))
                self.screen.blit(Boss_warg_name, (400, 20))

            if Boss_warg.y > 1100 and Boss_warg.Boss_warg_flag1:
                a = self.player.Player_coordinate()
                Boss_warg.x = -100
                Boss_warg.y = a[1]
                Boss_warg.Boss_warg_flag1 = False
                Boss_warg.Boss_warg_flag2 = True

                if Boss_warg.hp <= 100:
                    Boss_warg.Boss_warg_Heal_flag = True
                    pygame.time.set_timer(Boss_warg.timer, 100000000)
                    Boss_warg.armor += 500
                    Boss_warg.x = -100
                    Boss_warg.y = 200

            if Boss_warg.Boss_warg_flag2 and Boss_warg.x <= 900 and Boss_warg.Boss_warg_Heal_flag == False:
                Boss_warg.x += 20

                Boss_warg.anim += 1
                self.screen.blit(Boss_warg_Left[Boss_warg.anim % 2], (Boss_warg.x, Boss_warg.y))
                self.screen.blit(Boss_warg_heal_points, (Boss_warg.x + 10, Boss_warg.y - 30))
                self.screen.blit(Boss_warg_armor, (Boss_warg.x + 10, Boss_warg.y - 60))
                self.screen.blit(Boss_warg_name, (400, 20))

            if Boss_warg.x > 900 and Boss_warg.Boss_warg_flag2:
                a = self.player.Player_coordinate()
                Boss_warg.x = a[0]
                Boss_warg.y = 1100
                Boss_warg.Boss_warg_flag2 = False
                Boss_warg.Boss_warg_flag3 = True

                if Boss_warg.hp <= 100:
                    Boss_warg.Boss_warg_Heal_flag = True
                    pygame.time.set_timer(Boss_warg.timer, 100000000)
                    Boss_warg.armor += 500
                    Boss_warg.x = -100
                    Boss_warg.y = 200

            if Boss_warg.Boss_warg_flag3 and Boss_warg.y >= -100 and Boss_warg.Boss_warg_Heal_flag == False:
                Boss_warg.y -= 20

                Boss_warg.anim += 1
                self.screen.blit(Boss_warg_Up[Boss_warg.anim % 2], (Boss_warg.x, Boss_warg.y))
                self.screen.blit(Boss_warg_heal_points, (Boss_warg.x + 10, Boss_warg.y - 30))
                self.screen.blit(Boss_warg_armor, (Boss_warg.x + 10, Boss_warg.y - 60))
                self.screen.blit(Boss_warg_name, (400, 20))

            if Boss_warg.y < -100 and Boss_warg.Boss_warg_flag3:
                a = self.player.Player_coordinate()
                Boss_warg.x = 900
                Boss_warg.y = a[1]
                Boss_warg.Boss_warg_flag3 = False
                Boss_warg.Boss_warg_flag4 = True

                if Boss_warg.hp <= 100:
                    Boss_warg.Boss_warg_Heal_flag = True
                    pygame.time.set_timer(Boss_warg.timer, 100000000)
                    Boss_warg.armor += 500
                    Boss_warg.x = -100
                    Boss_warg.y = 200

            if Boss_warg.Boss_warg_flag4 and Boss_warg.x >= -100 and Boss_warg.Boss_warg_Heal_flag == False:
                Boss_warg.x -= 20

                Boss_warg.anim += 1
                self.screen.blit(Boss_warg_Right[Boss_warg.anim % 2], (Boss_warg.x, Boss_warg.y))
                self.screen.blit(Boss_warg_heal_points, (Boss_warg.x + 10, Boss_warg.y - 30))
                self.screen.blit(Boss_warg_armor, (Boss_warg.x + 10, Boss_warg.y - 60))
                self.screen.blit(Boss_warg_name, (400, 20))

            if Boss_warg.x < -100 and Boss_warg.Boss_warg_flag4:
                a = self.player.Player_coordinate()
                Boss_warg.x = a[0]
                Boss_warg.y = -100
                Boss_warg.Boss_warg_flag4 = False
                Boss_warg.Boss_warg_flag1 = True

                if Boss_warg.hp <= 100:
                    Boss_warg.Boss_warg_Heal_flag = True
                    pygame.time.set_timer(Boss_warg.timer, 100000000)
                    Boss_warg.armor += 500
                    Boss_warg.x = -100
                    Boss_warg.y = 200

            if abs(Boss_warg.x - player_x) < 50 and abs(Boss_warg.y - player_y) < 50:
                self.player.hp -= Boss_warg.base_attack()

                if player_x > Boss_warg.x:
                    player_x -= 150

                elif player_x < Boss_warg.x:
                    player_x += 150

                if player_y < Boss_warg.y:
                    player_y += 150

                elif player_y > Boss_warg.y:
                    player_y -= 150

                if self.player.hp <= 0:
                    self.player.hp = 0
                    self.gameplay = False

        if Boss_warg.hp > 150:
            Boss_warg.Boss_warg_Heal_flag = False
            Boss_warg.heal_anim = 0
            Boss_warg.Boss_warg_ability_flag = False

        if Boss_warg.Boss_warg_Heal_flag:
            Boss_warg.anim += 1

            if Boss_warg.x < 250:
                Boss_warg.x += 10
                self.screen.blit(Boss_warg_Left[Boss_warg.anim % 2], (Boss_warg.x, Boss_warg.y))
                self.screen.blit(Boss_warg_heal_points, (Boss_warg.x + 10, Boss_warg.y - 30))
                self.screen.blit(Boss_warg_armor, (Boss_warg.x + 10, Boss_warg.y - 60))
                self.screen.blit(Boss_warg_name, (400, 20))

            else:
                if Boss_warg.heal_anim != 3:
                    self.screen.blit(Boss_warg_Heal[Boss_warg.heal_anim], (Boss_warg.x, Boss_warg.y))
                    self.screen.blit(Boss_warg_heal_points, (Boss_warg.x + 10, Boss_warg.y - 30))
                    self.screen.blit(Boss_warg_armor, (Boss_warg.x + 10, Boss_warg.y - 60))
                    self.screen.blit(Boss_warg_name, (400, 20))
                    Boss_warg.heal_anim += 1
                else:
                    self.screen.blit(Boss_warg_Heal[3], (Boss_warg.x, Boss_warg.y))
                    self.screen.blit(Boss_warg_heal_points, (Boss_warg.x + 10, Boss_warg.y - 30))
                    self.screen.blit(Boss_warg_armor, (Boss_warg.x + 10, Boss_warg.y - 60))
                    self.screen.blit(Boss_warg_name, (400, 20))
                    Boss_warg.Boss_warg_ability_flag = True


    def Boss_nazgul_mechanicks(self, boss_nazgul):
        Boss_nazgul_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 25)
        Boss_nazgul_name = Boss_nazgul_label.render("King of nazguls", False, "blue")
        Boss_nazgul_heal_points = Boss_nazgul_label.render("Hp: " + str(boss_nazgul.hp), False, "green")
        Boss_nazgul_armor = Boss_nazgul_label.render("Armor: " + str(boss_nazgul.armor), False, "green")

        #screen.blit(boss_nazgul_down[0],(screen.get_width()//2,200))
        #if duck.x!=1000 or duck.x!=0:
        #    duck.duck_go(screen)
        if boss_nazgul.hp>0:
            self.screen.blit(Boss_nazgul_heal_points, (boss_nazgul.x + 10, boss_nazgul.y - 30))
            self.screen.blit(Boss_nazgul_armor, (boss_nazgul.x + 10, boss_nazgul.y - 60))
            self.screen.blit(Boss_nazgul_name, (400, 20))
            if boss_nazgul.flag_for_proza:
                boss_nazgul.proza(self.screen)
            else:
                if (boss_nazgul.hp>50 or boss_nazgul.flag_magic) and boss_nazgul.flag_invicible==False :
                    boss_nazgul.go_to(self.screen,self.player.Player_coordinate()[0],self.player.Player_coordinate()[1])
                    if abs(self.player.Player_coordinate()[0]-boss_nazgul.x)<25 and abs(self.player.Player_coordinate()[1]-boss_nazgul.y)<25:
                        self.player.hp-=boss_nazgul.standart_attack()
                elif boss_nazgul.hp<=50:
                    boss_nazgul.flag_go_to_center=True
                if boss_nazgul.flag_go_to_center:
                    boss_nazgul.go_to(self.screen,self.screen.get_width()//2,self.screen.get_height()//2)
                    if boss_nazgul.check==True:
                        boss_nazgul.flag_invicible=True
                        boss_nazgul.check=False
                        boss_nazgul.flag_go_to_center=False
                if boss_nazgul.flag_invicible:
                    if boss_nazgul.flag_totem:
                        boss_nazgul.invicible(self.screen)
                        if boss_nazgul.totem_spawn:
                            boss_nazgul.set_totem()
                            #totem_list=[Totem(boss_nazgul.x-200,boss_nazgul.y-200),Totem(boss_nazgul.x-200,boss_nazgul.y+200),Totem(boss_nazgul.x+200,boss_nazgul.y-200),Totem(boss_nazgul.x+200,boss_nazgul.y+200)]
                            boss_nazgul.totem_spawn=False
                        for i in boss_nazgul.totem_list:
                            i.spawn(self.screen)
                            i.draw(self.screen)
                        if boss_nazgul.hp<100 and len(boss_nazgul.totem_list)!=0:
                            if boss_nazgul.flag_heal:
                                boss_nazgul.hp+=5
                                boss_nazgul.flag_heal=False
                                pygame.time.set_timer(boss_nazgul.time_heal,2000)
                        else:
                            boss_nazgul.flag_invicible=False
                            boss_nazgul.totem_list.clear()
                            boss_nazgul.totem_spawn=True
                            boss_nazgul.flag_totem=False
                            pygame.time.set_timer(boss_nazgul.time_totem,20000)
                    else:
                        if not boss_nazgul.flag_magic:
                            if boss_nazgul.flag_create_magic:
                                boss_nazgul.set_magic(boss_nazgul.x,boss_nazgul.y)
                                boss_nazgul.flag_create_magic=False
                            magic=boss_nazgul.get_magic()
                            magic.special_attack(self.screen,self.player.Player_coordinate()[0],self.player.Player_coordinate()[1])
                            self.screen.blit(boss_nazgul_down[0],(boss_nazgul.x,boss_nazgul.y))
                            if abs(magic.x-self.player.Player_coordinate()[0])<=25 and abs(magic.y-self.player.Player_coordinate()[1])<=25:
                                boss_nazgul.flag_magic=True
                                self.player.hp-=magic.damage
                                if self.player.strong>=0:
                                    self.player.strong-=magic.sd
                                    print("Damage reduced by 10 points :( ...")
                                boss_nazgul.flag_invicible=False
                                boss_nazgul.flag_magic=True
                if self.player.hp <= 0:
                    self.player.hp = 0
                    self.gameplay = False

    def visual_health(self,health_model, Fullhp):

        health = self.player.hp
        section = Fullhp // 9
        level_hp = health // section
        if level_hp == 9:
            self.screen.blit(health_model[0], (100, 50))
            self.screen.blit(health_model[0], (150, 50))
            self.screen.blit(health_model[0], (200, 50))
        elif level_hp == 8:
            self.screen.blit(health_model[0], (100, 50))
            self.screen.blit(health_model[0], (150, 50))
            self.screen.blit(health_model[1], (200, 50))
        elif level_hp == 7:
            self.screen.blit(health_model[0], (100, 50))
            self.screen.blit(health_model[0], (150, 50))
            self.screen.blit(health_model[2], (200, 50))
        elif level_hp == 6:
            self.screen.blit(health_model[0], (100, 50))
            self.screen.blit(health_model[0], (150, 50))
            self.screen.blit(health_model[2], (200, 50))

        elif level_hp == 5:
            self.screen.blit(health_model[0], (100, 50))
            self.screen.blit(health_model[1], (150, 50))
            self.screen.blit(health_model[2], (200, 50))

        elif level_hp == 4:
            self.screen.blit(health_model[0], (100, 50))
            self.screen.blit(health_model[2], (150, 50))
            self.screen.blit(health_model[2], (200, 50))

        elif level_hp == 3:
            self.screen.blit(health_model[0], (100, 50))
            self.screen.blit(health_model[2], (150, 50))
            self.screen.blit(health_model[2], (200, 50))

        elif level_hp == 2:
            self.screen.blit(health_model[1], (100, 50))
            self.screen.blit(health_model[2], (150, 50))
            self.screen.blit(health_model[2], (200, 50))

        elif level_hp == 1 or health > 0:
            self.screen.blit(health_model[2], (100, 50))
            self.screen.blit(health_model[2], (150, 50))
            self.screen.blit(health_model[2], (200, 50))

#----------------------------------------------------------------------------------------------------


class Boss:
    def __init__(self, hp, armor, dmg, weapon, utility):
        self.hp = hp
        self.armor = armor
        self.dmg = dmg
        self.weapon = weapon
        self.utility = utility

    def base_attack(self):
        return self.dmg
class Nazgul_boss(Boss):
    count = 0
    count_animation=0
    def __init__(self,x,y):
        Boss.__init__(self,100,50,5,Weapon("Morgul Blade",5),Magic(";a;a;",0))
        self.x=x
        self.y=y
        self.la=[boss_nazgul_left,boss_nazgul_right,boss_nazgul_up,boss_nazgul_down]
        self.name="King of nazgul"
        self.sp=10
        self.flag_heal=True
        self.flag_invicible=False
        self.flag_go_to_center=False
        self.time_heal = pygame.USEREVENT + 1
        self.check=False
        self.flag_for_proza=True
        self.n=0
        self.totem_spawn=True
        self.time_totem = pygame.USEREVENT +1
        self.flag_totem=True
        self.flag_magic=False
        self.flag_create_magic=True
        self.totem_list=[]
        Nazgul_boss.count += 1
    def get_magic(self):
        return self.magic
    def set_magic(self,x,y):
        self.magic=Magic_pict("Cry of naxgul",10,10,magic_boss_nazgul,x,y)

    def standart_attack(self):
            return int(self.dmg+self.weapon.damage)
    def proza(self,surf):
        if self.n==255:
            self.flag_for_proza=False
        else:
            boss_nazgul_down[0].set_alpha(self.n)
            self.n+=5
        surf.blit(boss_nazgul_down[0],(self.x,self.y))
    def heal(self):
        self.hp+=5

    def invicible(self,surface):
        surface.blit(boss_nazgul_down[0],(self.x,self.y))
        invic_boss_nazgul[0].set_alpha(120)
        surface.blit(invic_boss_nazgul[0],(self.x-130,self.y-100))
    def go_to(self,sur:pygame.surface.Surface, x,y):
        if abs(self.x-x)<=11 and abs(self.y-y)<=11:
            self.check=True
        if abs(self.x-x)>11:
            if self.x-x>=11:
                self.x-=self.sp
                Nazgul_boss.animation(self,sur,"l",self.x,self.y)
            else:
                self.x+=self.sp
                Nazgul_boss.animation(self,sur,"r",self.x,self.y)
        elif abs(self.y-y)>11:
            if self.y-y>=11:
                self.y-=self.sp
                Nazgul_boss.animation(self,sur,"u",self.x,self.y)
            else:
                self.y+=self.sp
                Nazgul_boss.animation(self,sur,"d",self.x,self.y)
    def set_totem(self):
         self.totem_list=[Totem(self.x-200,self.y-200),Totem(self.x-200,self.y+200),Totem(self.x+200,self.y-200),Totem(self.x+200,self.y+200)]
    def animation(self, surf: pygame.surface.Surface, symbol: str, x, y):
        if Nazgul_boss.count_animation == 0:
            Nazgul_boss.count_animation = 1
        else:
            Nazgul_boss.count_animation = 0
        if symbol == "l":
            ch = 0
        elif symbol == "r":
            ch = 1
        elif symbol == "u":
            ch = 2
        elif symbol == "d":
                ch = 3
        surf.blit(self.la[ch][Nazgul_boss.count_animation], (x, y))




class BossOrkConqueror(Boss):
    count = 0
    def __init__(self, hp, armor, dmg, weapon, magic, cry, coord_x, coord_y, heal_boss):
        Boss.__init__(self, hp, armor, dmg, weapon, magic)
        self.hp = hp
        self.name = "BossOrkConqueror"
        self.cry = cry
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.heal = heal_boss
        self.flag_go_to_center = True
        self.anim = 0
        self.flag_orc_cry = True
        self.flag_boss_to_heal = True
        self.time = pygame.USEREVENT + 1
        self.time_definition = False
        self.time_to_protective_enable = pygame.USEREVENT + 1
        self.time_to_protective_enable_DEFINITION = False
        self.time_to_protective_unable = pygame.USEREVENT + 1
        self.time_to_protective_unable_DEFINITION = False
        self.flag_protective_dome_enable = False
        self.flag_protective_dome_unable = True
        self.can_protectiveDome = True
        self.can_portal = True
        self.flag_go_to_portal = False
        self.time_reload_can_portal = pygame.USEREVENT + 1
        self.portal1 = []
        self.portal2 = []
        BossOrkConqueror.count += 1

    def healing(self):
        if self.heal > 0:
            self.heal -= 1
            self.hp += 100

    def standart_attack(self):
        return self.dmg + self.weapon.damage


class Boss_warg(Boss):
    count = 0
    def __init__(self,x,y,anim):
        self.Boss_warg_flag1 = True
        self.Boss_warg_flag2 = False
        self.Boss_warg_flag3 = False
        self.Boss_warg_flag4 = False
        self.Boss_warg_Heal_flag = False
        self.Boss_warg_ability_flag = False
        self.heal_anim = 0
        self.name = "The Alpha Warg"
        self.anim = anim
        self.timer = pygame.USEREVENT + 1
        self.x = x
        self.y = y
        Boss.__init__(self,350,200,30,Weapon("Bloody claws",50),Magic('Growl',5))
        Boss_warg.count += 1

    def base_attack(self):
        print('The Alpha Warg attack with damage', self.dmg + self.weapon.damage)
        return self.dmg + self.weapon.damage

    def special_ability(self):
        print('The Alpha Warg try to heal...')
        a = 1
        for i in range(a):
            warg_list_in_the_game.append(Warg(True, False, False, False))
        self.hp += 2



    def Protect(self,dmg):
        print('The Alpha Warg try to protect')
        b = dmg * randint(0,1) * randint(0,1)
        if b != 0:
            self.hp += 15
        self.hp = self.hp - dmg + b


class Button:
    def __init__(self, name, position: list, x, y):
        self.name = name
        self.list_position = position
        self.flag_to_pressed = False
        self.try_to_click = False
        self.x = x
        self.y = y
        self.timer = pygame.USEREVENT + 1
        self.timer_keyup = pygame.USEREVENT + 1
        self.timer_keyup_DEFINITION = False
    def visual(self, surface):
        if self.flag_to_pressed:
            surface.blit(self.list_position[1], (self.x, self.y + 13))
        else:
            surface.blit(self.list_position[0], (self.x, self.y))

class Zelya:
    timer_spawn_zelya = pygame.USEREVENT + 1
    timer_spawn_zelya_DEFINITION = False
    zelya_list = []
    def __init__(self, name, points, anim: list, x, y):
        self.name = name
        self.points = points
        self.anim = anim
        self.anim_count = 0
        self.x = x
        self.y = y
        self.timer_for_give = pygame.USEREVENT
        pygame.time.set_timer(self.timer_for_give, 4000, 1)
        self.timer_for_give_DEFINITION = False

    def visual(self, surface):
        self.anim_count %= len(self.anim)
        surface.blit(self.anim[self.anim_count], (self.x, self.y))
        self.anim_count += 1


warg_list_in_the_game = []
