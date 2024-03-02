from random import randint

from classes.Models.Character.Character import Character
from classes.Models.Weapons.Weapon import Weapon
from file_for_images import Walk_left, Walk_right, Walk_Up, Walk_Down


class Human(Character):

    def __init__(self):
        Character.__init__(self,200,40, "is a tracker", Weapon("sword", 15),[Walk_left,Walk_right,Walk_Up,Walk_Down])

    def Attack(self):
        global bonus_attack
        print("The Human attack with damage", self.strong + bonus_attack + self.weapon.damage)
        a = self.strong + bonus_attack + self.weapon.damage
        bonus_attack = 0
        return a

    def Protect(self):
        a = randint(0, 1)
        self.hp = self.hp + a * 15
        print("the Human's protect give him a  " + str(a * 15) + " Hp")

    def Use_the_Ability(self):
        global flag_ability, bonus_attack
        if flag_ability != 0:
            print('The Human Find the vulnerability')
            bonus_attack += randint(20, 35)
        flag_ability = 0