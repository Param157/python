# For Loop
# While Loop

# for i in range(1, 11):
#     print(i, end=" ")

# i = 1
# while(i<=10):
#     print(i, end=" ")
#     i = i+1



# check a number is strong number (145 = 1+24+120) (sum of factorial of each digit of a number should be equals to number)
# num = 145
# temp = num
# sum = 0
# while(num>0):
#     rem = num%10
#     fact = 1
#     for i in range(1,rem+1):
#         fact = fact * i
#     sum = sum + fact
#     num = num//10
# if(sum == temp):
#     print("Strong number")
# else:
#     print("Not a Strong number")


# Print multiplication table of a number
# num = int(input("Enter a number: "))
# print("Multiplication Table of ",num)
# for i in range(1,11):
#     print("",num,"*",i,"=",i*num)





# Print sum of n natural numbers (10 = 1+2+3+4+5)
# a=int(input("Enter a natural number: "))
# num=a
# b=0
# while(num>0):
#     b=b+num
#     num=num-1
# print("The sum of first",a,"natural number is",b)



# Print all even numbers between a given range
# start = int(input("Enter the start of range: "))
# end = int(input("Enter the end of range: "))
# print("Even No. is:",end=" ")
# for num in range(start, end + 1):
#     if(num%2==0):
#         print(num, end=" ")



# Print all odd numbers between a given range
# a=int(input("Enter the start of range: "))
# b=int(input("Enter the end of range: "))
# print("Odd No. is:",end=" ")
# for num in range(a, b + 1):
#     if(num%2!=0):
#         print(num, end=" ")




# Print factorial of a given number (5 = 1*2*3*4*5)
# num = 5
# fact = 1
# for i in range(1,num+1):
#     fact = fact * i
# print(fact)



# Print factorial of a given number
# num=int(input("Enter a number: "))
# fact = 1
# for i in range(1,num+1):
#     fact = fact * i
# print(fact)











# print reverse of a number (123 = 321)

# a = int(input("Enter Number: "))
# rev=0
# while(a>0):
# b=a%10
# rev=rev*10+b
# a=a//10
# print("Reverse of number is:",rev)





# count digits in a number (1234 = 4)




# print sum of all digits in a number (123 = 6)
# a=int(input("Enter a number: "))
# b=0
# while(a>0):
#     c=a%10
#     b=b+c
#     a=a//10
# print("Total Sum of digits is: ",b)




# check a number is armstrong number (153 = 1+125+27) (sum of cube of each digit of a number should be equals to number)
# a=int(input("Enter a number: "))
# d=0
# temp=a
# while(a>0):
#     c=a%10
#     b=c*c*c
#     d=d+b
#     a=a//10
# if(temp==d):
#       print("",temp,"is an armstrong number")
# else:
#       print("",temp,"is not an armstrong number") 



# check a number is strong number (145 = 1+24+120) (sum of factorial of each digit of a number should be equals to number)


# check a palindrome number (121) (left to right or right to left should be equal)

# a = int(input("Enter a Number: "))
# temp=a
# rev=0
# while(a>0):
#     b=a%10
#     rev=rev*10+b
#     a=a//10
# if(temp==rev):
#     print("",temp,"is a palindrome number.")
# else:
#     print("",temp,"is not a palindrome number.")



# check a number is perfect number (28 = 1+2+4+7+14) (sum of divisiors of a number should be equals to that number)
# a = int(input("Enter a Number: "))
# b=0
# temp=a
# for i in range(1,a):
#     if(a%i==0):
#         b=b+i
# if(b==temp):
#     print("",temp,"is a perfect number.")
# else:
#     print("",temp,"is not a perfect number.")
    


