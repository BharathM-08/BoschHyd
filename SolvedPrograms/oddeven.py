def oddeven(a):
    if(a%2==0):
        return "Even"
    else:
        return "Odd"

a = int(input("Enter the Number: "))
print(oddeven(a))