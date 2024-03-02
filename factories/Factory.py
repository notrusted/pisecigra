from abc import abstractmethod, ABCMeta


class Factory:
    __metaclass__ = ABCMeta
    @abstractmethod
    @staticmethod
    def create():
        "Создать и передать одну модель"

    @abstractmethod
    @staticmethod
    def createMore(count: int):
        "Создать и передать ммножество моделей одного класса"

