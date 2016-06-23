import os


# import Liquidity
def liquidity_ratios():
    print ("\nFour Types of Liquidity Ratio")
    liquidity_list = ["1. Quick Ratio", "2. Current Ratio", "3. Working Capital", "4. Times Interest Earned"]
    for i in liquidity_list:
        print (i)

    while True:
        try:
            select = int(raw_input("\nSelect what type of liquidity ratio you are looking for? "))
        except ValueError:
            print "\nPlease select a number between 1 and 4"
            continue

        if select == 1:
            print "\nYou have selected Quick Ratio. \n(Cash + Cash Equivalents + " \
                  "Short Term Investments + Current Receivables) / Current Liabilities"

            while True:
                try:
                    print ""
                    calculation = bytes(raw_input("Would you like to perform this calculation? ")).lower()
                except ValueError:
                    print "Please enter Yes or No"
                    continue

                try:
                    if calculation.lower() == "yes":
                        print ""
                        cv = float(raw_input("Enter Cash value: "))
                        ce = float(raw_input("Enter Cash Equivalents value: "))
                        sti = float(raw_input("Enter Short Term Investments value: "))
                        cr = float(raw_input("Enter Current Receivables value: "))
                        cl = float(raw_input("Enter Current Liabilities value: "))

                        qr = (cv + ce + sti + cr) / cl
                        print "Quick Ratio = ", round(qr, 2)
                        break
                    elif calculation.lower() == "no":
                        another_loop()
                    else:
                        print "Please enter Yes or No"
                except ValueError:
                    print "Please enter just a number"
                except ZeroDivisionError:
                    print "Please don't divide by zero"
                    continue

            another_loop()

        elif select == 2:
            print "\nYou have selected Current Ratio. \nCurrent Assets / Current Liabilities"
            while True:
                try:
                    print ""
                    calculation = bytes(raw_input("Would you like to perform this calculation? ")).lower()
                except ValueError:
                    print "Please enter Yes or No"
                    continue

                try:
                    if calculation.lower() == "yes":
                        print ""
                        ca = float(raw_input("Enter Current Assets value: "))
                        cl = float(raw_input("Enter Current Liabilities value: "))
                        cr = ca / cl
                        print "Current Ratio = ", round(cr, 2)
                        break

                    elif calculation.lower() == "no":
                        another_loop()
                    else:
                        print "Please enter Yes or No"
                except ValueError:
                    print "Please enter just a number"
                except ValueError:
                    print "Please enter just a number"
                    continue

            another_loop()

        elif select == 3:
            print "\nYou have selected Working Capital. \nCurrent Assets / Current Liabilities"
            while True:
                try:
                    print ""
                    calculation = bytes(raw_input("Would you like to perform this calculation? ")).lower()
                except ValueError:
                    print "Please enter Yes or No"
                    continue

                try:
                    if calculation.lower() == "yes":
                        print ""
                        ca = float(raw_input("Enter Current Assets value: "))
                        cl = float(raw_input("Enter Current Liabilities value: "))
                        cr = ca / cl
                        print "Working Capital = ", round(cr, 2)
                        break

                    elif calculation.lower() == "no":
                        another_loop()
                    else:
                        print "Please enter Yes or No"
                except ValueError:
                    print "Please enter just a number"
                except ValueError:
                    print "Please enter just a number"
                    continue
            another_loop()

        elif select == 4:
            print "\nYou have selected Times Interest Earned. \nIncome before Interest and " \
                  "Taxes or EBIT / Interest Expense"
            while True:
                try:
                    print ""
                    calculation = bytes(raw_input("Would you like to perform this calculation? ")).lower()
                except ValueError:
                    print "Please enter Yes or No"
                    continue

                try:
                    if calculation.lower() == "yes":
                        print ""
                        ibi = float(raw_input("Enter Income before Interest value: "))
                        t = float(raw_input("Enter Taxes or EBIT value: "))
                        ie = float(raw_input("Enter Interest Expense value: "))
                        tie = (ibi + t) / ie
                        print "Times Interest Earned = ", round(tie, 2)
                        break

                    elif calculation.lower() == "no":
                        another_loop()
                    else:
                        print "Please enter Yes or No"
                except ValueError:
                    print "Please enter just a number"
                except ValueError:
                    print "Please enter just a number"
                    continue
            another_loop()
        else:
            print "\nPlease select a number between 1 and 4"


