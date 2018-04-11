from threading import Thread
from .lib.KinseiClient import KinseiSocket as KinseiClient
from .lib.KinseiTuner import *
import datetime

LISTA_IP = []
class Connessione(Thread):
    """
    la classe si occupa di inizializzare la connessione ed eseguire le richieste
    """
    def __init__(self, ip):
        """
        inizializzo il Tread
        @ip: ip del device
        """
        Thread.__init__(self)
        self.FWB4july2017 = True
        self.ip = ip
        self.kC = ''
        self.nPersone = ''
        self.coordPersone= ''

    def run(self):
        """
        ottengo la posizione delle persone ed il numero
        :return:
        """
        #setto a null le variabili
        self.nPersone = ''
        self.coordPersone = ''

        self.coordPersone = self.kC.getPersonsPositions(False) # returns [number of persons, [map ID, x,y]] , lista di liste
        self.nPersone = len(self.coordPersone)
        #SCRITTURA SUL DB
        print(self.nPersone + " " + self.coordPersone + " TEMPO " + datetime.datetime.now())

    def connectKinseiClient(self):
        """
        connessione con il device
        @return: True / False
        """
        ris = False
        self.kC = KinseiClient.KinseiSocket(self.ip)

        if self.FWB4july2017 and self.kC.checkIfOnline():
            ris = True
        return ris

def acquisizione(ListaDevice):
    """
    eseguo l'acquisizione dei dati
    @param ListaDevice: Lista di Oggetti Device con connessione attivata
    :return:
    """
    for d in ListaDevice:
        d.run()

def findIp():
    """
    trova ip address dei device
    @return: listaIp
    """
    listaIp=["", "",]
    return listaIp



