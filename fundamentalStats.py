# fundamental stats is used to store single stock information


class fundamentalStats(object):
    def __init__(self):
        _years = []
        # Revenue
        self._totalRevenue = []
        self._costRevenue = []
        self._grossProfit = [] # *

        # Operating expenses
        self._rd = [] # research development
        self._sellingGeneral = [] # Selling general and administrative
        self._nonRecurringExpense = [] # Non Recurring
        self._otherExpense = [] # Other
        self._operatingIncome = [] # * Operating Income or Loss

        # Income from Continuing Operations
        self._netIncomeFromContinueOps = [] # *

        # Net income
        self._netIncome = [] # *

    def getStatsFromFile(self, file):
            statsDict = {}
            fh = open(file,"r")
            lines = fh.readlines()
            for line in lines:
                k,v = line.split("=")
                k = k.strip()
                v = v.strip()
                statsDict[k] = v
            fh.close()
            # start to assign value
            self._years.append(statsDict["31"])
            self._years.append(statsDict["33"])
            self._years.append(statsDict["35"])

            self._grossProfit.append(statsDict["58"])
            self._grossProfit.append(statsDict["60"])
            self._grossProfit.append(statsDict["62"])

            self._operatingIncome.append(statsDict["106"])
            self._operatingIncome.append(statsDict["108"])
            self._operatingIncome.append(statsDict["110"])

            self._netIncomeFromContinueOps.append(statsDict["166"])
            self._netIncomeFromContinueOps.append(statsDict["168"])
            self._netIncomeFromContinueOps.append(statsDict["170"])

            self._netIncome.append(statsDict["205"])
            self._netIncome.append(statsDict["207"])
            self._netIncome.append(statsDict["209"])
