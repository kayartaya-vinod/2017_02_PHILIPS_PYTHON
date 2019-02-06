class Person:

    # constructor
    def __init__(self, _id=None, name=None, email=None, phone=None):
        if _id is not None and type(_id) is not int:
            raise Exception("Id must be a numeric value")

        self.id = id(self) if _id is None else _id
        self.name = name
        self.email = email
        self.phone = phone

    def say_hello(self):
        print("Hello, from %s" % ("a friend" if self.name is None else self.name))

# using the class name as a function call will create an instance (object)
# of the same class
p1 = Person(1, "John Doe")  # this is a call to the constructor (__init__) of class Person
print("type of p1 is %s" % type(p1))
print("id(p1) is %s" % id(p1))
p1.say_hello()

print("-"*50)
p2 = Person(name="Vinod", email="vinod@vinod.co", _id=123)
print("id(p2) is %s" % id(p2))

print("p1 == p2 is %s" % (p1 == p2))
print("p1 is p2 is %s" % (p1 is p2))
p2.say_hello()

p3 = Person()
p3.say_hello()



