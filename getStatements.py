import re
import json
from bs4 import BeautifulSoup
import requests
import getData
import getRatios


def getStatements(stock, ratio):
    # boilerplate url for financial statements
    finURL = 'https://ca.finance.yahoo.com/quote/{}/financials?p={}'

    # get the financial statement info and trim it down a bit
    res = requests.get(finURL.format(stock, stock))
    soup = BeautifulSoup(res.text, 'html.parser')
    pattern = re.compile(r'\s--\sData\s--\s')
    scriptData = soup.find('script', text=pattern).contents[0]

    start = scriptData.find('context') - 2
    jsonData = json.loads(scriptData[start:-12])
    jsonData['context'].keys()

    # get financial statement info
    incomeStatement = jsonData['context']['dispatcher']['stores']['QuoteSummaryStore']['incomeStatementHistory'][
        'incomeStatementHistory']
    # print(incomeStatement)
    incomeStatement = getData.getData(incomeStatement)
    # print(incomeStatement)

    cashFlows = jsonData['context']['dispatcher']['stores']['QuoteSummaryStore']['cashflowStatementHistory'][
        'cashflowStatements']
    # print(cashFlows)
    cashFlows = getData.getData(cashFlows)

    balanceSheet = jsonData['context']['dispatcher']['stores']['QuoteSummaryStore']['balanceSheetHistory'][
        'balanceSheetStatements']
    # print(balanceSheet)
    balanceSheet = getData.getData(balanceSheet)


    getRatios.getRatios(incomeStatement, cashFlows, balanceSheet,ratio)
