from classes.tcpserver  import TcpServer
from json import loads,dumps
from random import randint,random
from threading import Lock



class TcpClient:
    def __init__(self,serverhost="localhost",serverport=2223):
        self.serverhost = serverhost
        self.serverport = serverport
        self.playerid = random()
        print("playerid: " + str(self.playerid))

        self.odatalock = Lock()
        self.odata = None

        self.ihost = "localhost"
        self.iport = randint(49152,65535)
        self.commands = ["creply", "test2", "cprint_msg","cprint_lobby","cprint_status","cprint_board","cprint_current_color"]


        self.locallobby = []
        self.localboard = []

        self.ts = TcpServer(self.ihost, self.iport, self.decode)
        print("za ts")
        self.cconnect_to_lobby()
        self.cset_ready()
        self.ts.ireceiveTCP(self.decode)

        print("end __init__")
        #end of init--------------------------------------------------------------------

    def decode(self, idata):
        #print(idata)
        lidata = loads(idata)
        playerid, command, data = lidata
        # print(playerid)
        #print(command)
        #print(data)
        if (playerid == self.playerid):
           self.check_command(command, data)
        else:
            raise Exception("Wrong player remote command! " + str(command) + " " + str(playerid))

    def check_command(self, command, data):
        print("check_command")
        for index in range(len(self.commands)):
            if self.commands[index] == command:
                print("execute command")
                #execute command from list
                result = getattr(self,command)(data)
                return True
        raise Exception("No such remote command! " + str(command))
        return False



    def send_to_server(self,command,data):
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

#---------------remote server commands---------------
#---------------print-------------
    def cprint_msg(self, data):
        print(data)
        return True

    def cprint_lobby(self,data):
        self.locallobby=data
        print(data)

    def cprint_board(self,data):
        self.locallobby=data
        print(data)

    def cprint_status(self,data):
        print(data)

    def cprint_current_color(self,data):
        print(data)
#--------------lobby---------------
    def cconnect_to_lobby(self):
        self.send_to_server("sconnect_to_lobby",(self.ihost,self.iport))
        return True

    def cset_ready(self):
        self.send_to_server("sset_ready", True)
        return True
#-------------game-----------------
    def cstart_game(self):
        self.send_to_server("sstart_game", True)


if __name__ == "__main__":

    tc = TcpClient()