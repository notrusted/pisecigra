import pygame
from random import randint
from file_for_images import *
class Weapon:
    def __init__(self, Name, Damage):
        self.name = Name
        self.damage = Damage

class Magic:
    def __init__(self, name, dmg):
        self.name = name
        self.damage = dmg

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
    def __init__(self, anim):
        self.anim = anim
        Monster.__init__(self, randint(200, 240), randint(5, 20), 250, -100, randint(40, 45),
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
        Monster.__init__(self, randint(130, 190), randint(0, 20), randint(100,700), -100, randint(30, 35),
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
        Monster.__init__(self, randint(150, 200), randint(1, 20), 0, 0, randint(20, 40),
                         Weapon("Pushka", randint(5, 10)), 0)

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
class Nazgul_boss(Boss):
    count_animation=0
    def __init__(self,x,y):
        Boss.__init__(self,100,50,5,Weapon("Morgul Blade",5),Magic("cry of the Nazgull",10))
        self.x=x
        self.y=y
        self.la=[boss_nazgul_left,boss_nazgul_right,boss_nazgul_up,boss_nazgul_down]
        self.name="King of nazgul"
        self.sp=10
        self.flag_heal=True
        self.flag_invicible=False
        self.flag_go_to_center=False
        #self.time_invic = pygame.USEREVENT + 1
        self.time_heal = pygame.USEREVENT + 1
        self.check=False
        self.flag_for_proza=True
        self.n=0
        self.totem_spawn=True
    def standart_attack(self,screen,x,y):
            return int(self.dmg+self.weapon.damage)
    def special_attack(self,speed):
        speed-=5
        return self.utility.damage
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
        #self.armor=1000
        surface.blit(boss_nazgul_down[0],(self.x,self.y))
        invic_boss_nazgul[0].set_alpha(120)
        surface.blit(invic_boss_nazgul[0],(self.x-130,self.y-100))#self.y-100
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

    def healing(self):
        if self.heal > 0:
            self.heal -= 1
            self.hp += 100

    def standart_attack(self):
        return self.dmg + self.weapon.damage






class Boss_warg(Boss):
    def __init__(self,x,y,anim):
        self.name = "The Alpha Warg"
        self.anim = anim
        self.x = x
        self.y = y
        Boss.__init__(self,350,200,30,Weapon("Bloody claws",50),Magic('Growl',5))

    def base_attack(self):
        print('The Alpha Warg attack with damage', self.dmg + self.weapon.damage)
        return self.dmg + self.weapon.damage

    def special_ability(self):
        print('The Alpha Warg try to heal...')
        a = randint(1, 3)
        for i in range(a):
            warg_list_in_the_game.append(Warg(True, False, False, False))
        self.hp += 15



    def Protect(self,dmg):
        print('The Alpha Warg try to protect')
        b = dmg * randint(0,1) * randint(0,1)
        if b != 0:
            self.hp += 15
        self.hp = self.hp - dmg + b



warg_list_in_the_game = []
