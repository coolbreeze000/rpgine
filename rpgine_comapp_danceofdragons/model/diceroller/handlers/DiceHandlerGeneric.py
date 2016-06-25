from rpgine_core.model.RandomNumberGenerator import RandomNumberGenerator

class DiceHandlerGeneric:
    DEFAULT_VALUES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self):
        self.ran_num_generator = RandomNumberGenerator()

    def roll(self, values = DEFAULT_VALUES):
        return self.ran_num_generator.generateTrueRandomIntegerFromValues(values)

    def roll_all(self):
        pass