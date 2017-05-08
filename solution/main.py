from classes.game_logic import Game


def user_input_func():
    inp = input()

    return inp


g = Game(4)

while True:
    g.turn(user_input_func, user_input_func)
