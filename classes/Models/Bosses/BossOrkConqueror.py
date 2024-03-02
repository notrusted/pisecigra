import pygame

from classes.Models.Bosses.Boss import Boss


class BossOrkConqueror(Boss):
    count = 0
    def __init__(self, hp, armor, dmg, weapon, magic, cry, coord_x, coord_y, heal_boss):
        Boss.__init__(self, hp, armor, dmg, weapon, magic)
        self.hp = hp
        self.name = "BossOrkConqueror"
        self.cry = cry
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.heal = heal_boss
        self.flag_go_to_center = True
        self.anim = 0
        self.flag_orc_cry = True
        self.flag_boss_to_heal = True
        self.time = pygame.USEREVENT + 1
        self.time_definition = False
        self.time_to_protective_enable = pygame.USEREVENT + 1
        self.time_to_protective_enable_DEFINITION = False
        self.time_to_protective_unable = pygame.USEREVENT + 1
        self.time_to_protective_unable_DEFINITION = False
        self.flag_protective_dome_enable = False
        self.flag_protective_dome_unable = True
        self.can_protectiveDome = True
        self.can_portal = True
        self.flag_go_to_portal = False
        self.time_reload_can_portal = pygame.USEREVENT + 1
        self.portal1 = []
        self.portal2 = []
        BossOrkConqueror.count += 1

    def healing(self):
        if self.heal > 0:
            self.heal -= 1
            self.hp += 100

    def standart_attack(self):
        return self.dmg + self.weapon.damage