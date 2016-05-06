# coding=utf-8
from functions.all import isnumeric
class Vector:

    def __init__(self,values):
        if values==None:
            self.dimension=0
            self.vector=[]
        elif(type(values)==list):
            self.dimension=len(values)
            self.vector=values
        else:
            self.dimension=1
            self.vector=[values]

    def __add__(self, other):
        result= []
        if isinstance(other, Vector):
            if self.dimension==other.dimension:
                if self.dimension==0:
                    return self
                for i in range(len(self.vector)):
                    result.append(self.vector[i] + other.vector[i])
            else:
                print "różne wymiary wektorów"
        elif isnumeric(other):
            for i in self.vector:
                result.append(i + other)
        else:
            print "nieznany typ othera?"
        return Vector(result)

    def __radd__(self, other):
        return self + other
