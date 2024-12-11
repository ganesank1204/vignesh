def fadd(a,b):
    return a+b
def fsub(a,b):
    return a-b
def fmultiply(a,b):
    return a*b
def fdivision(a,b):
    return a/b
print("BASIC CALCULATOR")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
choice=(int(input("enter your choice")))
a=(int(input("enter the first number")))
b=(int(input("enter the second number")))
if choice==1:
    print(fadd(a,b))
elif choice==2:
    print(fsub(a,b))
elif choice==3:
    print(fmultiply(a,b))
elif choice==4:
    print(fdivision(a,b))
else:
    print("choice is invalid")