menulist  = []
pricelist = []

def showBill():
    totalprice = 0
    print("----My Food----")
    for number in range(len(menulist)):
        print(menulist[number],pricelist[number])
        totalprice+= int(pricelist[number])
    print("Total :",totalprice)

while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menprice = input("Price :")
        menulist.append(menuName)
        pricelist.append(menprice)

showBill()
