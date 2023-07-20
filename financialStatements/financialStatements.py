import pdfplumber
files = ['report/pfs/2_PFS_JAMEY CUTTER_052018s.pdf','report/pfs/2_PFS_N MERAIYA FEB 2018.pdf']

# pdf = pdfplumber.open(files[0])
# print(pdf.pages[0].extract_text()
#       .replace("_","")
#     #   .replace("…","")
#       .replace(".","")
#       .replace("\n"," ")
#       .split(" ")
#     )

# indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").split(" ").index("Bonds…………………………………$")
# print(pdf.pages[0].extract_text()
#       .replace("_","")
#     #   .replace("…","")
#       .replace(".","")
#       .replace("\n"," ")
#       .split(" ")[indexRightAfterBonds + 1]
#     )


# def getCashOnHand(files):
#     myList = []
#     for file in files:
#         pdf = pdfplumber.open(file)
#         indexRightAfterCash = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").split(" ").index("Cash")
#         cashNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterCash - 1]
#         if cashNumber == '':
#             myList.append(0)
#         else:
#             myList.append(int(cashNumber))
#     return myList

def getCashOnHand(file):
    pdf = pdfplumber.open(file)
    indexRightAfterCash = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").split(" ").index("Cash")
    cashNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterCash - 1]
    if cashNumber == '':
        return 0
    else:
        return int(cashNumber)

# print(getCashOnHand('report/pfs/2_PFS_N MERAIYA FEB 2018.pdf'))

def getSavingsAccount(file):
    pdf = pdfplumber.open(file)
    indexRightAfterCash = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").split(" ").index("Accounts…………………………………$")
    cashNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterCash + 1]
    if cashNumber == '':
        return 0
    else:
        return int(cashNumber)



def getCash(file):
    cashOnHandList = getCashOnHand(file)
    savingsAccountList = getSavingsAccount(file)
    return cashOnHandList + savingsAccountList

# print(getCash('report/pfs/2_PFS_N MERAIYA FEB 2018.pdf'))


def getMarketableSecurities(file):
    pdf = pdfplumber.open(file)
    indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").split(" ").index("Bonds…………………………………$")
    stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").split(" ")[indexRightAfterBonds + 1]
    if stocksAndBondsNumber == '':
        return 0
    else:
        return int(stocksAndBondsNumber)


def getTotalLiquidAssets(file):
    cashList = getCash(file)
    marketableSecuritiesList = getMarketableSecurities(file)

    return cashList + marketableSecuritiesList


def getPrimaryResidence(file):
    pdf = pdfplumber.open(file)
    indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("Estate…………………………………………$")
    stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds - 2]
    if stocksAndBondsNumber == '':
        return 0
    else:
        return int(stocksAndBondsNumber)


def getIRA(file):
    pdf = pdfplumber.open(file)
    indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("Account………………$")
    stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds + 1]
    if stocksAndBondsNumber == '':
        return 0
    else:
        return int(stocksAndBondsNumber)


def getLifeInsurance(file):
    pdf = pdfplumber.open(file)
    indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("Only……$")
    stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds + 1]
    if stocksAndBondsNumber == '':
        return 0
    else:
        return int(stocksAndBondsNumber)



def getNotesReceivable(file):
    pdf = pdfplumber.open(file)
    indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("Receivable……………………$")
    stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds + 1]
    if stocksAndBondsNumber == '':
        return 0
    else:
        return int(stocksAndBondsNumber)


def getBusinessValues(file):
    pdf = pdfplumber.open(file)
    indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("Assets…………………………………………$")
    stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds - 3]
    if stocksAndBondsNumber == '':
        return 0
    else:
        return int(stocksAndBondsNumber)


def getAutomobiles(file):
    pdf = pdfplumber.open(file)
    try:
        indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("Automobiles…………………………………………$")
        stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds - 1]
        if stocksAndBondsNumber == '':
            return 0
        else:
            return int(stocksAndBondsNumber)
    except:
            return 0


def getPersonalProperty(file):
    pdf = pdfplumber.open(file)
    try:
        indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("Property……………………………$")
        stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds - 3]
        if stocksAndBondsNumber == '':
            return 0
        else:
            return int(stocksAndBondsNumber)
    except:
            return 0



def getTotalOtherAssets(file):
    iraList = getIRA(file)
    lifeInsuranceList = getLifeInsurance(file)
    notesReceivableList = getNotesReceivable(file)
    businessValuesList = getBusinessValues(file)
    automobilesList = getAutomobiles(file)
    personalPropertyList = getPersonalProperty(file)

    return iraList + lifeInsuranceList + notesReceivableList + businessValuesList + automobilesList + personalPropertyList


def getTotalAssets(file):
    totalOtherAssetsList = getTotalOtherAssets(file)
    primaryResidenceList = getPrimaryResidence(file)
    totalLiquidAssetsList = getTotalLiquidAssets(file)

    return totalOtherAssetsList + primaryResidenceList + totalLiquidAssetsList


def getTotalREMortgage(file):
    pdf = pdfplumber.open(file)
    try:
        indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("Estate…………………$")
        stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds + 1]
        if stocksAndBondsNumber == '':
            return 0
        else:
            return int(stocksAndBondsNumber)
    except:
            return 0


