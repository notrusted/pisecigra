import pygame

from classes.Menu.Button import Button


class Volume_button(Button):
    def __init__(self):
        self.anim = [pygame.image.load('Repositories/source/images/buttons/Volume_on.png'),pygame.image.load('Repositories/source/images/buttons/Volume_off.png')]
        self.rect = [self.anim[0].get_rect(topleft=(900, 720)),self.anim[1].get_rect(topleft=(900, 720))]
        self.music_mute = False
        self.timer = 0


    def music_config(self,screen):
        if self.music_mute == False:
            screen.blit(self.anim[0], (900, 720))
        else:
            screen.blit(self.anim[1], (900, 720))

    def music_disabled(self,mouse,light_button):
        if self.timer == 0:
            if self.rect[0].collidepoint(mouse) and self.music_mute == False and pygame.mouse.get_pressed() == (1, 0, 0):
                self.music_mute = True
                light_button.vol_1 = False
                light_button.vol_0_5 = False
                light_button.vol_0_2 = False
                self.timer = 5
                pygame.mixer.music.stop()

            elif self.rect[1].collidepoint(mouse) and self.music_mute and pygame.mouse.get_pressed() == (1, 0, 0):
                self.music_mute = False
                light_button.vol_1 = True
                self.timer = 5
                pygame.mixer.music.play(-1)
        else:
            self.timer = self.timer - 1