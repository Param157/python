def addition(a,b):
    print("Addition is:",a+b)

def oddeven(num):
    if num%2==0:
        print(f"{num} is a Even Number")
    else:
        print(f"{num} is a Odd Number")

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    print("Factorial is: ",fact)