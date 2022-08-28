def vatcalculate(total):
    result = total+(total*7/100)
    return result
price = int(input("PriceB : "))
print(vatcalculate(price))