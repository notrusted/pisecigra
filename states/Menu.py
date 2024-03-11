import threading
from time import sleep

from Repositories.ImageRepository import ImageRepository
from classes.Menu.Button_old.Button import Button
from file_for_images import button_play_up, button_play_down, button_options_up, button_options_down, button_quit_up, \
    button_quit_down


class Menu:


    @staticmethod
    def menuInit(pygameInited, screen):
        thrdRender = threading.Thread(target=Menu.Render, args=(pygameInited, screen,),)
        thrdRender.start()
        thrdRender.join()

    @staticmethod
    def Logic(pygameInited, screen, buttons_main_menu: list):
        pygame = pygameInited
        current = None
        while True:
            for (i, elem) in enumerate(buttons_main_menu):
                elem_rect = elem.list_position[0].get_rect(topleft=(elem.x, elem.y))
                if elem_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed() == (1, 0, 0):
                    elem.flag_to_pressed = True
                elif elem_rect.collidepoint(pygame.mouse.get_pos()) and elem.flag_to_pressed and pygame.mouse.get_pressed() == (0, 0, 0):
                    elem.flag_to_pressed = False
                    sleep(0.2)
                    return
                else:
                    elem.flag_to_pressed = False







    @staticmethod
    def Render(pygameInited, screen):
        pygame = pygameInited
        button_play = Button("play", [button_play_up, button_play_down], 60, 100)
        button_options = Button('options', [button_options_up, button_options_down], 60, 225)
        button_quit = Button('quit', [button_quit_up, button_quit_down], 60, 350)
        buttons_main_menu = [button_play, button_options, button_quit]
        thrdLogic = threading.Thread(target=Menu.Logic, args=(pygame, screen, buttons_main_menu))
        thrdLogic.start()
        screen_saver = ImageRepository.getImage('Back')
        screen_saver = pygameInited.transform.scale(screen_saver, (1000, 800))

        while thrdLogic.is_alive():
            screen.blit(screen_saver, (0, 0))
            label = pygame.font.Font('Repositories/source/fonts/gwent_extrabold.ttf', 30)
            Game_Name = label.render("The Hobbit: Pyton's Adventure", False, "Black")
            screen.blit(Game_Name, (50, 50))
            for elem in buttons_main_menu:
                elem.visual(screen)

