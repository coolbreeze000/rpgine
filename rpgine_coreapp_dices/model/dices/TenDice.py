from rpgine_coreapp_dices.model.dices.GenericDice import GenericDice
from rpgine_coreapp_dices.model.dices.DiceType import DiceType

__author__ = 'dominik'

class TenDice(GenericDice):
    def __init__(self, name: str, type: DiceType):
        GenericDice.__init__(self, name, type)

        def __repr__(self):
            pass

        def __str__(self):
            pass