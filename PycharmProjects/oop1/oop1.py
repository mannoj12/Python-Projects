class Kettle(object):

    def __init__(self,make,price):
        self.make= make
        self.price=price
        self.on=False

kenwood = Kettle("kenwood",3.99)
print(kenwood.price)
print(kenwood.make)

kenwood.price=12.45
print(kenwood.price)



