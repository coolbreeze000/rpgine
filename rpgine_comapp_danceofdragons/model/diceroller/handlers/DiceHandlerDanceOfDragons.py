from rpgine_comapp_danceofdragons.model.diceroller.handlers.DiceHandlerGeneric import DiceHandlerGeneric

class DiceHandlerDanceOfDragons(DiceHandlerGeneric):
    DEFAULT_VALUES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    DEFAULT_SUCCESSES = [0, 8, 9]
    DEFAULT_SUBTRACTORS = [1]
    DEFAULT_REROLLS = [0]

    def __init__(self):
        DiceHandlerGeneric.__init__()

    def roll(self, values = DEFAULT_VALUES):
        DiceHandlerGeneric.roll(values)

    def roll_all(self, num_dices, values = DEFAULT_VALUES, rerolls = DEFAULT_REROLLS, successes = DEFAULT_SUCCESSES, subtractors = DEFAULT_SUBTRACTORS):
        result_values = []
        result_successes = []
        result_subtractors = []
        result_caused_rerolls = []

        for i in range(0, num_dices):
            iresult = self.roll()

            result_values.append(iresult)
            result_successes.append(iresult) if iresult in successes else None
            result_subtractors.append(iresult) if iresult in subtractors else None

            while iresult in rerolls:
                result_caused_rerolls.append(iresult)
                iresult = self.roll()
                result_values.append(iresult)
                result_successes.append(iresult) if iresult in successes else None
                result_subtractors.append(iresult) if iresult in subtractors else None

        return result_values, result_successes, result_subtractors, result_caused_rerolls