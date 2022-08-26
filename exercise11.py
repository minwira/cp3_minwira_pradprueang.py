number = int(input("input your number:"))
for x in range(number):
        print(" " *(number - x),"*"*(x*2+1))

number = int(input())
for i in range(number):
    text =" "
    print(" " *(number-1),"*"*(((i+1)*2)-1))
    number-=1
    i+=1
