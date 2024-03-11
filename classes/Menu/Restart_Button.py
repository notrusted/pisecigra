import pygame

from classes.Menu.Button import Button
from file_for_images import convert_list_of_images

class Restart_Button(Button):
    def __init__(self):
        self.anim = convert_list_of_images([pygame.image.load("Repositories/source/images/buttons/Restart_button.png"),pygame.image.load("Repositories/source/images/buttons/Restart_button_pressed.png")],1,1)
        self.rect = self.anim[0].get_rect(topleft=(320, 450))
        self.flag_to_restart = False
        self.timer = pygame.USEREVENT + 1
        self.base_label = pygame.font.Font("Repositories/source/fonts/gwent_extrabold.ttf", 50)
        self.restart_label = self.base_label.render("Restart", False, "White")
        self.click_sound = pygame.mixer.Sound('Sounds/click.wav')

    def Restart_button_print(self,screen):
        if not self.flag_to_restart:
            screen.blit(self.anim[0],(380,450))
            screen.blit(self.restart_label,(408,475))

        else:
            screen.blit(self.anim[1],(380,450))
            screen.blit(self.restart_label, (408, 475))

    def Restart_button_control(self,mouse):
        if not self.flag_to_restart:
            if self.rect.collidepoint(mouse) and pygame.mouse.get_pressed() == (1, 0, 0):
                self.click_sound.play()
                self.flag_to_restart = True
                pygame.time.set_timer(self.timer, 100000000)
                return False


        elif self.timer:
            self.flag_to_restart = False
            return True




