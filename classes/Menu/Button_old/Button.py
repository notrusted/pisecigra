import pygame


class Button:
    def __init__(self, name, position: list, x, y):
        self.name = name
        self.list_position = position
        self.flag_to_pressed = False
        self.try_to_click = False
        self.x = x
        self.y = y
        self.timer = pygame.USEREVENT + 1
        self.timer_keyup = pygame.USEREVENT + 1
        self.timer_keyup_DEFINITION = False
    def visual(self, surface):
        if self.flag_to_pressed:
            surface.blit(self.list_position[1], (self.x, self.y + 13))
        else:
            surface.blit(self.list_position[0], (self.x, self.y))