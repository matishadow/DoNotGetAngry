from classes.tcpserver import *
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread, Lock
from time import sleep
from json import dumps,loads
from random import *
from classes.enums import *
from classes.game import Game
from classes.dice import Dice
from classes.counter import *
from classes import *


class GameServer:
    def __init__(self):
        self.commands = ["stest", "stest2","sconnect_to_lobby","sset_ready"]#, "check_state", "list_lobby", "list_ready", "set_ready","start_game", "check_board", "check_dice", "check_current_color", "move"]
        self.odatalock=Lock()
        self.odata = None
        #
        self.lobby = []
        self.server_state = ServerState["LOBBY_READY"]
        self.g = None
        self.ts = TcpServer("localhost", 2223,self.decode)
        self.ts.ireceiveTCP(self.decode)
        print("end __init__")


    def decode(self, idata):
         #print(idata)
         lidata = loads(idata)
         playerid, command, data = lidata
         # print(playerid)
         #print(command)
         #print(data)
         self.check_command(command, playerid, data)


    def check_command(self, command, playerid, data):
        #print("check_command")
        if command == "sconnect_to_lobby":  # komenda przed playerid -> lobby
            print("execute command:" + command)
            # execute command from list
            result = getattr(self, command)(playerid, data)
            return True
        else:
            for index in range(len(self.commands)):
                if self.commands[index] == command:
                    print("execute command:" + command)
                    if(self.check_playerid(playerid)!=None):
                        #execute command from list
                        result = getattr(self,command)(playerid,data)
                        return True

        raise Exception("No such remote command! "+ str(command))
        return False

    def test(self,playerid,data):
        print(playerid)
    def test2(self,playerid,data):
        print("callback test2")

    def check_playerid(self,playerid):
        for index in range(len(self.lobby)):
            if (playerid == self.lobby[index][0]):
                return index
        return False

    def check_all_ready(self):
        for index in range(len(self.lobby)):
            if (self.lobby[index][2]==False):
                print("Not all ready")
                return False
        return True
    def send_to_client(self,playerid,command,data):
        index = self.check_playerid(playerid)
        if index != None:
            playerhost= self.lobby[index][1][0]
            playerport= self.lobby[index][1][1]
            self.odatalock.acquire(False)
            self.odata = dumps((playerid, command, data))
            self.odatalock.release()
            self.ts.osendTCP(playerhost, playerport, self.odatalock, self.odata)
        return True

    def send_to_all(self,command,data):
        for index in range(len(self.lobby)):
            playerid = self.lobby[index][0]
            self.send_to_client(playerid,command,data)
        return True

#-------------------server remote commands------------------
    def scheck_server_state(self,playerid):
        pass


    def sconnect_to_lobby(self,playerid,data):
        if(self.server_state!=ServerState["LOBBY_READY"]):
            return None
        print("connect_to_lobby: "+str(playerid) + str(data))
        if(len(self.lobby)<4):
            player = [playerid,data,False]
            self.lobby.extend([player])
            print("lobby: " + str(self.lobby))
            self.send_to_all("cprint_lobby",self.lobby)
            return True
        return None#bo None !=0

    def sset_ready(self,playerid,data):
        if (self.server_state != ServerState["LOBBY_READY"]):
            return False
        index = self.check_playerid(playerid)
        if index != None:
            self.lobby[index][2]=True
            self.send_to_all("cprint_lobby", self.lobby)
            if self.check_all_ready():
                self.sstart_game(None,None)
            return True
        return False

    def ssend_board_to_all(self):
        str_board = []
        for index in range(len(self.g.board.tiles)):
            str_board.append(None)
            if (self.g.board.tiles[index] != None):
                str_board[index] = self.g.board.tiles[index].color.name
        self.send_to_all("cprint_board", str_board)
        return True

    def ssend_color_to_all(self):
        self.send_to_all("cprint_current_color",self.g.current_color.name)
        return True

    def ssend_server_state(self):
        self.send_to_all("cprint_status", self.server_state.name)
        return True

    def sstart_game(self,playerid,data):
        if (self.check_all_ready()==False or self.server_state!=ServerState["LOBBY_READY"] or len(self.lobby)<2):
            return False
        else:
            self.server_state = ServerState["GAME_START"]
            self.ssend_server_state()
            self.g=Game(len(self.lobby))
            self.ssend_color_to_all()
            self.ssend_board_to_all()
            self.g.turn(self.suserdecision_callback,self.user_counter_choosen_callback)

            return True

    def suserdecision_callback(self):
        pass
    def user_counter_choosen_callback(self):
        self.send_to_client()
        pass
if __name__ == "__main__":

    gs = GameServer()