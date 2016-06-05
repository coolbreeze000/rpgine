from rpgine_core.model.RandomNumberGenerator import RandomNumberGenerator

class DiceHandlerGeneric:
    def __init__(self):
        self.ran_num_generator = RandomNumberGenerator()

    def roll(self, values):
        return self.ran_num_generator.generateTrueRandomIntegerFromValues(values)

    def roll_all(self):
        pass