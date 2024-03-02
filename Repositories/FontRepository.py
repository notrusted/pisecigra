import pygame


class FontRepository:
    Fonts = {
        "RobotoMono-VariableFont_wght.ttf": "Repositories/source/fonts/RobotoMono-VariableFont_wght.ttf",
        "Hardpixel.OTF": "Repositories/source/fonts/gwent_extrabold.ttf",
        "Angkor-Regular.ttf": "Repositories//source/fonts/Angkor-Regular.ttf",
        "gwent_extrabold.ttf": "Repositories//source/fonts/gwent_extrabold.ttf"
    }

    @staticmethod
    def getFont(name: str, size: int):
        return pygame.font.Font(FontRepository.Fonts[name], size)
