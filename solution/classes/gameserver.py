# ------------SERVER---------
#
# -------------LOBBY---------
# 1.stworzenie listy lobby
# 2.wysłanie dostępnych lobby/slotów
# 3.generacja hasha gracza
# 4.akceptacja wyboru slotu
# 5.decyzja o starcie gry
# -------------GRA-----------
# 6.wysłanie stanu planszy
# 7.przekazywanie tokena tury
# 8.odbieranie ruchu i walidacja
# 9.akceptacja ruchu
# 10.brak akceptacji
# 11.wygrana
from xmlrpc.server import SimpleXMLRPCServer
from random import *
from classes.enums import *
from classes.game import Game
from classes.dice import Dice
from classes.counter import *
from classes import *


class GameServer:
    def __init__(self, address ="localhost", port= 8003):
        self.address = address
        self.port = port
        self.timeout = 300
        self.server_state = ServerState['INIT']

        self.lobby = [False,
                      False,
                      False,
                      False]

        self.ready = [False,
                      False,
                      False,
                      False]

        g = None  # instancja Game

        self.playercount = 0
        self.server = SimpleXMLRPCServer((self.address, self.port), allow_none=True)

        self.register_functions()
        self.server_state = ServerState["LOBBY_READY"]
        print(self.check_state())

        self.server.serve_forever()

    # --------------------------------------------

    def register_functions(self):
        # generalne funkcje, podlączenie
        self.server.register_introspection_functions()
        self.server.register_function(self.check_state)
        self.server.register_function(self.list_lobby)
        self.server.register_function(self.list_ready)
        self.server.register_function(self.connect_to_lobby)
        self.server.register_function(self.set_ready)
        self.server.register_function(self.start_game)
        # funcje gry:
        self.server.register_function(self.check_board)
        self.server.register_function(self.check_dice)
        self.server.register_function(self.check_current_color)
        self.server.register_function(self.move)
        # server.register_function()
        return

    def check_playerid(self, playerid):  # wewnetrzna uniwersalna fkcja weryfikujaca gracza
        for index in range(len(self.lobby)):
            if (self.lobby[index] == playerid):
                return index  # zwraca kolor/slotu
        print("Nie ma takiego gracza w Lobby")
        return None  # gdy nie ma go w lobby

    def lobby_player_color(self, playerid):
        """zwraca kolor,dla gracza o danym id"""
        for index in range(len(self.lobby)):
            if (self.lobby[index] == playerid):
                return Color(index)
        return None

    def finish(self):
        server_state = ServerState['LOBBY_READY']
        # zeruję wszystkie zmienne
        self.lobby = [False,
                      False,
                      False,
                      False]

        self.ready = [False,
                      False,
                      False,
                      False]

        self.playercount = 0
        return

    # ----------------- RPC - komendy zdalne --------------
    def check_state(self):
        # print("Server state: " + str(server_state))
        return (self.server_state.name)

    def list_lobby(self):
        return self.lobby

    def list_ready(self):
        return self.ready

    def connect_to_lobby(self):
        """zwraca id oraz numer koloru"""
        if (self.server_state != ServerState["LOBBY_READY"]):
            print("connect_to_lobby: Serwer nie jest w Lobby")
            return [-1, -1]
        for index in range(len(self.lobby)):
            if (self.lobby[index] == False):
                self.lobby[index] = random()
                
                return [self.lobby[index], Color(index).name]  # zwraca ID i numer koloru/slotu

        print('Wszystkie sloty zajęte')
        return [-1, -1]  # wszystkie sloty zajęte

    def set_ready(self, playerid):
        if (self.server_state != ServerState["LOBBY_READY"]):
            print("set_ready: Serwer nie jest w Lobby")
            return False
        index = self.check_playerid(playerid)
        if (index != None):
            self.ready[index] = True
            # print("set_ready: Server state: " + str(server_state))
            return self.ready
        print("set_ready: Nie ma takiego gracza w Lobby")
        return False

    def start_game(self, playerid):

        if (self.server_state != ServerState["LOBBY_READY"]):
            print("start_game: Serwer nie jest w Lobby")
            return False
        if (self.check_playerid(playerid) == None):
            print("start.game: Nie ma takiego gracza w Lobby")
            return False
        # allready = False
        lplayercount = 0
        for index in range(len(self.lobby)):
            if (self.lobby[index] != False):
                lplayercount += 1
                if (self.ready[index] == False):
                    print("start.game: Nie ma wszyscy są gotowi")
                    return False
        if (lplayercount < 2):
            print("start.game: Za mało graczy")
            return False
        self.playercount = lplayercount
        print("start.game: Liczba graczy: " + str(self.playercount))
        self.g = Game(self.playercount)

        print(self.g.board.tiles)
        self.server_state = ServerState['GAME_START']
        print("Game started: " + str(self.lobby))
        return True

    # pobranie stanu gry
    def check_board(self, playerid):
        print(self.g.board.tiles)
        if (self.server_state != ServerState["GAME_START"]):
            print("check_board: Serwer nie jest w trakcie gry")
            return False
        str_board = []
        for index in range(len(self.g.board.tiles)):
            str_board.append(None)
            if (self.g.board.tiles[index] != None):
                str_board[index] = self.g.board.tiles[index].color.name
        return str(str_board)  # str(g.board.tiles)

    # sprawdzenie, czy tura gracza playerid:
    def check_current_color(self, playerid):
        if (self.server_state != ServerState["GAME_START"]):
            print("check_token: Serwer nie jest w trakcie gry")
            return False
        index = self.check_playerid(playerid)
        if (self.lobby_player_color(playerid) == self.g.current_color):
            return True
        return False

    def check_dice(self, playerid):
        if (self.server_state != ServerState["GAME_START"]):
            print("move: Serwer nie jest w trakcie gry")
            return None
        if (self.check_playerid(playerid) == None):
            return None
        if (self.check_current_color(playerid) != True):
            return None
        return self.g.dice.last_throw

    def move(self, playerid, user_input, choose_input):

        if (self.server_state != ServerState["GAME_START"]):
            print("move: Serwer nie jest w trakcie gry")
            return False
        if (self.check_playerid(playerid) == None):
            return False
        if (self.check_current_color(playerid) != True):
            return False

        def fuser_input(alert):
            #			if(alert!=None):
            #				print(alert)
            return user_input

        def fchoose_input():
            return choose_input

        self.g.turn(fuser_input, fchoose_input)
        return True


if __name__ == "__main__":
    gs = GameServer("localhost", 8003)
