import pygame



class Character():
    pred_rsp_hero = [0, 0]
    count_animation = 0
    attack_flag = True
    attack_timer = pygame.USEREVENT + 1
    attack_timer_DEFINITION = False
    player_x = 300
    player_y = 250

    def __init__(self, Hp, Strong, Ability, Weapon, list_animation: list):
        self.strong = Strong
        self.hp = Hp
        self.ability = Ability
        self.weapon = Weapon
        self.la = list_animation
        self.player_x = 0
        self.player_y = 0 #todo может сделать factory которая будет производить персонажей, чтобы только там менять входные параметры
    def Attack(self):
        return (self.strong + self.weapon.damage)

    def Protect(self):
        print('Try to Protect')
        print()

    def Use_the_Ability(self):
        print("use ability: ", self.ability)
        print()

    def animation(self, surf: pygame.surface.Surface, symbol: str, x, y):
        if Character.count_animation == 0:
            Character.count_animation = 1
        else:
            Character.count_animation = 0
        if symbol == "l":
            ch = 0
        elif symbol == "r":
            ch = 1
        elif symbol == "u":
            ch = 2
        elif symbol == "d":
            ch = 3
        surf.blit(self.la[ch][Character.count_animation], (x, y))

    def Player_coordinate(self):
        Character.pred_rsp_hero[0] = self.player_x
        Character.pred_rsp_hero[1] = self.player_y
        return (self.player_x, self.player_y)