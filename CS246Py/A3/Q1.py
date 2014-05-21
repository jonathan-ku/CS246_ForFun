'''
Created on 2014-01-26

@author: Jonathan
'''

class Length(object):
    
    def __init__(self, ft , in_):
        self.ft = ft
        self.in_ = in_
        self.flag = False
            
    def __add__(self, length2):
        if type(length2) == Length:
            return self.__add__(length2.ft * 12 + length2.in_)
        elif type(length2) == int:
            result_in = self.ft * 12 + self.in_ + length2
            if result_in >= 0:
                self.ft = result_in / 12
                self.in_ = result_in % 12
            else:
                self.ft = (-result_in) / 12
                self.in_ = (-result_in)%12
                self.flag = True
                
        else:
            raise Exception("Invalid Object Type.")
        return self

    def __sub__(self, length2):
        if type(length2) == Length:
            return self.__sub__(length2.ft * 12 + length2.in_)
        elif type(length2) == int:
            return self.__add__(-length2)
        else:
            raise Exception("Invalid Object Type.")

    def __str__(self):
        if self.flag == False:
            return "%d'%d\""  %(self.ft, self.in_)
        else:
            return "-%d'%d\""  %(self.ft, self.in_)


if __name__ == '__main__':
    l = Length(1,2)
    l2 = Length(0,11)
    print Length(1,2) -Length(0,11)
    print Length(0,11) -1
    print Length(0,11) - 12
    print Length(1,2) - 27
    print Length(1,2) -2 
    print Length(1,2) -3