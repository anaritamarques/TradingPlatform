import Models
from Models.Trader import Trader
class Trader:

    def __init__(self, name, email, password, plafond):
        self.name = name
        self.email = email
        self.password = password
        self.plafond = plafond

    def isLoginValid(self):
        if(len(self.password)>0):
            return Models.Trader.Trader.isLoginValid(self, self.email, self.password)

    def isDataValid(self):
        if (len(self.name) > 0) and (len(self.email) > 0 and (len(self.password) > 0) and (int(self.plafond)) >= 0):
            return True

    def isRegisterValid(self):
        if(Trader.isDataValid(self)):
            return Models.Trader.Trader.isRegisterValid(self, self.name, self.email, self.password, self.plafond)

    def getContracts(self, email):
        return Models.Trader.Trader.getContracts(self, email)

    def getName(self, idTrader):
        return Models.Trader.Trader.getName(self, idTrader)

    def addPlafond(self, email, plafond):
        if(len(plafond)==0):
            return False
        else:
            return Models.Trader.Trader.addPlafond(self, email, plafond)
