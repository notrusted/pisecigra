from random import randint

from classes.Models.Monsters.Monster import Monster
from classes.Models.Weapons.Weapon import Weapon
from file_for_class import rand_spawn


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