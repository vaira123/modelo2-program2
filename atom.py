# coding=utf-8
from vector import Vector
class Atom:

    def __init__(self,hydrofobowy,położenie):
        self.hydrofobowy=hydrofobowy
        if type(położenie)==Vector:
            self.położenie=położenie
        else:
            print "błąd położenia"
