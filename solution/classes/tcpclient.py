from classes.tcpserver import TcpServer
from json import loads, dumps
from random import randint, random
from threading import Lock
from time import sleep
from uuid import uuid4
from classes.enums import *


class TcpClient:
    def __init__(self, serverhost="localhost", serverport=2223, game_window=None):
        self.serverhost = serverhost
        self.serverport = serverport
        self.playerid = uuid4().hex
        self.my_color = None
        print("playerid: " + str(self.playerid))

        self.odatalock = Lock()
        self.odata = None

        self.ihost = "localhost"
        self.iport = randint(49152, 65535)
        self.commands = ["creply", "test2", "cprint_msg", "cprint_lobby", "cprint_status", "cprint_board",
                         "cprint_current_color", "cprint_dice", "cuserdecision_callback",
                         "cuser_counter_choosen_callback", "cuser_dice_confirm_callback", "cprint_my_color"]

        self.locallobby = []
        self.localboard = []
        self.game_window = game_window

        self.ts = TcpServer(self.ihost, self.iport, verbose=False)
        self.ts.ireceiveTCP(self.decode)

        self.cconnect_to_lobby()
        sleep(0.5)
        self.cset_ready()


        # print("end __init__")
        # end of init--------------------------------------------------------------------

    def decode(self, idata):
        # print(idata)
        lidata = loads(idata)
        playerid, command, data = lidata
        # print(playerid)
        # print(command)
        # print(data)
        if (playerid == self.playerid):
            self.check_command(command, data)
        else:
            raise Exception("Wrong player remote command! " + str(command) + " " + str(playerid))

    def check_command(self, command, data):
        # print("check_command")
        for index in range(len(self.commands)):
            if self.commands[index] == command:
                # print("execute command")
                # execute command from list
                result = getattr(self, command)(data)
                return True
        raise Exception("No such remote command! " + str(command))
        return False

    def send_to_server(self, command, data):
        self.odatalock.acquire(False)
        self.odata = dumps((self.playerid, command, data))
        self.odatalock.release()
        self.ts.osendTCP(self.serverhost, self.serverport, self.odatalock, self.odata)

    def creply(self, data):
        self.odatalock.acquire(False)
        self.odata = dumps((self.playerid, "test", "data"))
        self.odatalock.release()
        self.ts.osendTCP(self.serverhost, self.serverport, self.odatalock, self.odata)
        return True

    # ---------------remote server commands---------------
    # ---------------print-------------
    def cprint_msg(self, data):
        print(data)
        return True

    def cprint_my_color(self, data):
        self.my_color = data
        print("My color :" + str(data))
        self.game_window.set_player_color(str(data))
        return True

    def cprint_lobby(self, data):
        self.locallobby = data
        print(data)
        return True

    def cprint_dice(self, data):
        print(data)
        return True

    def cprint_board(self, data):
        str_board = []
        for index in range(len(data)):
            str_board.append(None)
            if (data[index] != None):
                str_board[index] = str(data[index]) + "[" + str(index) + "]"
        print(str(str_board))
        # print(data)
        return True

    def cprint_status(self, data):
        print(data)

    def cprint_current_color(self, data):
        print(data)

    # --------------lobby---------------
    def cconnect_to_lobby(self):
        self.send_to_server("sconnect_to_lobby", (self.ihost, self.iport))
        return True

    def cset_ready(self):
        self.send_to_server("sset_ready", True)
        return True

    # -------------game-----------------
    def cstart_game(self):
        self.send_to_server("sstart_game", True)

    def cuserdecision_callback(self, data):
        # print("dice: " + str(data))
        self.cprint_dice(data)
        decision = int(input("userdecision_callback :"))
        self.send_to_server("supdate_user_decision_callback", decision)
        return True

    def cuser_counter_choosen_callback(self, data):
        self.cprint_dice(data)
        decision = (int(input("user_counter_choosen_callback :")), int(input("is home? :")))
        self.send_to_server("supdate_user_counter_choosen_callback", decision)
        return True

    def cuser_dice_confirm_callback(self, data):
        self.cprint_dice(data)
        input("Dice OK?")
        self.send_to_server("supdate_dice_confirm_callback", True)
        return True


if __name__ == "__main__":
    tc = TcpClient()
