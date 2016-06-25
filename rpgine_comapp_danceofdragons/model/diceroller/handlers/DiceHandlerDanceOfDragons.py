from rpgine_comapp_danceofdragons.model.diceroller.handlers.DiceHandlerGeneric import DiceHandlerGeneric

import sys

class DiceHandlerDanceOfDragons(DiceHandlerGeneric):
    DEFAULT_VALUES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    DEFAULT_SUCCESSES = [0, 8, 9]
    DEFAULT_SUBTRACTORS = [1]
    DEFAULT_REROLLS = [0]

    def __init__(self):
        super(DiceHandlerDanceOfDragons, self).__init__()

    def roll(self, values = DEFAULT_VALUES):
        return super(DiceHandlerDanceOfDragons, self).roll(values)

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

    def roll_all_and_interpret(self, num_dices, values = DEFAULT_VALUES, rerolls = DEFAULT_REROLLS, successes = DEFAULT_SUCCESSES, subtractors = DEFAULT_SUBTRACTORS):
        status = None

        result_values, result_successes, result_subtractors, result_caused_rerolls = self.roll_all(num_dices, values, rerolls, successes, subtractors)

        real_successes = len(result_successes) - len(result_subtractors)

        if len(result_successes) > 0 and (len(result_successes) - len(result_subtractors)) > 0:
            status = "SUCCESS(%s) with %s successes and %s subtractors" % (real_successes, len(result_successes), len(result_subtractors))
        elif len(result_successes) > 0 and (len(result_successes) - len(result_subtractors)) < 0:
            status = "NEGATIVE SUCCESS with %s successes and %s subtractors" % (len(result_successes), len(result_subtractors))
        elif len(result_successes) == 0 and (len(result_successes) - len(result_subtractors)) < 0:
            status = "BOTCH with %s successes and %s subtractors" % (len(result_successes), len(result_subtractors))
        elif (len(result_successes) - len(result_subtractors)) == 0:
            status = "FAILURE with %s successes and %s subtractors" % (len(result_successes), len(result_subtractors))

        return status, result_values, result_successes, result_subtractors, result_caused_rerolls

    def roll_all_rounds(self, num_dices, num_rounds, difficulty, values = DEFAULT_VALUES, rerolls = DEFAULT_REROLLS, successes = DEFAULT_SUCCESSES, subtractors = DEFAULT_SUBTRACTORS):
        sum_successes = 0

        if not str.isdigit(num_rounds):
            num_rounds = sys.maxsize**10 #only temporary, should be done with itertools.count

        for i in range(0, num_rounds):
            result_values, result_successes, result_subtractors, result_caused_rerolls = self.roll_all(num_dices,
                                                                                                       values,
                                                                                                       rerolls,
                                                                                                       successes,
                                                                                                       subtractors)

            sum_successes += result_successes - result_subtractors