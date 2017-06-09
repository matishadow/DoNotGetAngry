from enum import Enum


class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2
    YELLOW = 3


class UserDecision(Enum):
    OUT = 0
    MOVE = 1


class ServerState(Enum):
    INIT = 0
    LOBBY_READY = 1
    GAME_START = 2
