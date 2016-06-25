from rpgine_comapp_danceofdragons.model.diceroller.handlers.DiceHandlerDanceOfDragons import DiceHandlerDanceOfDragons

while(True):
    debug = True

    roll_input = input("Enter number of dices to roll: ")

    dhandler = DiceHandlerDanceOfDragons()

    status, result_values, result_successes, result_subtractors, result_caused_rerolls = dhandler.roll_all_and_interpret(int(roll_input))

    if debug == True:
        """
        print("%s {INDIVIDUAL_VALUES: %s, INDIVIDUAL_SUCCESSES: %s, INDIVIDUAL_SUBTRACTORS: %s, INDIVIDUAL_REROLLS: %s}" % (
            status, result_values, result_successes, result_subtractors, result_caused_rerolls))
        """
        print("%s {INDIVIDUAL_VALUES: %s}" % (status, result_values))
        print("__________________________________")

    if debug == False:
        print(status)

#TEST