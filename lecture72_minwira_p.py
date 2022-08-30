menuList = []

def showBill():
    totalprice = 0
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        totalprice += int(menuList[number][1])
        print("Total :", totalprice)

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName, menuPrice])

showBill()