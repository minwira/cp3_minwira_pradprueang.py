systemMenu = {"ข้าวหมกไก่":45,"ข้าวมันไก่":50,"ข้าวปลาทอด":35,"ข้าวไก่ทอด":55}
menulist  = []

def showBill():
    totalprice = 0
    print("----My Food----")
    for number in range(len(menulist)):
        print(menulist[number][0],menulist[number][1])
        totalprice+= int(menulist[number][1])
    print("Total :",totalprice)

while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:

        menulist.append([menuName,systemMenu[menuName]])

showBill()
