# coding=utf-8
from vector import Vector
class Atom:

    def __init__(self,id,hydrofobowy,położenie):
        self.id=id
        self.hydrofobowy=hydrofobowy
        if type(położenie)==Vector:
            self.położenie=położenie
        else:
            print "błąd położenia"

    def to_pdb(self):
        section = 'ATOM'.ljust(6)  # 1-6
        id = str(self.id).rjust(5)  # 7-11
        space1 = ''.rjust(1)  # 12
        name = ' C'.ljust(4)  # 13-16
        altLoc = ''.rjust(1)  # 17
        if self.hydrofobowy == 'H':
            resName = 'ALA'.rjust(3)  # 18-20
        else:
            resName = 'ARG'.rjust(3)  # 18-20
        space2 = ''.rjust(1)  # 21
        chain = 'A'.rjust(1)  # 22
        resSeq = str(self.id).rjust(4)  # 23-26
        iCode = ''.rjust(1)  # 27
        space3 = ''.rjust(3)  # 28-30
        x = str(self.x).rjust(8)  # 31-38 fixme przerobić na wektor
        y = str(self.y).rjust(8)  # 39-46 fixme
        z = '0'.rjust(8)  # 47-54
        occupancy = ''.rjust(6)  # 55-60
        tempFactor = ''.rjust(6)  # 61-66
        space4 = ''.rjust(10)  # 67-76
        element = 'C'.rjust(2)  # 77-78
        charge = '0'.rjust(2)  # 79-80
        return section + id + space1 + name + altLoc + resName + space2 + chain + resSeq + iCode + space3 + x + y + z \
               + occupancy + tempFactor + space4 + element + charge