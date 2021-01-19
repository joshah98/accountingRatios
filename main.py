import getStatements

if __name__=="__main__":
    loop = True

    while loop:
        stock = input('Enter the company stock name: ')
        ratio = input('Would you like to look at liquidity ratios, solvency ratios, or profitability ratios? ')

        getStatements.getStatements(stock, ratio)

        cont = input('Would you like to look at another stock? (Y/N) ')
        loop = True if cont == 'Y' else False