# import Solvency
def solvency_ratios():

    print ("\nThree Types of Solvency Ratios")

    solvency_list = ["1. Debt to Equity Ratio", "2. Equity Ratio", "3. Debt Ratio"]
    for i in solvency_list:
        print (i)

    while True:
        try:
            select = int(raw_input("\nSelect what type of Solvency Ratios you are looking for? "))
        except ValueError:
            print "\nPlease select a number between 1 and 3"
            continue

        if select == 1:
            print "\nYou have selected Debt to Equity Ratio. \nTotal Liabilities / Total Equity"
            while True:
                try:
                    print ""
                    calculation = bytes(raw_input("Would you like to perform this calculation? ")).lower()
                except ValueError:
                    print "Please enter Yes or No"
                    continue

                try:
                    if calculation.lower() == "yes":
                        print ""
                        tl = float(raw_input("Enter Total Liabilities value: "))
                        te = float(raw_input("Enter Total Equity value: "))
                        tlte = tl / te
                        print "Debt to Equity Ratio = ", round(tlte, 2)
                        break

                    elif calculation.lower() == "no":
                        another_loop()
                    else:
                        print "Please enter Yes or No"
                except ValueError:
                    print "Please enter just a number"
                except ValueError:
                    print "Please enter just a number"
                    continue
            another_loop()

        elif select == 2:
            print "\nYou have selected Equity Ratio. \nTotal Equity / Total Assets"
            while True:
                try:
                    print ""
                    calculation = bytes(raw_input("Would you like to perform this calculation? ")).lower()
                except ValueError:
                    print "Please enter Yes or No"
                    continue

                try:
                    if calculation.lower() == "yes":
                        print ""
                        te = float(raw_input("Enter Total Equity value: "))
                        ta = float(raw_input("Enter Total Assets value: "))
                        teta = te / ta
                        print "Equity Ratio = ", round(teta, 2)
                        break

                    elif calculation.lower() == "no":
                        another_loop()
                    else:
                        print "Please enter Yes or No"
                except ValueError:
                    print "Please enter just a number"
                except ValueError:
                    print "Please enter just a number"
                    continue
            another_loop()

        elif select == 3:
            print "\nYou have selected Debt Ratio. \nTotal Liabilities / Total Assets"
            while True:
                try:
                    print ""
                    calculation = bytes(raw_input("Would you like to perform this calculation? ")).lower()
                except ValueError:
                    print "Please enter Yes or No"
                    continue

                try:
                    if calculation.lower() == "yes":
                        print ""
                        tl = float(raw_input("Enter Total Liabilities value: "))
                        ta = float(raw_input("Enter Total Assets value: "))
                        tlta = tl / ta
                        print "Debt Ratio = ", round(tlta, 2)
                        break

                    elif calculation.lower() == "no":
                        another_loop()
                    else:
                        print "Please enter Yes or No"
                except ValueError:
                    print "Please enter just a number"
                except ValueError:
                    print "Please enter just a number"
                    continue
            another_loop()
        else:
            print "\nPlease select a number between 1 and 3"


