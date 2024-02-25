import pygame


class FontsRepository:
    fonts = {
        "Hardpixel": "Fonts/Hardpixel.OTF",
        "gwent_extrabold": "Fonts\gwent_extrabold.ttf",
        "Angkor-Regular": "Fonts\Angkor-Regular.ttf",
        "RobotoMono-Variable": "Fonts\RobotoMono-VariableFont_wght.ttf"
    }

    @staticmethod
    def get(self, name: str, size: int):
        return pygame.font.Font(self.fonts[name], size)
