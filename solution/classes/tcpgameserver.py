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
PAUSE = 0.01

class GameServer:
    def __init__(self):
        self.commands = ["sconnect_to_lobby","sset_ready","supdate_user_decision_callback","supdate_user_counter_choosen_callback","supdate_dice_confirm_callback"]#, "check_state", "list_lobby", "list_ready", "set_ready","start_game", "check_board", "check_dice", "check_current_color", "move"]
        self.odatalock=Lock()
        self.odata = None
        #
        self.lobby = []
        self.server_state = ServerState["LOBBY_READY"]
        self.g = None
        self.ts = TcpServer("localhost", 2223,verbose=False)
        self.user_decision_callback_buffer = None #przekazuję odpowiedź callbacka klienta do turn
        self.user_counter_choosen_callback_buffer = None
        self.user_dice_confirm = False

        self.ts.ireceiveTCP(self.decode)

        self.mainloop()
        #pętla logiki gry:
        #1.oczekiwanie na graczy:

        #print("end __init__")

    def mainloop(self):
        print("LOBBY_READY")
        while True:
            if self.check_all_ready():
                print("mainloop: start_game")
                self.start_game()
                self.ssend_color_to_all()
                break
            sleep(PAUSE)
        #petla gry:
        while True:
            self.ssend_current_color_to_all()
            self.ssend_board_to_all()
            try:
                end_of_game = self.g.turn(self.suserdecision_callback, self.suser_counter_choosen_callback, self.suser_dice_confirm_callback)
            except:
                print("turn error")
            finally:
                pass
                #if end_of_game:
                #   break
            sleep(PAUSE)



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
        if command == "sconnect_to_lobby":  # komenda przed przypisaniem playerid -> lobby
            #print("execute command:" + command)
            # execute command from list
            result = getattr(self, command)(playerid, data)
            return True
        else:
            for index in range(len(self.commands)):
                if self.commands[index] == command:
                    #print("execute command:" + command)
                    if(self.check_playerid(playerid)!=None):
                        #execute command from list
                        result = getattr(self,command)(playerid,data)
                        return True

        raise Exception("No such remote command! "+ str(command))
        return False


    def check_playerid(self,playerid):
        for index in range(len(self.lobby)):
            if (playerid == self.lobby[index][0]):
                return index
        return False

    def check_all_ready(self):
        if(len(self.lobby)<2):
            #print("Not enough players")
            return False
        for index in range(len(self.lobby)):
            if (self.lobby[index][2]==False):
                #print("Not all ready")
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
            #print(playerhost,playerport)
            self.ts.osendTCP(playerhost, playerport, self.odatalock, self.odata)
        return True

    def send_to_all(self,command,data):
        for index in range(len(self.lobby)):
            playerid = self.lobby[index][0]
            self.send_to_client(playerid,command,data)
            sleep(PAUSE)
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

    def ssend_color_to_all(self):
        for index in range(len(self.lobby)):
            playerid = self.lobby[index][0]
            self.send_to_client(playerid,"cprint_my_color",Color(index).name)
            sleep(PAUSE)
        return True

    def return_playerid_from_color(self,color):
        for index in range(len(self.lobby)):
            playerid = self.lobby[index][0]
            self.send_to_client(playerid,"cprint_my_color",Color(index).name)

    def sset_ready(self,playerid,data):
        print("set_ready: " + str(playerid))
        print(self.lobby)
        #if len(self.lobby)<1:
        #    return False
        if (self.server_state != ServerState["LOBBY_READY"]):
            return False
        index = self.check_playerid(playerid)

        if index != None:
            self.lobby[index][2]=True
            self.send_to_all("cprint_lobby", self.lobby)
            #przeniesione do self.mainloop()
            #if self.check_all_ready():
            #    self.sstart_game(None,None)
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

    def ssend_current_color_to_all(self):
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
            self.ssend_current_color_to_all()
            self.ssend_board_to_all()
            #self.g.turn(self.suserdecision_callback,self.user_counter_choosen_callback)

            return True

    def start_game(self):
        if (self.check_all_ready()==False or self.server_state!=ServerState["LOBBY_READY"] or len(self.lobby)<2):
            return False
        else:
            self.server_state = ServerState["GAME_START"]
            self.ssend_server_state()
            self.g=Game(len(self.lobby))
            #self.ssend_current_current_color_to_all()
            #self.ssend_board_to_all()
            #self.g.turn(self.suserdecision_callback,self.user_counter_choosen_callback)

            return True

    def suserdecision_callback(self,alert):
        #print("suserdecision_callback " + str(alert))
        playerid =self.lobby[self.g.current_color.value][0]
        dice = self.g.dice.last_throw
        self.send_to_client(playerid,"cuserdecision_callback",dice)
        #print(self.user_decision_callback_buffer)
        #input("uwaga!!!")
        while (self.user_decision_callback_buffer==None):#oczekiwanie na odpowiedź przez zmienną
            sleep(0.5)
        ret = UserDecision(self.user_decision_callback_buffer).name
        self.user_decision_callback_buffer = None
        return ret

    def suser_counter_choosen_callback(self):
        #print("user_counter_choosen_callback")
        #return input(), input()
        playerid = self.lobby[self.g.current_color.value][0]
        dice = self.g.dice.last_throw
        self.send_to_client(playerid,"cuser_counter_choosen_callback", dice)
        while (self.user_counter_choosen_callback_buffer == None):  # oczekiwanie na odpowiedź przez zmienną
            sleep(0.5)
        ret = self.user_counter_choosen_callback_buffer
        self.user_counter_choosen_callback_buffer = None
        return ret

    def suser_dice_confirm_callback(self):
        playerid = self.lobby[self.g.current_color.value][0]
        dice = self.g.dice.last_throw
        self.send_to_client(playerid, "cuser_dice_confirm_callback", dice)
        while (self.user_dice_confirm == None):  # oczekiwanie na odpowiedź przez zmienną
            sleep(0.5)
        ret = self.user_dice_confirm
        self.user_dice_confirm = None
        return ret

    def supdate_user_decision_callback(self,playerid,data):
        self.user_decision_callback_buffer = data
        return True


    def supdate_user_counter_choosen_callback(self,playerid,data):
        self.user_counter_choosen_callback_buffer = data
        return True

    def supdate_dice_confirm_callback(self,playerid,data):
        self.user_dice_confirm = data
        return True

if __name__ == "__main__":

    gs = GameServer()