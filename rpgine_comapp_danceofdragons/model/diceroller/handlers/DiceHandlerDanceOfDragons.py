from rpgine_comapp_danceofdragons.model.diceroller.handlers.DiceHandlerGeneric import DiceHandlerGeneric

from rpgine_comapp_danceofdragons.model.diceroller.dices.DiceTen import DiceTen

class DiceHandlerDanceOfDragons(DiceHandlerGeneric):
    DICE_TYPES = {DiceTen.__class__}

    def __init__(self):
        DiceHandlerGeneric.__init__()