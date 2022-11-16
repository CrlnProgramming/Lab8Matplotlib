import matplotlib.pyplot as plt
plt.style.use('_mpl-gallery')

price = []
purchasesfile = []
budgetFile = [] 

def ReadFromFile(Temp):
    print("Available files: purchasesfile, price, budgetFile")
    enterNamefile = input("\tEnter name read file: ")
    with open(f'{enterNamefile}.txt','r') as f:
        Temp = f.readlines()
        f.close()
    return Temp

while True:
    try:
        print("\n")
        menuOption = input("\t B = Bild a graph, X = Exit\n")
        if (menuOption == 'B'):
            plt.plot(ReadFromFile(price))
            plt.plot(ReadFromFile(purchasesfile))
            plt.plot(ReadFromFile(budgetFile))
            plt.show()
        elif (menuOption == 'X'):
            print("\tU welcome!")
            break
        else:
            print("Error!")
    except BaseException:
        print("\tYou entered the wrong value.Try again\n")
