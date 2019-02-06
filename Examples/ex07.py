filename = "./dateutils.py"

x = open(filename, "rt")

# txt = x.read()

lines = x.readlines()

for txt in lines:
    print(txt, end="")

x.close()

