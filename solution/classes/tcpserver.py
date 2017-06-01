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
TCPsleep = 0.5

class TcpServer:


    def __init__(self, ihost, iport,idatadecode):

        print("Start Tcpserver@"+str(ihost)+ ":" + str(iport))
        self.buf = 1024
        self.iaddr = (ihost, iport)
        #oaddr = (ohost,oport)
        self.idatalock = Lock() #lock na self.idata oraz self.idatanew
        self.idata = None
        self.idatanew = False
        self.iTCPthread = None
        self.oTCPthread = None


    def ireceiveTCP(self,idatadecode):
        self.iTCPthread = Thread(target=self.istartTCP, args=([self.iaddr]))  # wątek oczekujący na przychodzące połączenia
        self.iTCPthread.start()
        self.ihandledata(idatadecode)


    def osendTCP(self,ohost,oport,odatalock,odata):
        self.oTCPthread = Thread(target=self.ostartTCP, args=([ohost,oport,odatalock,odata]))  # wątek oczekujący na przychodzące połączenia
        self.oTCPthread.start()


    def killallthreads(self):
        try:
            self.iTCPthread.join()
            self.oTCPthread.join()
        finally:
            pass


    def ostartTCP(self,ohost,oport,odatalock,odata):
        oaddr = (ohost,oport)
        TCPSock = socket(AF_INET, SOCK_STREAM)
        TCPSock.connect(oaddr)
        while True:
            succes = odatalock.acquire(False)
            if succes:
                if odata != None:
                    bin_data = odata.encode()
                    if (TCPSock.send(bin_data)):
                        odata=None
                        odatalock.release()
                        break
            sleep(TCPsleep)


    def istartTCP(self,addr):

        iSock = None  # incoming socket
        try:
            iSock = socket(AF_INET, SOCK_STREAM)
            iSock.bind(addr)
            iSock.listen(10)
        except:
            print("socket exception")
        stopped = False
        #(conn, (ip, port)) = iSock.accept()
        #print(conn)
        while not stopped:
            ex=False
            try:
                iSock.settimeout(0.2)
                (conn, (ip, port)) = iSock.accept()
            except:
                ex = True
                #print("accept timeout")
            finally:
                if ex == False:
                    print(conn)
                    try:
                        #conn.settimeout(0.2)
                        bin_idata = conn.recv(self.buf)
                    except:
                        ex=True
                        #print("data timeout")
                        pass
                    finally:
                        if ex==False:
                            idata = bin_idata.decode()
                            #print(idata)
                            #handledata(idata)
                            while True:
                                succes = self.idatalock.acquire(False)
                                if succes:
                                    #print("startTCP: idataLock")
                                    self.idatanew = True
                                    self.idata = idata
                                    self.idatalock.release()
                                    break
                                else:
                                    print("startTCP: idatalock fail")
            sleep(TCPsleep)

                            #print("data")

    def ihandledata(self,idatadecode):  # obsługa przychodzących danych:
        # print(" handledata")
        idata = None
        idatanew = False
        while True:
            # print("handledata: while")
            if self.idatanew:
                # print("handledata: idatanew!!!")
                succes = self.idatalock.acquire(False)
                if (succes & self.idatanew):
                    self.idatanew = False
                    idata = self.idata
                    self.idata = None
                    self.idatalock.release()
                    idatanew = True
                else:
                    print("handledata: idatalock fail")
                    sleep(TCPsleep)
            if (idatanew):
                idatadecode(idata)
                idatanew = False
            sleep(TCPsleep)




#if __name__ == "__main__":
#    ts = tcpserver("localhost", 2223)