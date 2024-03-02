import pygame

from classes.Models.Bosses.Boss import Boss
from classes.Models.Enviroments.Totem import Totem
from classes.Models.Magic.Magic import Magic
from classes.Models.Magic.Magic_pict import Magic_pict
from classes.Models.Weapons.Weapon import Weapon
from file_for_images import invic_boss_nazgul, boss_nazgul_down, magic_boss_nazgul, boss_nazgul_left, boss_nazgul_right, \
    boss_nazgul_up


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