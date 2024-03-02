from random import randint

from classes.Models.Monsters.Monster import Monster
from classes.Models.Weapons.Weapon import Weapon


class Nazgul(Monster):
    count = 0
    def __init__(self, anim):
        self.anim = anim
        coord_rand = self.rand_spawn()
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

    def rand_spawn(self):
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
            return (x, y)