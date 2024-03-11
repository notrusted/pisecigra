import pygame
from states.Intro import Intro
from states.Menu import Menu


class MainController:

    allObjects = {

    }

    allFlags = {
        'Start_game_flag' : False,
        'gameplay' : False,

    }
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.clock.tick(30)
        #self.monsterFactory = MonstersFactory
        self.screen = pygame.display.set_mode((1000, 800))


    def Init(self):

        Intro.Intro(self.screen)
        Menu.menuInit(self.screen)

"""
    def Update(self):
        #todo

    def eventsListener(self):
        #todo
"""