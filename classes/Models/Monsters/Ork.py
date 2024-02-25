from random import randint

from classes.Models.Monsters.Monster import Monster
from classes.Models.Weapons.Weapon import Weapon
from file_for_class import rand_spawn


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