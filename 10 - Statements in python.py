# if else elif
# if(condition):
#     statement
# else:
#     statement

# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# if(num1>num2):
#     print("Num1 is greater than Num2")
# elif(num1==num2):
#     print("Num1 & Num2 are same")
# else:
#     print("Num2 is greater than Num1")

# a = int(input("Enter number: "))
# b = int(input("Enter number: "))
# c = int(input("Enter number: "))

# if(a>b and a>c):
#     print("A is greater")
# elif(b>a and b>c):
#     print("B is greater")
# else:
#     print("C is greater")

# a = 33
# if(a%2==0):
#     print("Even")
# else:
#     print("Odd")



# 1) - Check a number is divisible by 4 & 6
# a=int(input("Enter a number: "))
# if(a%4==0 and a%6==0):
#     print("",a,"is divisible by 4 and 6")
# else:
#     print("",a,"is not divisible by 4 and 6")
    
    

# 2) - Check a year is leap year or not 
# a=int(input("Enter the Year: "))
# if(a%4==0 and a!=1700 and a!=1800 and a!=1900):
#     print("",a,"is a leap year.")
# else:
#     print("",a,"is not a leap year.")
                



# 3) - Student marks 60 - 100 --> 1st Division
# 45 - 59 --> 2nd Division
# 33 - 44 --> 3rd Division
# less than 33 --> Failed
# a=int(input("Enter the Student Marks: "))
# b=int(input("Enter the Maximum Marks: "))
# c=(a/b)*100
# print("Percentage of Student Marks",c)
# if(c>=60):
#     print("1st Division")
# elif(c>=45):
#     print("2nd Division")
# elif(c>=33):
#     print("3rd Division")
# else:
#     print("Failed")



# 4) - Electricity Unit 0 - 100 --> "No Bill" 
# 101 - 200 --> 5 Rs per unit --- (110 -- 50 Rs)
# 201 - 300 --> 10 Rs per unit --- (220 -- 700 Rs)
a=int(input("Enter Electricity Unit: "))
if(a<=100):
    print("Your Electricity Bill is Zero")
elif(a<=200):
    b=a%100
    c=b*5
    print("Your Electricity Bill is ",c)
elif(a<=300):
    b=a%100
    c=b*10
    print("Your Electricity Bill is ",c)
else:
    b=a%100
    c=b*15
    print("Your Electricity Bill is ",c)

