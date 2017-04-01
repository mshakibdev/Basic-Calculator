a = int(input('Enter first Number: '))
b = int(input('Enter first Number: '))
print('''    Press 1 for Summation
    press 2 for Subtraction
    press 3 for Multiplication
    press 4 for Division''')

d = int(input())

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
x = div(a,b)
s = add(a,b)
r = sub(a,b)
t = mul(a,b)

if d==1:
    print(a,'+',b,'=',s)
elif d==2:
    print(a,'-',b,'=',r)
elif d==3:
    print(a,'*',b,'=',t)
elif d==4:
    print(a,'/',b,'=',x)
