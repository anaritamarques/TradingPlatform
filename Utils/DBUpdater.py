import time
from threading import Thread
from random import randint, random

from datetime import date

import Controllers
from Controllers.Contract import Contract
from Controllers.Asset import Asset

class DBUpdater(Thread):

    def __init__(self, email, tkframe):
        self.tkframe = tkframe
        self.user = email
        Thread.__init__(self)

    def randPrice(self, lastPrice):
        return float(lastPrice) + (float(lastPrice) * (randint(-3, 3)/100))

    def randChange(self, changeN):
        return float(changeN) + (float(changeN) * (randint(-3, 3)/100))

    def randPercentage(self, changePercentage):
        return float(changePercentage) + (float(changePercentage) * (randint(-3, 3)/100))

    def randVolume(self, volume):
        return float(volume) + (float(volume) * (randint(-3, 3)/100))

    def changeAsset(self, idAsset):
        lastPrice = Asset.getLastPrice(self, idAsset)
        newLastPrice = DBUpdater.randPrice(self, lastPrice)
        change = Asset.getChange(self, idAsset)
        newChange = DBUpdater.randChange(self, change)
        changePercentage = Asset.getChangePercentage(self, idAsset)
        newChangePercentage = DBUpdater.randPercentage(self, changePercentage)
        volume = Asset.getVolume(self, idAsset)
        newVolume = DBUpdater.randVolume(self, volume)
        Asset.updateAsset(self, idAsset, newLastPrice, newChange, newChangePercentage, newVolume)
        Asset.notifyObservers(self, self.user, self.tkframe)
        return newLastPrice

    def changeContract(self, contract, newLastPrice):
        todayDate = date.fromtimestamp(time.time())
        sellPrice = Contract.getSellPrice(self, contract)
        endOfContract = Contract.getEndOfContract(self, contract)
        takeProfit = Contract.getTakeProfit(self, contract)
        stopLoss = Contract.getStopLoss(self, contract)
        sellerId = Contract.getSellerId(self, contract)
        buyerId = Contract.getBuyerId(self, contract)
        status = Contract.getStatus(self, contract)
        numberOfContracts = Contract.getNumberOfAssets(self, contract)
        Contract.updateContract(self, contract, newLastPrice, sellerId, buyerId, sellPrice,
                                todayDate, endOfContract, takeProfit, stopLoss, status, numberOfContracts)

    def run(self):
        while True:
            newLastPrice = 0
            for x in range(1, 9):
                newLastPrice = DBUpdater.changeAsset(self, x)

            contracts = Contract.getOpenAssetContracts(self, x)
            for contract in contracts:
                DBUpdater.changeContract(self, contract, newLastPrice)

            secondsToSleep = randint(1, 5)
            time.sleep(secondsToSleep)


