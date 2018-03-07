# key elements for 5 rules of investment
import fundamentalStats
import balanceStats

class fundamentalProto(object):
    def __init__(self):
        self._earnings = []
        self._netProfit = []
        self._revenue = []
        self._margin = []
        self._netIncome = []
        self._shareholderEquity = []
        self._roe = []
        self._price = []
        self._pe = []
        self.growthRate = []
        self._netassets = []
        self._pb = []
    def calcFundProto(self, fundStats, balanceStats):
        # do calculation
        self._earnings = []
        self._netProfit = fundStats._netIncomeFromContinueOps
        self._revenue = fundStats._totalRevenue
        for index in range(len(self._netProfit)):
            self._margin.append(float(self._netProfit[index])/float(self._revenue[index]))

        self._netIncome = fundStats._netIncomeFromContinueOps
        self._shareholderEquity = balanceStats._totalStockholderEquity
