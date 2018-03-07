# record balance stats

class balanceStats(object):
    def __init__(self):
        self._currentAsset = []
        self._totalAsset = []
        self._currentLiabilities = []
        self._totalLiabilities = []

        self._totalStockholderEquity = []
        self._netAssets = []

    def getStatsFromFile(self, file):
        statsDict = {}
        fh = open(file, "r")
        lines = fh.readlines()
        for line in lines:
            k, v = line.split("=")
            k = k.strip()
            v = v.strip()
            statsDict[k] = v
        fh.close()

        self._currentAsset.append(statsDict["85"])
        self._currentAsset.append(statsDict["87"])
        self._currentAsset.append(statsDict["89"])

        self._totalAsset.append(statsDict["145"])
        self._totalAsset.append(statsDict["147"])
        self._totalAsset.append(statsDict["149"])

        self._currentLiabilities.append(statsDict["181"])
        self._currentLiabilities.append(statsDict["183"])
        self._currentLiabilities.append(statsDict["185"])

        self._totalLiabilities.append(statsDict["226"])
        self._totalLiabilities.append(statsDict["228"])
        self._totalLiabilities.append(statsDict["230"])

        self._totalStockholderEquity.append(statsDict["301"])
        self._totalStockholderEquity.append(statsDict["303"])
        self._totalStockholderEquity.append(statsDict["305"])

        self._netAssets.append(statsDict["310"])
        self._netAssets.append(statsDict["312"])
        self._netAssets.append(statsDict["314"])

