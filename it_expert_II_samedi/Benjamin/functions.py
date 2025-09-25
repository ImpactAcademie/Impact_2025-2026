def test():
    print("Salut")

test()

def isNumberEven(a):
    if a%2 ==0:
        return True
    return False

int1 = 2215

if isNumberEven(int1):
    print("Number even")
else:
    print("pas pair")

def calc(a=0, b=5):
    print(a*b)
calc()

def calc1(*args):
    print(args[0] * args[1])
    print(args[1] * args[2])
calc1(1,3,2)

for i in range(6):
    if i == 4:
        break
    print(i)