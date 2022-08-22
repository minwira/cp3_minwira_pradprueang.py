usernameInput = input("username : ")
passwordInput = input("password : ")
if usernameInput == "jkshop" and passwordInput == "1234":

    print("let'go shopping")
    print("---------jkshop----------")
    print("1.chocolate milk (price 65 (THB))")
    print("2.setrewbery milk (price 60(THB))")
    print("3.banana milk (price 50 (THB))")
    seclected = int(input("chose what you want to drink>> "))
    if seclected == 1:
        drink = "chocolate milk"
        price = 65
    elif seclected == 2:
        drink = "setrewbery milk"
        price = 60
    elif seclected==3:
        drink = "banana milk"
        price = 50
        print("drink your chose:",drink, ":",price, "THB")
        amountofdrink = int(input("please chose QTY: "))
        print("Summary : ",drink, ":",amountofdrink,"x",price,"=", price*amountofdrink,"THB")



