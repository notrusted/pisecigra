from factories.MonstersFactory import MonstersFactory
from classes.Models.Monsters.Ork import Ork
from classes.Models.Monsters.Nazgul import Nazgul
from classes.Models.Monsters.Warg import Warg
class ArmyMonsters:

    def __init__(self):
        self.army_of_orks = []
        self.army_of_nazguls = []
        self.army_of_wargs = []

    def addMonster(self,type):
        if type == "ork":
            self.army_of_orks.append(Ork(3))

        elif type == "nazgul":
            self.army_of_nazguls.append((Nazgul(0)))

        elif type == "warg":
            self.army_of_wargs.append(Warg(True, False, False, False))

    def deleteMonster(self, index: int,type):
        if type == "ork":
            self.army_of_orks.pop(index)

        elif type == "nazgul":
            self.army_of_nazguls.pop(index)

        elif type == "warg":
            self.army_of_wargs.pop(index)
