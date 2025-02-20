# Initilze an empty tuple
mytuple = ()

# Checking whether a variable is a tuple or not
print(type(mytuple))

mytuple = (1,2,3,4)
mytuple1 = (10.2,10.4,10.16,20.8)
mytuple2 = ("viren", "shlok", "Nair", "Tyagi")
mytuple3 = ("shivansh", "yuvika", 1, 11.6)

# tuple allows duplicacy
mytuple4 = (1,2,3,3,4,4)

# printing a tuple
for i in mytuple4:
    print(i)

# tuple is a ordered data set 

# mytuple[0]=50  # TypeError: 'tuple' object does not support item assignment

# print(mytuple[1:4])

a = [1,2,3,4,5]
print(a[-1:3:1])

# Assignment not allowed in tuple

print(mytuple * 3)

mytuple = list(mytuple)
print(mytuple)
print


print(mytuple)

