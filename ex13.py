class A(object):
    def __init__(self):
        super(A, self).__init__()
        self.n1 = 100
        print("Constructing A instance")


class B(object):
    def __init__(self):
        super(B, self).__init__()
        self.n2 = 200
        print("Constructing B instance")


class C(A, B):
    def __init__(self):
        super(C, self).__init__()
        self.n3 = 300
        print("Constructing C instance")


def main():
    c1 = C()
    print("c1.n1 = {0}".format(c1.n1))
    print("c1.n2 = {0}".format(c1.n2))
    print("c1.n3 = {0}".format(c1.n3))

if __name__ == "__main__":
    main()