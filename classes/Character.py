from Weapon import Weapon
class Character:
    def __init__(self,Hp, Strong, Ability, Weapon):
        self.strong = Strong
        self.hp = Hp
        self.ability = Ability
        self.weapon = Weapon

    def Attack(self):
        return (self.strong + self.weapon.damage)

    def Protect(self):
        print('Try to Protect')
        print()

    def Use_the_Ability(self):
        print("use ability: ", self.ability)
        print()


class Elf(Character):

    def __init__(self):
        Character.__init__(self,90,30, "has agility",Weapon("Bow",30))


    def Attack(self):
        print("The Elf attack with damage", self.strong + self.weapon.damage)
        return self.strong + self.weapon.damage

    def Protect(self):
        a =  5 * randint(0,1)
        self.hp = self.hp + a
        print("The Elf's protect give him a " + str(a) + " Hp")

    def Use_the_Ability(self):
        global flag_ability,Arrow_How
        if flag_ability != 0:
            print("The Elf try to use him agility")
            Arrow_How += 15
        flag_ability = 0



class Human(Character):

    def __init__(self):
        Character.__init__(self,150,40, "is a tracker", Weapon("sword", 15))

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
            bonus_attack += randint(20,35)
        flag_ability = 0

class Hobbit(Character):

    def __init__(self):
        Character.__init__(self,50,70, 'can a hide', Weapon('Arnors knife', 15))

    def Attack(self):
        print( "The Hobbit attack with damage", self.strong + self.weapon.damage)
        return self.strong + self.weapon.damage

    def Protect(self):
        a = randint(0,1) * randint(1,5) * 5
        self.hp = self.hp + a
        print("The Hobbit's  protect give him a " + str(a) +' Hp')

    def Use_the_Ability(self):
        global flag_ability
        if flag_ability != 0:
            print( " The Hobbit was able to hide")
            self.hp += 15
        flag_ability = 0
