from rpgine_comapp_danceofdragons.model.diceroller.dices.DiceGeneric import DiceGeneric

class DiceTen(DiceGeneric):
    VALUES = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

    def __init__(self):
        DiceGeneric.__init__()