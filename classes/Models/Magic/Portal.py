import pygame

from classes.Models.Magic.Magic import Magic


class Portal(Magic):
    def __init__(self, x, y, surface):
        Magic.__init__(self, "Portal", 0)
        self.flag_to_visual = True
        self.time_to_visual = pygame.USEREVENT + 1
        pygame.time.set_timer(self.time_to_visual, 5000)
        self.x = x
        self.y = y
        self.surface = surface
        self.anim = 0

    def visual(self, surface, portal_vis: list):
        if self.flag_to_visual:
            self.anim += 1
            surface.blit(portal_vis[self.anim % 4], (self.x, self.y))