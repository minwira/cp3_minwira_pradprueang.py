class Customer:
    name = ""
    lastname = ""
    age = 0
    def addCart (self):
        print("Added to " , self.name , self.lastname ,"'s cart")
custumer1 =Customer()
custumer1.name = "minwira"
custumer1.lastname = "pp"
custumer1.age = 22
custumer1.addCart()

custumer2 = Customer()
custumer2.name = "jackson"
custumer2.lastname = "wang"
custumer2.age = 27
custumer2.addCart()

custumer3 = Customer()
custumer3.name = "baby"
custumer3.lastname = "shark"
custumer3.age = 1
custumer3.addCart()

custumer4 = Customer()
custumer4.name = "mama"
custumer4.lastname = "moo"
custumer4.age = 5
custumer4.addCart()