# import Efficiency
def efficiency_ratios():
    print ("\nFour Types of Efficiency Ratios")
    efficiency_list = ["1. Accounts Receivable Turnover", "2. Asset Turnover Ratio", "3. Inventory Turnover Ratio",
                       "4. Days Sales in Inventory"]
    for i in efficiency_list:
        print (i)

    while True:
        try:
            select = int(raw_input("\nSelect what type of Efficiency Ratio you are looking for? "))
        except ValueError:
            print "\nPlease select a number between 1 and 4"
            continue
        if select == 1:
            print "\nYou have selected Accounts Receivable Turnover. \nNet Cash Sales " \
                  "/ Average Accounts Receivable"
            while True:
                try:
                    print ""
                    calculation = bytes(raw_input("Would you like to perform this calculation? ")).lower()
                except ValueError:
                    print "Please enter Yes or No"
                    continue

                try:
                    if calculation.lower() == "yes":
                        print ""
                        ncs = float(raw_input("Enter Net Cash Sales value: "))
                        aar = float(raw_input("Enter Average Accounts Receivable value: "))
                        ncsaar = ncs / aar
                        print "Accounts Receivable Turnover = ", round(ncsaar, 2)
                        break

                    elif calculation.lower() == "no":
                        another_loop()
                    else:
                        print "Please enter Yes or No"
                except ValueError:
                    print "Please enter just a number"
                except ValueError:
                    print "Please enter just a number"
                    continue
            another_loop()
        elif select == 2:
            print "\nYou have selected Asset Turnover Ratio. \nNet Sales / Average Total Assets"
            while True:
                try:
                    print ""
                    calculation = bytes(raw_input("Would you like to perform this calculation? ")).lower()
                except ValueError:
                    print "Please enter Yes or No"
                    continue

                try:
                    if calculation.lower() == "yes":
                        print ""
                        ns = float(raw_input("Enter Net Sales value: "))
                        ats = float(raw_input("Enter Average Total Assets value: "))
                        nsats = ns / ats
                        print "Asset Turnover Ratio = ", round(nsats, 2)
                        break

                    elif calculation.lower() == "no":
                        another_loop()
                    else:
                        print "Please enter Yes or No"
                except ValueError:
                    print "Please enter just a number"
                except ValueError:
                    print "Please enter just a number"
                    continue
            another_loop()
        elif select == 3:
            print "\nYou have selected Inventory Turnover Ratio. \nCosts of Goods Sold / Average Inventory"
            while True:
                try:
                    print ""
                    calculation = bytes(raw_input("Would you like to perform this calculation? ")).lower()
                except ValueError:
                    print "Please enter Yes or No"
                    continue

                try:
                    if calculation.lower() == "yes":
                        print ""
                        cgs = float(raw_input("Enter Costs of Goods Sold value: "))
                        ai = float(raw_input("Enter Average Inventory value: "))
                        cgsai = cgs / ai
                        print "Inventory Turnover Ratio = ", round(cgsai, 2)
                        break

                    elif calculation.lower() == "no":
                        another_loop()
                    else:
                        print "Please enter Yes or No"
                except ValueError:
                    print "Please enter just a number"
                except ValueError:
                    print "Please enter just a number"
                    continue
            another_loop()
        elif select == 4:
            print "\nYou have selected Days Sales in Inventory. \n(Ending Inventory / Cost of Goods Sold) * 365"
            while True:
                try:
                    print ""
                    calculation = bytes(raw_input("Would you like to perform this calculation? ")).lower()
                except ValueError:
                    print "Please enter Yes or No"
                    continue

                try:
                    if calculation.lower() == "yes":
                        print ""
                        ei = float(raw_input("Enter Ending Inventory value: "))
                        cgs = float(raw_input("Enter Cost of Goods Sold value: "))
                        eicgs = (ei / cgs) * 365
                        print "Days Sales in Inventory = ", round(eicgs, 2)
                        break

                    elif calculation.lower() == "no":
                        another_loop()
                    else:
                        print "Please enter Yes or No"
                except ValueError:
                    print "Please enter just a number"
                except ValueError:
                    print "Please enter just a number"
                    continue
            another_loop()
        else:
            print "\nPlease select a number between 1 and 4"


