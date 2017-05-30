#-------------CLIENT--------
#
#-------------LOBBY---------
#1.podłączenie do servera, sprawdzenie komunikacji
#2.odpytanie o dostępne lobby
#3.wybranielobby i ready
#--------------GRA----------
#4.pobranie stanu planszy
#5.walidacja ruchu
#6.błąd ruchu
#7.wygrana/przegrana, powrót do lobby

from xmlrpc.client import ServerProxy
import xmlrpc.client
from classes.enums import *
from classes.counter import *


class Client:
    def __init__(self, address="localhost", port=8003):
        self.address=address
        self.port=port
        self.timeout=300

        self.playerid=None
        self.color=None

        self.server = ServerProxy("http://" + address + ":" + str(port), allow_none=True)  # ("http://localhost:8003")

        print(self.server.system.listMethods())

        # self.lobby()
        self.lobby_auto()

        self.game()


    #------------------------------------------DEBUG-----------------------
    def lobby_auto(self):
        """debug only: autoconnect+set_ready"""
        gamestarted = False

        while(gamestarted==False):
            if(self.server.check_state()!=ServerState["LOBBY_READY"].name):
                break
            print("Server state: " + str(self.server.check_state()))
            self.connect_to_lobby()
            if(self.server.set_ready(self.playerid)==False):
                print("set_ready == False")
                raise Exception("set_ready == False")
            print("Ready: " + str(self.server.list_ready()))
            input("Wait4secPlayer")
            if(self.server.check_state()!=ServerState["LOBBY_READY"].name):
                break
            if(self.server.start_game(self.playerid)==False):
                print("start_game == False")
                raise Exception("start_game == False")
            gamestarted=True

        return







    def connect_to_lobby(self):
        connection=self.server.connect_to_lobby()
        print(self.server.list_lobby())
        if (connection!=False):
            self.playerid = connection[0]
            self.color=connection[1]
            print("Connection: " + str(self.playerid) + " " + str(self.color))
            return True
        return False


    def lobby(self):
        gamestarted = False

        while(gamestarted==False):
            if(self.server.check_state()!=ServerState["LOBBY_READY"].name):
                    break
            choice=input("\n1.server_state 2.list_lobby 3.list_ready 4.connect_to_lobby 5.set_ready 6.start_game\n")
            if (choice=="1"):
                print("Server state: " + str(self.server.check_state()))
            if (choice=="2"):
                print("Lobby: " + str(self.server.list_lobby()))
            if (choice=="3"):
                print("Ready: " + str(self.server.list_ready()))
            if (choice=="4"):
                self.connect_to_lobby()
            if (choice=="5"):
                if(self.server.set_ready(self.playerid)==False):
                    print("set_ready == False")
                    raise Exception("set_ready == False")
                print("Ready: " + str(self.server.list_ready()))
            if (choice=="6"):
                if(self.server.start_game(self.playerid)==False):
                    print("start_game == False")
                    raise Exception("start_game == False")
                gamestarted=True

        return

    def game(self):
        gameended = False

        while(gameended==False):
            if(self.server.check_state()!=ServerState['GAME_START'].name):
                break
            choice=input("\n1.server_state 2.check_board 3.check_current_color 4.move\n")
            if (choice=="1"):
                print("Server state: " + str(self.server.check_state()))
            if (choice=="2"):
                print("Board: " + str(self.server.check_board(self.playerid)))
            if (choice=="3"):
                print("Current color: " + str(self.server.check_current_color(self.playerid)))
            if (choice=="4"):
                print("Move: ")
                print("B: " + str(self.server.check_board(self.playerid)))
                #przekopiowane z main
                dice=self.server.check_dice(self.playerid)
                print("Dice: " + str(dice))

                user_input = UserDecision(int(input())).name

                tile_index = int(input())
                is_home_tile = int(input())
                choose_input = tile_index, is_home_tile
                try:
                    self.server.move(self.playerid,user_input,choose_input)
                except xmlrpc.client.Fault as err:
                    print("A fault occurred")
                    print("Fault code: %d" % err.faultCode)
                    print("Fault string: %s" % err.faultString)

                print("B: " + str(self.server.check_board(self.playerid)))


        return

if __name__ == "__main__":
    c=Client()
    

        
