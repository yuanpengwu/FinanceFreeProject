import scrapy
import re


class QuotesSpider(scrapy.Spider):
    name = "balanceQuotes"

    def start_requests(self):
        def generateSourceLink():
            reList = []
            txt_file = open('stocklist.txt', "r")
            lines = txt_file.readlines()
            for line in lines:
                line = line.strip()
                tmpStr = "https://finance.yahoo.com/quote/%s/balance-sheet?p=%s"% (line, line)
                reList.append(str(tmpStr))
            return reList

        urls = generateSourceLink()
        '''
        urls = [
            "https://finance.yahoo.com/quote/GE/financials?p=GE",
            "https://finance.yahoo.com/quote/MITK/financials?p=MITK",
        ]
        '''
        #print("urls = ", urls)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        stockSymbol = response.url.split("=")[-1]
        dataKey = "data-reactid"
        items = response.css('span').extract()
        print(items)
        print("size of items = ", len(items))
        filename = '%s-balance-sheet.txt' % stockSymbol
        with open(filename, 'w+') as f:
            for item in items:
                result = self.extractInfo(item)
                if result != "":
                    f.write(result)
                    f.write('\n')
        self.log('Saved file %s' % filename)
    def extractInfo(self, line):
        if "data-reactid" not in line:
            return ""
        matchObj =  re.match(r'<span data-reactid=\"(\d+)\">(.*)</span>', line, re.M|re.I)
        ret=""
        if matchObj and matchObj.group(2) != "":
            ret = matchObj.group(1)+"="+matchObj.group(2)
        return ret