# import Profitability
def profitability_ratios():
    print ("\nFour Types of Profitability Ratios")
    liquidity_list = ["1. Gross Margin Ratio", "2. Profit Margin Ratio", "3. Return on Assets",
                      "4. Return on Capital Employed", "5. Return on Equity"]
    for i in liquidity_list:
        print (i)

    while True:
        try:
            select = int(raw_input("\nSelect what type of Profitability Ratios you are looking for? "))
        except ValueError:
            print "\nPlease select a number between 1 and 5"
            continue
        if select == 1:
            print "\nYou have selected Gross Margin Ratio. \nGross Margin / Net Sales"
            while True:
                try:
                    print ""
                    calculation = bytes(raw_input("Would you like to perform this calculation? ")).lower()
                except ValueError:
                    print "Please enter Yes or No"
                    continue

                try:
                    if calculation.lower() == "yes":
                        print ""
                        gm = float(raw_input("Enter Gross Margin value: "))
                        ns = float(raw_input("Enter Net Sales value: "))
                        gmns = gm / ns
                        print "Gross Margin Ratio = ", round(gmns, 2)
                        break

                    elif calculation.lower() == "no":
                        another_loop()
                    else:
                        print "Please enter Yes or No"
                except ValueError:
                    print "Please enter just a number"
                except ValueError:
                    print "Please enter just a number"
                    continue
            another_loop()

        elif select == 2:
            print "\nYou have selected Profit Margin Ratio. \nNet Income / Net Sales"
            while True:
                try:
                    print ""
                    calculation = bytes(raw_input("Would you like to perform this calculation? ")).lower()
                except ValueError:
                    print "Please enter Yes or No"
                    continue

                try:
                    if calculation.lower() == "yes":
                        print ""
                        ni = float(raw_input("Enter Net Income value: "))
                        ns = float(raw_input("Enter Net Sales value: "))
                        nins = ni / ns
                        print "Profit Margin Ratio = ", round(nins, 2)
                        break

                    elif calculation.lower() == "no":
                        another_loop()
                    else:
                        print "Please enter Yes or No"
                except ValueError:
                    print "Please enter just a number"
                except ValueError:
                    print "Please enter just a number"
                    continue
            another_loop()
        elif select == 3:
            print "\nYou have selected Return on Assets. \nNet Income / Average Total Assets"
            while True:
                try:
                    print ""
                    calculation = bytes(raw_input("Would you like to perform this calculation? ")).lower()
                except ValueError:
                    print "Please enter Yes or No"
                    continue

                try:
                    if calculation.lower() == "yes":
                        print ""
                        ni = float(raw_input("Enter Net Income value: "))
                        ata = float(raw_input("Enter Average Total Assets value: "))
                        niata = ni / ata
                        print "Return on Assets = ", round(niata, 2)
                        break

                    elif calculation.lower() == "no":
                        another_loop()
                    else:
                        print "Please enter Yes or No"
                except ValueError:
                    print "Please enter just a number"
                except ValueError:
                    print "Please enter just a number"
                    continue
            another_loop()
        elif select == 4:
            print "\nYou have selected Return on Capital Employed. \nNet Operating Profit / Employed Capital"
            while True:
                try:
                    print ""
                    calculation = bytes(raw_input("Would you like to perform this calculation? ")).lower()
                except ValueError:
                    print "Please enter Yes or No"
                    continue

                try:
                    if calculation.lower() == "yes":
                        print ""
                        nop = float(raw_input("Enter Net Operating Profit value: "))
                        ec = float(raw_input("Enter Employed Capital value: "))
                        nopec = nop / ec
                        print "Return on Capital Employed = ", round(nopec, 2)
                        break

                    elif calculation.lower() == "no":
                        another_loop()
                    else:
                        print "Please enter Yes or No"
                except ValueError:
                    print "Please enter just a number"
                except ValueError:
                    print "Please enter just a number"
                    continue
            another_loop()
        elif select == 5:
            print "\nYou have selected Return on Equity. \nNet Income / Shareholder's Equity"
            while True:
                try:
                    print ""
                    calculation = bytes(raw_input("Would you like to perform this calculation? ")).lower()
                except ValueError:
                    print "Please enter Yes or No"
                    continue

                try:
                    if calculation.lower() == "yes":
                        print ""
                        ni = float(raw_input("Enter Net Income value: "))
                        se = float(raw_input("Enter Shareholder's Equity value: "))
                        nise = ni / se
                        print "Return on Equity = ", round(nise, 2)
                        break

                    elif calculation.lower() == "no":
                        another_loop()
                    else:
                        print "Please enter Yes or No"
                except ValueError:
                    print "Please enter just a number"
                except ValueError:
                    print "Please enter just a number"
                    continue
            another_loop()
        else:
            print "\nPlease select a number between 1 and 5"


