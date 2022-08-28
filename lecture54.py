def login():
    usernameInput = input("username : ")
    passwordInput = input("password : ")
    if usernameInput == "jkshop" and passwordInput == "1234":
        return True
    else:
        return  False
def showMenu():
    print("let'go shopping")
    print("---------jkshop----------")
    print("1.chocolate milk (price 65 (THB))")
    print("2.setrewbery milk (price 60(THB))")
    print("3.banana milk (price 50 (THB))")
def menuSelect():
    seclected = int(input("chose what you want to drink>> "))
    if seclected == 1:
        drink = "chocolate milk"
        price = 65
    elif seclected == 2:
        drink = "setrewbery milk"
        price = 60
    elif seclected == 3:
        drink = "banana milk"
        price = 50
        return seclected
def vatCalculator(price):
    vat = 7
    result = price + (price * vat / 100)
    return result
def priceCalculator():
    drink1 = int(input("First Product Price : "))
    drink2 = int(input("Second Product Price : "))
    return vatCalculator(drink1 + drink2)


print(priceCalculator())