def getAccountsPayable(file):
    pdf = pdfplumber.open(file)
    try:
        indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("Payable……………………………$")
        stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds + 1]
        if stocksAndBondsNumber == '':
            return 0
        else:
            return int(stocksAndBondsNumber)
    except:
            return 0


def getNotesPayable(file):
    pdf = pdfplumber.open(file)
    try:
        indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("Others………$")
        stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds + 1]
        if stocksAndBondsNumber == '':
            return 0
        else:
            return int(stocksAndBondsNumber)
    except:
            return 0


def getInstallmentAccountsAuto(file):
    pdf = pdfplumber.open(file)
    try:
        indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("(Auto)…………………$")
        stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds - 7]
        if stocksAndBondsNumber == '':
            return 0
        else:
            return int(stocksAndBondsNumber)
    except:
            return 0


def getInstallmentAccountsOther(file):
    pdf = pdfplumber.open(file)
    try:
        indexRightAfterBonds = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ").index("(Other)………………$")
        stocksAndBondsNumber = pdf.pages[0].extract_text().replace("_","").replace(".","").replace("\n"," ").replace(",","").split(" ")[indexRightAfterBonds - 7]
        if stocksAndBondsNumber == '':
            return 0
        else:
            return int(stocksAndBondsNumber)
    except:
            return 0


def getInstallmentAccounts(file):
    totalOtherAssetsList = getInstallmentAccountsAuto(file)
    primaryResidenceList = getInstallmentAccountsOther(file)
    return totalOtherAssetsList + primaryResidenceList


def getTotalLiabilities(file):
    totalREMortageList = getTotalREMortgage(file)
    accountsPayableList = getAccountsPayable(file)
    notesPayableList = getNotesPayable(file)
    installmentAccountsList = getInstallmentAccounts(file)
    return totalREMortageList + accountsPayableList + notesPayableList + installmentAccountsList


def getNetWorth(file):
    totalAssetsList = getTotalAssets(file)
    totalLiabilities = getTotalLiabilities(file)
    return totalAssetsList + totalLiabilities


def getAbsoluteTotal(file):
    #this total is the same as total assets but im gonna rewrite it just because
    absoluteTotal = getTotalAssets(file)
    return absoluteTotal

# def masterMethod(file):
    
#     cashOnHand = getCashOnHand(files)
#     savingsAccount = getSavingsAccount(files)
#     cash = getCash()
#     ms = getMarketableSecurities(files)
#     tla = getTotalLiquidAssets()
#     pr = getPrimaryResidence(files)
#     ira = getIRA(files)
#     li = getLifeInsurance(files)
#     nr = getNotesReceivable(files)
#     bv = getBusinessValues(files)
#     a = getAutomobiles(files)
#     pp = getPersonalProperty(files)
#     toa = getTotalOtherAssets(files)
#     ta = getTotalAssets(files)
#     trm = getTotalREMortgage(files)
#     ap = getAccountsPayable(files)
#     np = getNotesPayable(files)
#     iaa = getInstallmentAccountsAuto(files)
#     iao = getInstallmentAccountsOther(files)
#     ia = getInstallmentAccounts(files)
#     tl = getTotalLiabilities()
#     nw = getNetWorth()
#     at = getAbsoluteTotal()

#     return cashOnHand,savingsAccount,cash,ms,tla,pr,ira,li,nr,bv,a,pp,toa,ta,trm,ap,np,iaa,iao,ia,tl,nw,at


# # start_time = time.perf_counter()  # get the start time
# # print(masterMethod(files))
# # end_time = time.perf_counter()  # get the end time

# # elapsed_time = end_time - start_time  # calculate the elapsed time
# # print(f"Elapsed time: {elapsed_time:.6f} seconds")  # print the elapsed time

# class financialStatements:
#     def __init__(self,files):
#         self.cashOnHand = getCashOnHand(files)
#         self.savingsAccount = getSavingsAccount(files)
#         self.cash = getCash()
#         self.markertableSecurities = getMarketableSecurities(files)
#         self.totalLiquidAssets = getTotalLiquidAssets()
#         self.primaryResidence = getPrimaryResidence(files)
#         self.ira = getIRA(files)
#         self.lifeInsurance = getLifeInsurance(files)
#         self.notesRecievable = getNotesReceivable(files)
#         self.businessValues = getBusinessValues(files)
#         self.automobiles = getAutomobiles(files)
#         self.personalProperty = getPersonalProperty(files)
#         self.totalOtherAssets = getTotalOtherAssets(files)
#         self.totalAssets = getTotalAssets(files)
#         self.totalREMortgage = getTotalREMortgage(files)
#         self.accountsPayable = getAccountsPayable(files)
#         self.notesPayable = getNotesPayable(files)
#         self.installmentAccountsAuto = getInstallmentAccountsAuto(files)
#         self.installmentAccountsOther = getInstallmentAccountsOther(files)
#         self.installmentAccounts = getInstallmentAccounts(files)
#         self.totalLiabilites = getTotalLiabilities()
#         self.netWorth = getNetWorth()
#         self.grandTotal = getAbsoluteTotal()

# print(
#     financialStatements(files).cashOnHand,
#     financialStatements(files).savingsAccount,
#     financialStatements(files).cash,
#     financialStatements(files).grandTotal,
#     financialStatements(files)
#       )