# import Market
def market_prospect_ratios():
    print ("\nFour Types of Market Prospect Ratios")
    market_list = ["1. Earnings Per Share", "2. Price Earnings P/E Ratio", "3. Dividend Payout Ratio",
                   "4. Dividend Yield"]
    for i in market_list:
        print (i)

    while True:
        try:
            select = int(raw_input("\nSelect what type of Market Prospect Ratios you are looking for? "))
        except ValueError:
            print "\nPlease select a number between 1 and 4"
            continue

        if select == 1:
            print "\nYou have selected Earnings Per Share. \n(Net Income - Preferred Dividends)  / " \
                  "Weighted Average Common Shares Outstanding"
            while True:
                try:
                    print ""
                    calculation = bytes(raw_input("Would you like to perform this calculation? ")).lower()
                except ValueError:
                    print "Please enter Yes or No"
                    continue

                try:
                    if calculation.lower() == "yes":
                        print ""
                        ni = float(raw_input("Enter Net Income value: "))
                        pd = float(raw_input("Enter Preferred Dividends value: "))
                        wacso = float(raw_input("Enter Weighted Average Common Shares Outstanding value: "))
                        nipdwaco = (ni - pd) / wacso
                        print "Earnings Per Share = ", round(nipdwaco, 2)
                        break

                    elif calculation.lower() == "no":
                        another_loop()
                    else:
                        print "Please enter Yes or No"
                except ValueError:
                    print "Please enter just a number"
                except ValueError:
                    print "Please enter just a number"
                    continue
            another_loop()
        elif select == 2:
            print "\nYou have selected Price Earnings P/E Ratio. \nMarket Value Price Per Share / Earning Per Share"
            while True:
                try:
                    print ""
                    calculation = bytes(raw_input("Would you like to perform this calculation? ")).lower()
                except ValueError:
                    print "Please enter Yes or No"
                    continue

                try:
                    if calculation.lower() == "yes":
                        print ""
                        mvpps = float(raw_input("Enter Market Value Price Per Share value: "))
                        eps = float(raw_input("Enter Earning Per Share value: "))
                        mvppseps = mvpps / eps
                        print "Price Earnings P/E Ratio = ", round(mvppseps, 2)
                        break

                    elif calculation.lower() == "no":
                        another_loop()
                    else:
                        print "Please enter Yes or No"
                except ValueError:
                    print "Please enter just a number"
                except ValueError:
                    print "Please enter just a number"
                    continue
            another_loop()
        elif select == 3:
            print "\nYou have selected Dividend Payout Ratio. \nTotal Dividend / Net Income"
            while True:
                try:
                    print ""
                    calculation = bytes(raw_input("Would you like to perform this calculation? ")).lower()
                except ValueError:
                    print "Please enter Yes or No"
                    continue

                try:
                    if calculation.lower() == "yes":
                        print ""
                        td = float(raw_input("Enter Total Dividend value: "))
                        ni = float(raw_input("Enter Net Income value: "))
                        tdni = td / ni
                        print "Dividend Payout Ratio = ", round(tdni, 2)
                        break

                    elif calculation.lower() == "no":
                        another_loop()
                    else:
                        print "Please enter Yes or No"
                except ValueError:
                    print "Please enter just a number"
                except ValueError:
                    print "Please enter just a number"
                    continue
            another_loop()
        elif select == 4:
            print "\nYou have selected Dividend Yield. \nCash Dividends Per Share / Market Value Per Share"
            while True:
                try:
                    print ""
                    calculation = bytes(raw_input("Would you like to perform this calculation? ")).lower()
                except ValueError:
                    print "Please enter Yes or No"
                    continue

                try:
                    if calculation.lower() == "yes":
                        print ""
                        cdps = float(raw_input("Enter Cash Dividends Per Share value: "))
                        mvps = float(raw_input("Enter Market Value Per Share value: "))
                        cdpsmvps = cdps / mvps
                        print "Dividend Yield = ", round(cdpsmvps, 2)
                        break

                    elif calculation.lower() == "no":
                        another_loop()
                    else:
                        print "Please enter Yes or No"
                except ValueError:
                    print "Please enter just a number"
                except ValueError:
                    print "Please enter just a number"
                    continue
            another_loop()
        else:
            print "\nPlease select a number between 1 and 4"


