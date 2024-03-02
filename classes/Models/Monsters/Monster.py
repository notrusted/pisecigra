from random import randint


class Monster:
    def __init__(self, Hp, Armor, X, Y, Damage, Weapon, anim):
        self.anim = anim
        self.hp = Hp
        self.armor = Armor
        self.damage = Damage
        self.weapon = Weapon
        self.x = X
        self.y = Y

    def Attack(self):
        return self.damage + self.weapon.damage

    def Protect(self, dmg):
        a = randint(0, 1)
        self.hp = self.hp - dmg + dmg * a * a