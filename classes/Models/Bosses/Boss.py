class Boss:
    def __init__(self, hp, armor, dmg, weapon, utility):
        self.hp = hp
        self.armor = armor
        self.dmg = dmg
        self.weapon = weapon
        self.utility = utility

    def base_attack(self):
        return self.dmg