from random import SystemRandom

__author__ = 'dominik'

class RandomNumberGenerator:
    def __init__(self):
        self.sysrandom = SystemRandom()

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def generateTrueRandom(self, start: int, stop: int, step: int = 1):
        return self.sysrandom.randrange(start, stop, step)

    def generateTrueRandomInteger(self, start: int, stop: int):
        return self.sysrandom.randint(start, stop)