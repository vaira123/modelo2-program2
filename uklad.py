# coding=utf-8
from random import randint

from atom import Atom
from vector import Vector


class Układ:
    def __init__(self, sekw, temp, ):
        self.temp=temp
        self.sekw=sekw
        self.atomy=[]

    def wybór(self): #wybór losowego atomu do obracania wokół niego
        wybrany=randint(1,len(self.sekw)-2)

    def początek(self): #nadaje atomom początkowe położenie w linii, oraz unikalne id
        for i in range(len(self.sekw)):
            self.atomy.append(Atom(i,self.sekw(i),Vector([0,i])))

    #todo przeiterować po atomach żeby każdy się wypisywał do pdb
            #todo sprawdzić najpierw czy się ładnie wypisuje początek