def add(a,b):
    return a+b 

def sub(a,b):
    return a-b 

def mul(a,b):
    return a*b 

def div(a,b):
    return a//b 

print("Simple Calculator")
a = int(input("Enter First  Value: "))
b = int(input("Enter Second Value: "))
while(True):
    print("1.Add \n2.Subtract \n3.Multiplication \n4.Divide \n5.Exit")
    print("Enter your Choice :")
    ch = int(input())
    match(ch):
        case 1:
            print(add(a,b))
        case 2:
            print(sub(a,b))
        case 3:
            print(mul(a,b))
        case 4:
            print(div(a,b))
        case 5:
            print("Exitting")
            break 