#Given a list, Write one line of Python that takes this list a and makes a 
#new list that has only the even elements of this list in it.

#part 1
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b=[]
for i in range(0,len(a)):
    if a[i]%2 == 0:
        b.append(a[i])

print b


#part 2 - using list comprehension to accomplish the same thing as above
d = [a[i] for i in range (0,len(a)) if a[i]%2 == 0 ]
print d
