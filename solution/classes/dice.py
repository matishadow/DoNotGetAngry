from random import randint


class Dice:
    MAXIMUM_NUMBER_OF_DOTS = 6

    def __init__(self):
        self.last_throw = None

    def throw_the_dice(self, decision_was_valid, confirm_callback):

        if decision_was_valid:
            throw = randint(1, 6)
            self.last_throw = throw
        else:
            throw = self.last_throw
        confirm_callback()
        return throw

    @staticmethod
    def throw_was_maximum(throw):
        return throw == Dice.MAXIMUM_NUMBER_OF_DOTS
