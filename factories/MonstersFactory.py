from classes.Models.Monsters.Duck import Duck
from classes.Models.Monsters.Monster import Monster
from classes.Models.Monsters.Nazgul import Nazgul
from classes.Models.Monsters.Ork import Ork
from classes.Models.Monsters.Warg import Warg


class MonstersFactory:
    params_Duck = {}

    params_Nazgul = {
        "anim": 0
    }

    params_Ork = {
        "anim": 3
    }

    params_Warg = {
        "flag1": True,
        "flag2": False,
        "flag3": False,
        "flag4": False
    }

    @staticmethod
    def createMonster(type) -> Monster:
        return MonstersFactory.checkType(type)

    @staticmethod
    def createArrayMonsters(type, count: int) -> list:
        army = []
        for i in range(0, count):
            army.append(MonstersFactory.checkType(type))
        return army

    @staticmethod
    def checkType(type) -> Monster:
        if not issubclass(type, Monster):
            raise Exception("Этот класс не является монстром")

        if issubclass(type, Duck):
            return Duck()

        if issubclass(type, Nazgul):
            return Nazgul(MonstersFactory.params_Nazgul["anim"])

        if issubclass(type, Ork):
            return Ork(MonstersFactory.params_Ork["anim"])

        if issubclass(type, Warg):
            return Warg(
                MonstersFactory.params_Warg["flag1"],
                MonstersFactory.params_Warg["flag2"],
                MonstersFactory.params_Warg["flag3"],
                MonstersFactory.params_Warg["flag4"],
            )
