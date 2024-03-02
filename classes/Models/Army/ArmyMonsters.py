from factories.MonstersFactory import MonstersFactory


class ArmyMonsters:

    def __init__(self, type):
        self.army = []
        self.type = type

    def addMonster(self):
        self.army.append(MonstersFactory.createMonster(self.type))

    def deleteMonster(self, index: int):
        self.army.pop(index)