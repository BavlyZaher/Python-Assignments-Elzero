#1
a = "Bavly",
print(a)
print(type(a))

#2
friends = ("Osama", "Ahmed", "Sayed")
p = list(friends)
p[0] = "Elzero"
friends = tuple(p)
print(friends)
print(type(friends))
print(len(friends))

#3
nums = (1, 2, 3)
letters = ("A", "B", "C")
a = nums + letters
print(a)
print(len(a))

#4
my_tuple = (1, 2, 3, 4)
a,b,_,c = my_tuple
print(a)
print(b)
print(c)