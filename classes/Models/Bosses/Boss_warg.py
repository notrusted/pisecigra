from random import randint

import pygame

from classes.Models.Bosses.Boss import Boss
from classes.Models.Magic.Magic import Magic
from classes.Models.Monsters.Warg import Warg
from classes.Models.Weapons.Weapon import Weapon


class Boss_warg(Boss):
    count = 0

    def __init__(self, x, y, anim):
        self.name = "The Alpha Warg"
        self.anim = anim
        self.timer = pygame.USEREVENT + 1
        self.x = x
        self.y = y
        Boss.__init__(self, 350, 200, 30, Weapon("Bloody claws", 50), Magic('Growl', 5))
        Boss_warg.count += 1

    def base_attack(self):
        print('The Alpha Warg attack with damage', self.dmg + self.weapon.damage)
        return self.dmg + self.weapon.damage

    def special_ability(self):
        print('The Alpha Warg try to heal...')
        a = 1
        for i in range(a):
            warg_list_in_the_game.append(Warg(True, False, False, False)) #todo сделать либо отдельный класс для множества волков, либо сделать этот массив полем
        self.hp += 2

    def Protect(self,dmg):
        print('The Alpha Warg try to protect')
        b = dmg * randint(0, 1) * randint(0, 1)
        if b != 0:
            self.hp += 15
        self.hp = self.hp - dmg + b