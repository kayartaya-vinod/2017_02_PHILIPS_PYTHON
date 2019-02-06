class Product(object):
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__price = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if type(id) is not int:
            raise ValueError("ID must be an int value")
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            raise Exception("Invalid price;  must be > 0")

        self.__price = price

    def __eq__(self, other):
        print("id(self)={0}, id(other)={1}".format(id(self), id(other)))
        if type(other) in (int, float):
            return self.__price == other
        elif type(other) is str:
            return self.__name == other
        elif type(other) is Product:
            return self.__price == other.price
        else:
            raise TypeError("Invalid type for comparison")

    def __iadd__(self, other):
        if type(other) in (int, float):
            if self.price is None:
                self.price = 0
            self.price += other
        elif type(other) is str:
            if self.name is None:
                self.name = ""
            self.name += other
        else:
            raise TypeError("You may append only str, int or float")

        return self

if __name__ == "__main__":
    p1 = Product()
    p1.id = 123

    p1 += 50
    p1 += " (new)"

    print("p1.id is {0}".format(p1.id))
    print("p1.name is {0}".format(p1.name))
    print("p1.price is {0}".format(p1.price))


def test():
    p1 = Product()

    print("p1.id is {0}".format(p1.id))
    print("p1.name is {0}".format(p1.name))
    print("p1.price is {0}".format(p1.price))

    print("-"*80)

    p1.id = 123
    p1.name = "Nokia 1100"
    p1.price = 999

    print("p1.id is {0}".format(p1.id))
    print("p1.name is {0}".format(p1.name))
    print("p1.price is {0}".format(p1.price))
    print("-" * 80)

    p2 = Product()
    p2.id = 123
    p2.name = "Nokia 1100"
    p2.price = 999

    p1.__eq__(p2)
    print("id(p1) = {0}, id(p2) = {1}".format(id(p1), id(p2)))
    print("p1 == p2 is {0}".format(p1 == p2))

    print("id(p1) = {0}, id(999) = {1}".format(id(p1), id(999)))
    print("p1 == 999 is {0}".format(999 == p1))
    print("p1 == \"Nokia 1100\" is {0}".format(p1 == "Nokia 1100"))
    print("p1 == True is {0}".format(p1 == True))

    print("p1 is p2 is {0}".format(p1 is p2))

