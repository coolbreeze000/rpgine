import re

from rpgine_comapp_danceofdragons.model.diceroller.handlers.DiceHandlerDanceOfDragons import DiceHandlerDanceOfDragons

debug = True

dhandler = DiceHandlerDanceOfDragons()

while(True):
    try:
        roll_input = input("Enter number of dices to roll: ")

        if re.compile('^\d{1,}$').match(roll_input):
            status, result_values, result_successes, result_subtractors, result_caused_rerolls = dhandler.roll_all_and_interpret(
                int(roll_input))

            if debug == True:
                """
                print("%s {INDIVIDUAL_VALUES: %s, INDIVIDUAL_SUCCESSES: %s, INDIVIDUAL_SUBTRACTORS: %s, INDIVIDUAL_REROLLS: %s}" % (
                    status, result_values, result_successes, result_subtractors, result_caused_rerolls))
                """
                print("%s {INDIVIDUAL_VALUES: %s}" % (status, result_values))
                print("__________________________________")

            if debug == False:
                print(status)
        elif re.compile('^\d{1,}\*\d{1,}$').match(roll_input):
            num_dices, num_rolls = roll_input.split('*', 2)

            sum_successes = 0

            for i in range(0, int(num_rolls)):
                status, result_values, result_successes, result_subtractors, result_caused_rerolls = dhandler.roll_all_and_interpret(
                    int(num_dices))

                sum_successes += len(result_successes) - len(result_subtractors)

                if debug == True:
                    print("%s {INDIVIDUAL_VALUES: %s}" % (status, result_values))

                if debug == False:
                    print(status)

            print("TOTAL SUCCESSES: %s" % (sum_successes))
    except:
        print("ERROR!")