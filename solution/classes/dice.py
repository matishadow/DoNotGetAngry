from random import randint


class Dice:
    MAXIMUM_NUMBER_OF_DOTS = 6

    @staticmethod
    def throw_the_dice():
        return randint(1, 6)
