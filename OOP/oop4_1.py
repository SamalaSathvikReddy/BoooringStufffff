class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class Archer(Human):
    def __init__(self, name, num_arrows):
        self.__num_arrows = num_arrows 
        super().__init__(name)

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        if(self.__num_arrows == 0):
            raise Exception("not enough arrows")
        else:
            self.__num_arrows = self.__num_arrows - 1

class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)

    def triple_shoot(self, target):
        if(self.__num_arrows >= 3):
            self.__num_arrows = self.__num_arrows - 3
            print("TARGET was shot by 3 crossbow bolts")
        else:
            raise Exception("not enought arrows for a triple shot") 

