from random import randint


class Dice:
    MAXIMUM_NUMBER_OF_DOTS = 6

    def __init__(self):
        self.last_throw = -1

    def throw_the_dice(self):
        throw = randint(1, 6)
        self.last_throw = throw

        return throw

    @staticmethod
    def throw_was_maximum(throw):
        return throw == Dice.MAXIMUM_NUMBER_OF_DOTS
