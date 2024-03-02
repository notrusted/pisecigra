from random import randint

from classes.Models.Character.Character import Character
from classes.Models.Weapons.Weapon import Weapon
from file_for_images import Elf_left, Elf_right, Elf_down, Elf_up


class Elf(Character):

    def __init__(self):
        Character.__init__(self,190,30, "has agility",Weapon("Bow",30),[Elf_left,Elf_right,Elf_up,Elf_down])

    def Attack(self):
        print("The Elf attack with damage", self.strong + self.weapon.damage)
        return self.strong + self.weapon.damage

    def Protect(self):
        a = 5 * randint(0, 1)
        self.hp = self.hp + a
        print("The Elf's protect give him a " + str(a) + " Hp")

    def Use_the_Ability(self):
        global flag_ability, Arrow_How
        if flag_ability != 0:
            print("The Elf try to use him agility")
            Arrow_How += 15
        flag_ability = 0