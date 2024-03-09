from random import randint

from classes.Models.Character.Character import Character
from classes.Models.Weapons.Weapon import Weapon
from file_for_images import Hobba_left, Hobba_right, Hobba_down, Hobba_up



class Hobbit(Character):

    def __init__(self):
        Character.__init__(self,150,70, 'can a hide', Weapon('Arnors knife', 15),[Hobba_left,Hobba_right,Hobba_up,Hobba_down])

    def Attack(self):
        print("The Hobbit attack with damage", self.strong + self.weapon.damage)
        return self.strong + self.weapon.damage

    def Protect(self):
        a = randint(0, 1) * randint(1, 5) * 5
        self.hp = self.hp + a
        print("The Hobbit's  protect give him a " + str(a) + ' Hp')

    def Use_the_Ability(self):
        global flag_ability
        if flag_ability != 0:
            print(" The Hobbit was able to hide")
            self.hp += 15
        flag_ability = 0