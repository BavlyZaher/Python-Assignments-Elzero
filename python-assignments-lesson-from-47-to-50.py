#1
num = int(input("Put Num Here => "))
list = []
while num > 0:
    num-=1
    if num == 6:
        continue
    if num == 0:
        break
    print(num)
    list.append(num)
else:
    print("Number 0 Is Not Larger Than 0")
print(f"{len(list)} Numbers Printed Successfully.")

#2
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
a = []
n = 0
friends.sort()
while friends[n] == friends[n].capitalize() : # Or while friends[n].istitle() :
    print(friends[n])
    n+=1
else:
    a = friends[n:]
print(f"Friends Printed And Ignored Names Count Is {len(a)}")
   
#3
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
while skills:
    print(skills.pop(0))

#4
my_friends =[]
n = 3
n1 = 1
while n >= 0:
    name = input("Please Enter Your Name  ").strip()
    if name.islower() :
        print(f"Friend {name.capitalize()} Added => 1st Letter Become Capital")
        print(f"Names Left in List Is {n}")
        my_friends.append(name.capitalize())
        n -= 1
        print(my_friends)
    elif name.isupper() :
        print("Invalid Name")
    else:
        my_friends.append(name.capitalize())
        print(f"Friend {name.capitalize()} Added")
        print(f"Names Left in List Is {n}")
        n -= 1
        print(my_friends)
while my_friends:
    print(f"#{n1} {my_friends.pop(0)}")
    n1 +=1