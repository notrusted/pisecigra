import pygame

from classes.Menu.Button import Button
from file_for_images import convert_list_of_images


class light_button(Button):
    def __init__(self):
        self.anim = convert_list_of_images([pygame.image.load("Repositories/source/images/buttons/Light_button.png"),pygame.image.load("Repositories/source/images/buttons/Off_light_button.png")],1/3,1/3)
        self.rect = [self.anim[1].get_rect(topleft=(530,330)),self.anim[1].get_rect(topleft=(500,330)),self.anim[1].get_rect(topleft=(470,330))]
        self.vol_1 = True
        self.vol_0_5 = False
        self.vol_0_2 = False
        self.timer = 0


    def choice_of_level(self,Volume_button):
        if self.timer == 0:
            if self.rect[0].collidepoint(pygame.mouse.get_pos()) and Volume_button.music_mute == False and pygame.mouse.get_pressed() == (1, 0, 0) and self.vol_1 == False:
                pygame.mixer_music.set_volume(1)
                self.vol_1 = True
                self.vol_0_5 = False
                self.vol_0_2 = False
                self.timer = 10


            elif self.rect[1].collidepoint(pygame.mouse.get_pos()) and Volume_button.music_mute == False and pygame.mouse.get_pressed() == (1, 0, 0) and self.vol_0_5 == False:
                pygame.mixer_music.set_volume(0.5)
                self.vol_0_5 = True
                self.vol_1 = False
                self.vol_0_2 = False
                self.timer = 10


            elif self.rect[2].collidepoint(pygame.mouse.get_pos()) and Volume_button.music_mute == False and pygame.mouse.get_pressed() == (1, 0, 0) and self.vol_0_2 == False:
                pygame.mixer_music.set_volume(0.2)
                self.vol_0_2 = True
                self.vol_1 = False
                self.vol_0_5 = False
                self.timer = 10
        else:
            self.timer = self.timer - 1



    def level_config(self,screen):
        if self.vol_0_2:
            screen.blit(self.anim[0], (470, 330))
        else:
            screen.blit(self.anim[1], (470, 330))

        if self.vol_0_5:
            screen.blit(self.anim[0], (500, 330))
        else:
            screen.blit(self.anim[1], (500, 330))

        if self.vol_1:
            screen.blit(self.anim[0], (530, 330))
        else:
            screen.blit(self.anim[1], (530, 330))
