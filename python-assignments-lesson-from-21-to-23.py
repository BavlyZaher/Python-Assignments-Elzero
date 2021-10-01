#1
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])
print(friends.pop(0))
print(friends[-1])
print(friends.pop(-1))

#2
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[::2])
print(friends[1::2])

#3
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[1:4])
print(friends[-2:])

#4
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends[-2] = "Elzero"
friends[-1] = "Elzero"
print(friends)

#5
friends = ["Osama", "Ahmed", "Sayed"]
friends.insert(0,"Nasser")
print(friends)
friends.insert(4,"Salem") # or friends.append("Salem")
print(friends)

#6
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
friends.pop(0) # ممكن استخدم remove عادي
friends.pop(0)
print(friends)
friends.pop(-1)
print(friends)

#7
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
All = friends + employees +school # ممكن استخدم	extend
print(All)

#8
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)

#9
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends))

#10
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[-1][0])
print(technologies[-1][-1])