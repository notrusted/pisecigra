import threading

import pygame

from Repositories.FontRepository import FontRepository
from Repositories.ImageRepository import ImageRepository
from time import sleep


class Intro:

    @staticmethod
    def Intro(surface):
        screen_saver = ImageRepository.getImage('Back')
        screen_saver = pygame.transform.scale(screen_saver, (1000, 800))
        label = FontRepository.getFont("gwent_extrabold.ttf", 60)
        project_company = label.render("JIN Project", True, "White")
        while True:
            surface.blit(screen_saver, (0, 0))
            surface.blit(project_company, (surface.get_width() // 2 - 150, surface.get_height() // 2))
        sleep(10)