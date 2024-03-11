import pygame


class ImageRepository:

    Images = {
        'Back': 'Repositories/source/images/Back/Back.jpg'
    }

    @staticmethod
    def getImage(name: str):
        return pygame.image.load(ImageRepository.Images[name])
