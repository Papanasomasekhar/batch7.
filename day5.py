# ! -----> common funtions for list

#l1 = [6, 7, 8, 9, 0]
# print(len(l1))

# print(max(l1))
# print(min(l1))


# l1 = [6, 8, 9, "p", "u"]
# print(min(l1))
# print(max(l1))

# l1 = [6, 8, 9, 0, 8.89, -5, 0.78]
# print(min(l1)) # -5


# l1 = [6, 8, 9, 0, 8.89, -5, 0.78]
# index() --> to get index value ofspecific element
# print(l1.index(9))


# l1 = [6, 6, 6, 7, 8, 9, 0, 8.89, -5, 0.78]
# count() --> how many num of times an element is repeated
# print(l1.count(6))


#! some funtions which is specifically used for list

# To add element inside list
# ? insert(index_value, element) --> to add element at specific index position
# l1 = [6, 6, 6, 7, 8, 9, 0, 8.89, -5, 0.78]
# l1.insert(4, "cars")
# print(l1)

# ? To delete element from list
# l1 = [6, 6, 6, 7, 8, 9, 0, 8.89, -5, 0.78]
# pop() --> last element will be deleted
# l1.pop()
# print(l1)

# pop(index_value) --> used to deleted element at specific index
# l1.pop(4) # 4 is index value
# print(l1)


# *remove(element) --> used to deleted element directly
# l1.remove(8.89)
# print(l1)

#* clear() --> to complete delete all element in list
# l1.clear()
# print(l1)


# del -> to delete the list
#del l1 #or del(l1)
# print(l1)


# ? ----> join 2 lists


# l1 = [9, 0, 8]
# l2 = ["p", "o", "t", 34]
#*print(l1+l2)

# ! or

# * extend() --> to combine 2 lists
# l1.extend(l2)
# print(l1)

# ? -----> copy()
# l1 = [6, 7, 8, 9, 3]
# l2 = l1.copy()
# print(l2)
# print(l1)

# print(id(l1))
# print(id(l2))


# ! diff between shallow copy and deep copy
# * shallow copy
# import copy
# l1 = [8, 9, 0,[5, 6],[3, 2, 1]]
# l2 = copy.copy(l1)
# l1.append(890)
# print(l1)
# print(l2)                )



# * deep copy
# import copy
# l1 = [8, 9, 0,[5, 6],[3, 2, 1]]
# print(l1[-1][1]) --> to index nested list

# l2 = copy.deepcopy(l1)
# l1[-1].append('cars')
# print(l1)
# print(l2)


# ? sort --> arrange elements in list ascending or descending order

# l1 = [9,7,2,3,5,23,63,32]
# l1.sort(reverse=True)
# print(l1)

# l1 = ['z', 'i', 'o', 'p', '9']
# l1.sort()
# print(l1)


# ! ----> nested list
# l1 = [8, 9, [0, 8, 7], ["p", "o", "y"], [8, 't']]
# print(l1[-2][1]) # --> o

# print(l1[1:4])
# print(l1[1:-1])

# ? to delete "t" form l1
# l1[-1].remove('t')
# print(l1)

# ? combine these ["p", "o", "y"],[8, 't'] lists in l1 to ["p", "o", 'y', 8, 't']

# l1[-2].extend(l1[-1])
# l1.pop(-1)
# print(l1)


# ! ----> Tuple

# 1.) tuple have to be surrounded by ()
# 2.) The element inside tuple are not changable
# 3.) The element inside tuple are indexed
# 4.) The element will excuted in order
# 5.) It is heterogenous
# 6.) It allow duplicate element

# Iterate based on index value

# l1=[9,8,0,6,5,7,36,54,55,6,43,5,66]
# for i in range(0,len(l1)):
#     print(l1[i])



# ! ----> Strings
# s1 = '0'
# print(type(s1))

# s1 = "u"
# print()

# ----> common function



# len(), min(), max(), index(), count()
# s1 = "hello world"
# print(len(s1))
# print(max(s1))
# print(min(s1))


#ord()--->used to find the ASCII value of a character
# s1='u'
# print(ord(s1))

#strip()--->to eliminate the space in beginning and end of string
# s1=" where are you"
# print(s1.lstrip())
# print(s1.rstrip())
# print(s1.strip())



# --> strip()
# --> to eliminating the space in beginnning and end of string
# M:-1
# --> to eliminate left space

'''
                                                                                                                                                                                                                                                                   
s1 = "   where are you.?"
print(s1.lstrip())

# M:-2
# --> to eliminate right space

s1 = "where are you.?  "
print(s1.rstrip())

# M:-3
# --> to eliminate right and left space

# s1 = "   where are you.?    "
# print(s1.strip())


# ---> split()-->
# --> to split the words in string based on a character
s1= "where are you.?"
print(s1.split("r"))
print(s1.split())


# replace() --> to replace a specific char in the string

s1= "where are you.?"
print(s1.replace('r','&&'))


# swapace() --> to convert capital to small and small to capital at a time

s1 = "HEY there"
print(s1.swapcase())

                         
# title function()
# s1 = "HEY there"
# print(s1.title())

# capitalize() 
# s1 = "HEY there"
# print(s1.capitalize())

# join the strings
s1 = "hello"
s2 = "world"
#  s1= 'hey dont sleep there'
# i = 7

# join the strings

s1 = "hello"
s2 = "world"
print(s1+s2)


# * title() --> to write the string in format of title
s1 = 'never giveup'
print(s1.title())


# * capitalize() --> 1st character of string will be converted to capital
s1 = 'never giveup'
print(s1.capitalize())


# * Join the strings
#s1 = " hello"
#s2 = 'world'
#print(s1+s2)



s1 = how are you
i am fine
hey there



# splitlines() --> used to split the string based on lines
print(s1.splitline())

# * find() --> to find the index based on a character          
#s1 = "hello world"
#print(s1.find('z'))
#print(s1.index('z'))


# * join() -->
l1 = ["hey" ,"there"]
print(" ".join(l1))
print(" $ ".join(l1))


s1 = "welcome to all"
print(s1.endswith('l')) ---> we get either true or false
print(s1.startswith('w'))


s1 = "67"
print(type(s1))
print(s1.isdigit())

'''

# * print the string in reverse manner
s1 = "Welcome to all"
print(s1[::-1])




















