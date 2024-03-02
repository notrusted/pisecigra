from random import randint

from classes.Models.Monsters.Monster import Monster
from classes.Models.Weapons.Weapon import Weapon


class Ork(Monster):
    count = 0

    def __init__(self, anim):
        self.anim = anim
        coord = self.rand_spawn()
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