from enum import Enum


class Color(Enum):
    BLUE = 0
    RED = 1
    GREEN = 2
    YELLOW = 3


class UserDecision(Enum):
    OUT = 0
    MOVE = 1


class ServerState(Enum):
    INIT = 0
    LOBBY_READY = 1
    GAME_START = 2
