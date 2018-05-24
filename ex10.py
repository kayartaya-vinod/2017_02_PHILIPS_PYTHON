class Employee:
    def __init__(self, empno=None, name=None, salary=35000):
        self.__empno = empno
        self.__name = name
        self.__salary = salary

    def set_empno(self, empno):
        if type(empno) is not int:
            raise ValueError("EMPNO must be a int value")
        self.__empno = empno

    def get_empno(self):
        return self.__empno

    def set_name(self, name):
        if type(name) is not str:
            raise ValueError("NAME must be a str value")
        self.__name = name

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def display(self):
        print("Emp#: %s" % self.__empno)
        print("Name: %s" % self.__name)
        print("Salary: %s" % self.__salary)
        print("-"*50)


if __name__ == "__main__":
    e1 = Employee()
    e1.set_empno(7654)
    # e1.__name = "John Doe"
    e1.set_name("John Doe")
    e1.display()

    e2 = Employee(7788, "Scott", 45000)
    e2.display()

    print("{0} earns Rs.{1} as monthly salary".format(e2.get_name(), e2.get_salary()))
