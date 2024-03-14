# ! Eg:3
# ? Take values of length and breadth of a
# ? from user and check if it is square or not.

# length = int(input("Enter the length"))
# breadth = int(input("Enter the breadth"))
# if length == breadth:
#     print("it is a square")
# else:
#     print("it is not a square")

# ! Eg:4
#python program to check whether the
# given integer is a multiple of both 5 and 7

#n = int(input("Enter the number: "))
#if n%5==0 and n%7==0:
#    print("yes")
#else:
#   print("no")
    
# ! Eg:5

# price = int(input("Enter the price: "))
# amount = 0
# if price>=100000:
#     discount = 100000*(6/100)
#     value = price-discount
#     amount=value*(15/100)
#     total=value+amount
# else:
#     tax = price*(5/100)
#     total = price+tax
# print("the onroad cost of bike is: ",total)
    
# ! Eg:6

#a = 7
#b = 0
#c = 3

#if a>b and a>c:
#    print("A is greater")
#elif b>a and b>c:
#    print("B is greater")
#elif c>a and c>b:
#    print("C is greater")

# ! Eg:7
# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

#mark = int(input("enter mark: "))
#if mark>=80 and mark<=100:
#    print("A")
#elif mark>=60 and mark<80:
#    print("B")
#elif mark>=50 and mark<60:
#    print("C")
#elif mark>=40 and mark<50:
#    print("D")
#else:
#   print("fail")


# ! --> short hand if else
# Eg:1
#a = 90
#b = 6
#if a>b:
#    print("A")
#else:
#   print("B")


# ? --> using short hand if else
# * Rules
# 1.)statement inside the if condition have to be present at first
# 2.)elif cannot be used in short hand if else
# 3.)always it have to end with else

# print("A") if a>b else print("B")

# ! code to check the given char is vowel or consonent
# char  = input("Enter the char: ")
# if char=="a" or char =='e' or char =='i' or char =='o' or char =='u':
#     print("is a vowel")
# else:
#     print("its consonent")
 
# ? or

# str1 = "aeiouAEIOU"
# if char in str1:
#     print("vowel")
# else:
#     print("consonent")


# ? using shorthand if else
# char = input("Enter the char: ")
# str1 = "aeiouAEIOU"
# print("vowels") if char str1 else print("consonent")


# ! ---> elif ladder using short hand if else
# Eg:1
# ? Find greatest among 3 variables using short hand if else

#a = 8
#b = 5
#c = 9

#print("A is greater") if a>b and a>c else print("B is greater")
# if b>a and b>c else print("C is greater")

# ! ----------> looping

# looping can be implimented using
# for loop
# while loop

# ----> for loop
# ? it is used to iterate the iterables eg(string, list, tuple, etc...)

# todo --> syntax for loop

# ! for syntax in c
# for(i=0;i<10;i++){
#     printf("hello");
# }


# ? Eg:1
# To print the value from 1 to10 using for loop

#for i in range(0, 10):
#    print(i)

# ? Eg:2
#for val in range(1, 15, 2):
#    print(val)

#for val in range(1, 15, 3):
#    print(val)


# ? Eg:3
# to decrement the value

#for val in range(10, 0, -1):
#    print(val)

#for val in range(10, 0, -2):
#    print(val)

#for val in range(10, 0, 1):
#    print(val)

# ? Eg:4
# ! print the output of 7th multiplication table from 21 to 43

# ----> method:1
for val in range(1, 10+1,):
    print('7','x',val,'=',val*7)

# --> Method:2
for val in range(1, 10+1,): 
 ans = "7 x {} = {}"
 print(ans.format(val, val*7))


for val in range(1,25):
    print(val)
    if val ==6:
        break

# !
































