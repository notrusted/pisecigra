from random import randint

import pygame

from classes.Models.Bosses.Boss import Boss
from classes.Models.Magic.Magic import Magic
from classes.Models.Monsters.Warg import Warg
from classes.Models.Weapons.Weapon import Weapon



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

    def special_ability(self,Mob_Army):
        print('The Alpha Warg try to heal...')
        a = 1
        for i in range(a):
            Mob_Army.addMonster("warg")
        self.hp += 2



    def Protect(self,dmg):
        print('The Alpha Warg try to protect')
        b = dmg * randint(0,1) * randint(0,1)
        if b != 0:
            self.hp += 15
        self.hp = self.hp - dmg + b

