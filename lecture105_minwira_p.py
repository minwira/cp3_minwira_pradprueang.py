class vehicle:
    lecenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Car(vehicle):
    def sayHello(self):
        print("Hello World")
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Pickup(vehicle):
    pass
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Van(vehicle):
    pass
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Estatecar(vehicle):
    pass
    def turnOnAirConditioner(self):
        print("Turn On : Air")


car1 = Car()
car1.turnOnAirConditioner()

pickup1 = Pickup()
pickup1.turnOnAirConditioner()

van1 = Van()
van1.turnOnAirConditioner()

Estatecar1 = Estatecar()
Estatecar1.turnOnAirConditioner()