# import Coverage
def coverage_ratios():
    print ("\nFour Types of Coverage Ratios")
    efficiency_list = ["1. Fixed Charge Coverage Ratio", "2. Debt Service Coverage Ratio"]
    for i in efficiency_list:
        print (i)

    while True:
        try:
            select = int(raw_input("\nSelect what type of Coverage Ratios you are looking for? "))
        except ValueError:
            print "\nPlease select a number between 1 and 2"
            continue
        if select == 1:
            print "\nYou have selected Fixed Charge Coverage Ratio. \n(EBIT + Fixed Charges Before Taxes) " \
                  "/ (Fixed Charges Before Taxes + Interest)"
            while True:
                try:
                    print ""
                    calculation = bytes(raw_input("Would you like to perform this calculation? ")).lower()
                except ValueError:
                    print "Please enter Yes or No"
                    continue

                try:
                    if calculation.lower() == "yes":
                        print ""
                        ebit = float(raw_input("Enter EBIT value: "))
                        fcbt = float(raw_input("Enter Fixed Charges Before Taxes value: "))
                        iv = float(raw_input("Enter Interest value: "))
                        ebitfcbtiv = (ebit + fcbt) / (fcbt + iv)
                        print "Fixed Charge Coverage Ratio = ", round(ebitfcbtiv, 2)
                        break

                    elif calculation.lower() == "no":
                        another_loop()
                    else:
                        print "Please enter Yes or No"
                except ValueError:
                    print "Please enter just a number"
                except ValueError:
                    print "Please enter just a number"
                    continue
            another_loop()
        elif select == 2:
            print "\nYou have selected Debt Service Coverage Ratio. \nOperating Income / Total Debt Service Costs"
            while True:
                try:
                    print ""
                    calculation = bytes(raw_input("Would you like to perform this calculation? ")).lower()
                except ValueError:
                    print "Please enter Yes or No"
                    continue

                try:
                    if calculation.lower() == "yes":
                        print ""
                        oi = float(raw_input("Enter Operating Income value: "))
                        tdsc = float(raw_input("Enter Total Debt Service Costs value: "))
                        oitdsc = oi / tdsc
                        print "Debt Service Coverage Ratio = ", round(oitdsc, 2)
                        break

                    elif calculation.lower() == "no":
                        another_loop()
                    else:
                        print "Please enter Yes or No"
                except ValueError:
                    print "Please enter just a number"
                except ValueError:
                    print "Please enter just a number"
                    continue
            another_loop()
        else:
            print "\nPlease select a number between 1 and 2"


# Start Function
def start():
    while True:
        try:
            choice = int(raw_input("\nWhat Sort of Equation are you looking for? "))
        except ValueError:
            print "\nMake sure you enter a number between 1 and 6"
            continue

        if choice == 1:
            liquidity_ratios()
        elif choice == 2:
            solvency_ratios()
        elif choice == 3:
            efficiency_ratios()
        elif choice == 4:
            profitability_ratios()
        elif choice == 5:
            market_prospect_ratios()
        elif choice == 6:
            coverage_ratios()
        else:
            print "\nMake sure you enter a number between 1 and 6"


# Do you want to lookup another financial ratio?
def another_loop():
    while True:
        try:
            another = bytes(raw_input("\nDo you want to lookup another financial ratio? ")).lower()
        except ValueError:
            print "Please enter Yes or No"
            continue

        if another.lower() == "yes":
            # print "Reset"
            os.system('cls')
            reset()

        elif another.lower() == "no":
            # print "Shutting Down"
            exit()
        else:
            print "Please enter Yes or No"


# Reset Program
def reset():
    # Program Start Here
    print ("\nWelcome to Accounting 101\n")
    print ("Here are the different types of financial ratio being offered")

    list_two = ["1. Liquidity Ratio", "2. Solvency Ratios", "3. Efficiency Ratios", "4. Profitability Ratios",
                "5. Market Prospect Ratios", "6. Coverage Ratios"]
    for a in list_two:
        print(a)
    start()


# Program Start Here
print ("\nWelcome to Accounting 101\n")
print ("Here are the different types of financial ratio being offered")

list_one = ["1. Liquidity Ratio", "2. Solvency Ratios", "3. Efficiency Ratios", "4. Profitability Ratios",
            "5. Market Prospect Ratios", "6. Coverage Ratios"]
for i in list_one:
    print(i)
start()
