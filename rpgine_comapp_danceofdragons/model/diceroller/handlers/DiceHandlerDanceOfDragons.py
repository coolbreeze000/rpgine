from rpgine_comapp_danceofdragons.model.diceroller.handlers.DiceHandlerGeneric import DiceHandlerGeneric

from rpgine_comapp_danceofdragons.model.diceroller.dices.DiceTen import DiceTen

class DiceHandlerDanceOfDragons(DiceHandlerGeneric):
    DEFAULT_VALUES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    DEFAULT_SUCCESSES = [0, 8, 9]
    DEFAULT_REROLLS = [0]

    def __init__(self):
        DiceHandlerGeneric.__init__()

    def roll(self, values = DEFAULT_VALUES, successes = DEFAULT_SUCCESSES, rerolls = DEFAULT_REROLLS):
        pass