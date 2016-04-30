from rpgine_coreapp_dices.model.dices.DiceType import DiceType

__author__ = 'dominik'

class GenericDice:
    def __init__(self, name: str, type: DiceType):
        self.name = name
        self.type = type

    def __repr__(self):
        pass

    def __str__(self):
        pass