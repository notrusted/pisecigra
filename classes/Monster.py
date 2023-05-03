from random import *
from classes.Character import *
from classes.Weapon import *
class Monster:
    def __init__(self, Hp, Armor, X,Y, Damage, Weapon):
        self.hp = Hp
        self.armor = Armor
        self.damage = Damage
        self.weapon = Weapon
        self.x = X
        self.y = Y

    def Attack(self):
        return self.damage

    def Protect(self, dmg):
        a = randint(0, 1)
        self.hp = self.hp - dmg + dmg * a * a


class Nazgul(Monster):
    def __init__(self):
        Monster.__init__(self, randint(20, 50),  randint(5, 20), 250,-100,randint(1,15),"Sword")


    def Attack(self):
        print('Nazgul attack with damage', self.damage + self.weapon.damage)
        return self.damage + self.weapon.damage

    def Protect(self, dmg):
        print('Nazgul try to protect')
        b = dmg
        self.hp = self.hp - dmg + (b * randint(0, 1) * randint(0, 1))
