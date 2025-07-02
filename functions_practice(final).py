1.
def greet(name):
    return "Hello " + name + " !"
name=input("Enter name:") 
print(greet(name))

2.
def is_even(n):
    return True
n=int(input("Enter the no.:"))
if n%2==0:
    is_even(n)
else:
    print(n," is not even")
print(is_even(n))

3.
def add(a,b):
    return a+b
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print("The sum is :",add(a,b))

4.
def find_max(a, b, c):                       
    if a > b and a > c:
         return a
    elif b > a and b > c:
         return b
    else:
         return c
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
print("The maximum no is : ",find_max(a, b, c))
