from random import randint

from classes.Models.Monsters.Monster import Monster
from classes.Models.Weapons.Weapon import Weapon
from file_for_images import convert_list_of_images, duck_list


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