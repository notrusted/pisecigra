from classes.Models.Monsters.Monster import Monster
from classes.Models.Monsters.Ork import Ork
from factories.Factory import Factory


class OrcFactory(Factory):
    base_parametr = {
        "Anim": 3
    }

    @staticmethod
    def create() -> Monster:
        return Ork(OrcFactory.base_parametr["Anim"])

    @staticmethod
    def createMore(count: int) -> list:
        armyOrcs = []
        for i in range(0, count):
            armyOrcs.append(OrcFactory.create())
        return armyOrcs
