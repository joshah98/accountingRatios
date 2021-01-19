def getRatios(inc, cf, bs, ratio):

    if ratio == 'liquidity':
        currA = bs[0]['totalCurrentAssets']
        currL = bs[0]['totalCurrentLiabilities']
        inv = bs[0]['inventory']

        currRatio = currA/currL
        quickRatio = (currA - inv)/currL

        print('The current ratio describes the ability to meet current obligations with current assets')
        print('The quick ratio describes the ability to meet current obligations with most liquid assets')
        print(currRatio)
        print(quickRatio)

    elif ratio == 'solvency':
        totalSHE = bs[0]['totalStockholderEquity']
        cash = bs[0]['cash']
        debt = bs[0]['shortLongTermDebt'] + bs[0]['longTermDebt']

        debtToEquity = (debt - cash)/totalSHE
        percTotalCap = (debt - cash)/(debt - cash + totalSHE)

        intExp = inc[0]['interestExpense']
        ebit = inc[0]['ebit']
        opAct = cf[0]['totalCashFromOperatingActivities']
        totalL = bs[0]['totalLiab']


        intCov = ebit/intExp
        cftl = opAct/totalL

        print('Debt to equity measures amount of debt they have relative to shareholders equity; the lower this ratio, '
              'the better')
        print('Net debt as a percentage of total capitalization measures total portion of financing represented by debt')
        print(debtToEquity)
        print(percTotalCap)

        print('Interest coverage measures a companies ability to cover interest expenses from earnings; the higher this'
               'ratio, the better')
        print('Cash flows to total liabilities measures a companies ability to cover total obligations with '
              'operating cash flow')
        print(intCov)
        print(cftl)

    elif ratio == 'profitability':
        rev = inc[0]['totalRevenue']
        gp = inc[0]['grossProfit']
        netInc = inc[0]['netIncome']
        she = bs[0]['totalStockholderEquity']

        gpm = gp/rev
        npm = netInc/rev
        roe = netInc/she

        print('The gross profit margin measures left over money from product sales after subtracting cost of goods sold')
        print('Net profit margin measures how much of each dollar earned is profit')
        print('Return on equity measures the rate of return on resources provided by investors')
        print(gpm)
        print(npm)
        print(roe)
    else:
        print('This analysis type is either invalid or unavailable')







