import pygame


class Zelya:
    timer_spawn_zelya = pygame.USEREVENT + 1
    timer_spawn_zelya_DEFINITION = False
    zelya_list = []

    def __init__(self, name, points, anim: list, x, y):
        self.name = name
        self.points = points
        self.anim = anim
        self.anim_count = 0
        self.x = x
        self.y = y
        self.timer_for_give = pygame.USEREVENT
        pygame.time.set_timer(self.timer_for_give, 4000, 1)
        self.timer_for_give_DEFINITION = False

    def visual(self, surface):
        self.anim_count %= len(self.anim)
        surface.blit(self.anim[self.anim_count], (self.x, self.y))
        self.anim_count += 1