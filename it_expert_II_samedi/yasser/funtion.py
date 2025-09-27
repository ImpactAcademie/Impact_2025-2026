def test():
    print("this is test")

def isNumberEven(a):
    if a%2==0:
        return True
    return False

int1=2044
if int1%2==0:
    print("number even")

def calc(a=0,b=5):
    print(a*b)

calc()
calc(4,9)

def calc1(*args):
    print(args[0]*args[1])
    print(args[1]*args[2])

calc1(1,3,6)

for i in range(6):
    if i==4:
        pass
    print(i)
    