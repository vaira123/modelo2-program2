# coding=utf-8
from random import randint
from atom import Atom
from vector import Vector


class Uklad:

    def __init__(self, sekw, temp=1 ):
        self.temp=temp
        self.sekw=sekw
        self.atomy=[]

    def wybor(self): #wybor losowego atomu do obracania wokol niego
        wybrany=randint(1,len(self.sekw)-2)

    def poczatek(self): #nadaje atomom poczatkowe polozenie w linii, oraz unikalne id
        for i in range(len(self.sekw)):
            self.atomy.append(Atom(i,self.sekw[i],Vector([0,i]))) #fixme <vector.Vector instance at 0x7fe44c2755a8> ??

            print i
            print Vector([0,i])

    def wypisywanie(self,przyklad): #iteruje po atomach, zeby wypisaly sie do pliku
        result = 'MODEL     ' + str(przyklad) + '\n'
        for a in self.atomy:
            result += a.pdb() + '\n'
        result += 'ENDMDL\n'
        return result

    def plikk(self, przyklad):
        prz=str(przyklad)
        plik= open(prz, 'w')
        plik.write(self.wypisywanie(przyklad))
        plik.close()

####################################################3
S='PHPPHPPHHPPHHPPHPPHP'
Ss=Uklad(S,1)
Sss=Ss.poczatek()
Sss.plikk('alla')
#todo sprawdzić najpierw czy sie ladnie wypisuje poczatek