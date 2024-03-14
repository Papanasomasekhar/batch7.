# ----> while loop
# ----> break using while loop

# Eg:1
# 1.)Iterate from 20 to 30 and break the loop in 27

#i = 20
#while i<30:
#    if i == 27:
#        break
#    print(i)
#    i+=1

# 2.)

#i = 20
#while i<31:
#    print(i)
#    if i == 27:
#        break
#    i+=1

'''
i = 20
while i<31:
    if i == 27:
        print(i)
        break
    i+=1
'''
# ! -----> continue
# ----> Eg:1
'''
i = 20
while i<31:
    if i==27:
        continue
    print(i)
    i+=1
'''   

# !! Eg:2
'''
i = 20
while i<31:
    i+=1
    if i==27:
        continue
    print(i)
'''

# ! Eg:5
# while to iterate from 12 to 22
# find the sum of all numbers
'''
i = 12
sum = 0
while i<22:
    i+=1
    sum = sum+i
print(sum)
'''    
# ! Eg:6
# find the average of value from 20 to 25
'''
i = 20
sum = 0
while i<25:
    i+=1
    sum=sum+i
avg=sum/5
print(avg)
'''
'''
i = 20
sum = 0
count = 0
while i<25:
    sum=sum+i
    count+=1
    i+=1
print(sum/count)

# ! --------> Nested for loop
# Eg:1

for i in range(1, 3):
    for j in range(1,4+1):
        print(i, j)
        

# Eg:2
# * * * * 
# * * * * 
# * * * * 
# * * * * 
for row in range(2000):
    for col in range(5):
        print("*", end=" ")
    print()


# ! to print stars in right angled triangle

for row in range(0,6):
    for col in range(0,row+1):
        print("*",end="")
    print()

    
#******
#*****
#****
#***
#**
#*

for row in range(0,6):
    for col in range(row,6):
        print("*",end=" ")
        print()

*****
*   *
*   *
*   *
*****

for row in range(5):
    for col in  range(5):
        if col==0 or col==5-1 or row==0 or row ==5-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


       *
     * * *

'''
for row in range(0, 5):
    for col in range (0, 6):
        if((row==0 and col==3) or (row==1 and(col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# *
# * *
# *   *
# *     *
# *       *
# * * * * * *            

# ---> list

# primary


# Number --> int, float complex
# string
# boolean
# set
# dictionary


# ? ---> List
# 1.)if the collection of elements are sorounded by square brackets
# to be list
#  ! eg:
# l1=[4,7,9,9.89,"hello",7+9j,[8,9,0]]

# Characteristics of list
# 1.) List have to be surrounded []
# 2.) It is mutable (the elements in the list are changable)
# 3.) Every elements inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous

# to access the elements in a list
1l=[1,4,1,7,89.9,7.5,"p","i"]
print(l1)

# -->Indexing
# In the collection datatypes like list, tuple, string, the elements will be alloted with predefines unique value called index value

# We have 2 types of indexing
# Positive indexing ---> starts with 0 from left hand side
# Negative indexing ---> starts with -1 from right hand side

# ---->Negative indexing
#lst1 = [1, 4, 1, 7, 89.7, 75, "p", "i"]
#print(lst1[-1])
#print(lst1[-5])


lst1 = [24,34,65,87,6,"akash","vijay","hima"]
print(lst1[-1])
print(lst1[-2])
print(lst1[-3])



# ? ---> slicing
lst11=[1,4,1,7,89.7,7.5,"p","i"]
lst1[start_index:end_index:step]
print(lst1[0:4])
print()


#print(1st1[-7:-1:2])
#! To insert ot add element inside list
# append()-> used to add elelement at last position of list
# 11 [9, 8, 0, 6]
# 11.append("car")
#  print(11)



















