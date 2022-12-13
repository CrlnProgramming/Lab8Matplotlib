import matplotlib.pyplot as plt #libr for bars

#Declaring lists and dictionaries
price = []
purchasesFile = []
budgetFile = []
DictPrice = {}
DictBudgetFile = {}
DictDay = {}

#Function for read from files 
def ReadFromFile(_tempData):
    #tryCatch construction for error handling
    try:
        print("Available files: price, budgetFile, purchasesfile")
        enterNamefile = input("\tEnter name read file: ")
        #with open -> safly opening files  
        with open(f'{enterNamefile}.txt','r') as f:
            #reading files on line end edding in temp values
            _tempData = f.readlines()
            #closing a file
            f.close()
        return _tempData 
    except:
        print("The file name is written incorrectly. Please try again")

#Function-call with parameters "price" and adding instance -> readListPrice
readListPrice = ReadFromFile(price)
#Function-call with parameters "budgetFile" and adding instance -> readListBudgetFile
readListBudgetFile = ReadFromFile(budgetFile)
#Function-call with parameters "purchasesFile" and adding instance -> readListPurchasesFile
readListPurchasesFile = ReadFromFile(purchasesFile)

#FormatEmployee its function for format list and remove unnecessary symbols
def formatEmployee(_readList):
    #Remove "/n" on lists
    _tempFirstList = [item[:-1] for item in _readList]
    #Splitting the sheet into pieces and eating into a list
    _tempSecondList = [item.strip().split(",") for item in _tempFirstList]
    return _tempSecondList

#Function-call with parameters "readListPrice" and adding instance -> formatForPriceList
formatForPriceList = formatEmployee(readListPrice)
#Function-call with parameters "readListBudgetFile" and adding instance -> formatForBudgetFileList
formatForBudgetFileList = formatEmployee(readListBudgetFile)
#Function-call with parameters "readListPurchasesFile" and adding instance -> formatForPurchasesList
formatForPurchasesList = formatEmployee(readListPurchasesFile)

#Function cleaves out the meaning and enters them into the dictionary
def TemplateToDictiunary(_readList, _dictionary):
    #Extracts the value and pulls it apart by lines   
    for item in _readList:
        TempList1 = item[0]
        TempList2 = item[1:]
        #Splitting the sheet into pieces and eating into a list
        b = [item.strip().split("$") for item in TempList2]
        #Extracts the value and adding in dictionary 
        for item in b:
            line1 = item[1]

        _dictionary[TempList1] = line1

    return _dictionary

#Function-call with parameters "formatForPriceList, DictPrice" and adding instance -> templatePriceListForDict
templatePriceListForDict = TemplateToDictiunary(formatForPriceList, DictPrice)
#Function-call with parameters "formatForBudgetFileList, DictBudgetFile" and adding instance -> templateBudgetFileListForDict
templateBudgetFileListForDict = TemplateToDictiunary(formatForBudgetFileList, DictBudgetFile)

def TemplateDic(_readList, _dictionary):
    #Extracts the value and pulls it apart by lines
    for item in _readList:
        line = item[0]
    
        #Search day on line
        if (line[0:3] == 'DAY'):
            _dictionary[line] = len(line)#calculate items 
        
    return _dictionary

#Function-call with parameters "formatForPurchasesList, DictDay" and adding instance -> filledPurchasesDic
filledPurchasesDic = TemplateDic(formatForPurchasesList, DictDay)

def MenuBar(_dictionary1,_dictionary2, _dictionary3):
    try:
        menuOption = input("1 - Graf#1, 2 - Graf#2 , Graf#- d3: ")
    
        if (menuOption == "1"):
            ax = plt.subplot()

            x = []
            y = []

            #adds it back to the list from the dictionary.needed for rendering by x and y
            for k, v in _dictionary1.items():
                x.append(k)
                y.append(v)

            ax.bar(x,y) #Rendering

            ax.set_ylabel('Price') #Lable on y
            ax.set_title('Total Price Items in a Week') #Title 

            plt.show()

        elif (menuOption == "2"):
            ax = plt.subplot()

            x = []
            y = []

            for k, v in _dictionary2.items():
                x.append(k)
                y.append(v)

            ax.bar(x,y)

            ax.set_ylabel('Budget')
            ax.set_title('Budget in a Week')

            plt.show()

        elif (menuOption == "3"):
            ax = plt.subplot()

            x = []
            y = []

            for k, v in _dictionary3.items():
                x.append(k)
                y.append(v)

            ax.bar(x,y)

            ax.set_ylabel('Cost')
            ax.set_title('Total cost on weekday')

            plt.show()

    except:
        print("Incorrect value. Please try again")

#Function-call with parameters "templatePriceListForDict, templateBudgetFileListForDict, filledPurchasesDic"
MenuBar(templatePriceListForDict, templateBudgetFileListForDict, filledPurchasesDic)
MenuBar(templatePriceListForDict, templateBudgetFileListForDict, filledPurchasesDic)
MenuBar(templatePriceListForDict, templateBudgetFileListForDict, filledPurchasesDic)