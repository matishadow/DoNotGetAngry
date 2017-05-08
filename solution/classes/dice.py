from random import randint


class Dice:
    @staticmethod
    def throw_the_dice():
        return randint(1, 6)
