#1
def calculate(n1,n2,operation="Unknown"):
    if operation == "Unknown" or operation.strip() == "+" or operation.capitalize().strip() == "Add" or operation.capitalize().strip() == "A":
        return(n1+n2)
    elif operation.strip() == "-" or operation.capitalize().strip() == "Subtract" or operation.capitalize().strip() == "S":
        return(n1-n2)
    elif operation.strip() == "*" or operation.capitalize().strip() == "Multiply" or operation.capitalize().strip() == "M":
        return(n1*n2)
    else :
        return("Wrong Operation")
print(calculate(10, 20)) # 30
print(calculate(10, 20, "+")) # 30
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "a")) # 30
print(calculate(10, 20, "A")) # 30
print(calculate(10, 20, "-")) # -10
print(calculate(10, 20, "subTRACT")) # -10
print(calculate(10, 20, "S")) # -10
print(calculate(10, 20, "*")) # 200
print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m")) # 200

#2
def addition(*nums):
    a=0
    for num in nums :
        if num == 10 :
            continue
        if num == 5 :
            num = -num
        a+=num
    return(a)
print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160

#3
def show_skills(name,*skills):
    if len(skills) == 0 :
        print(f"Hello {name} You Have No Skills To Show")
    else:
        print(f"Hello {name} Your Skills Is")
        for skill in skills :
            print(f"\"- {skill}\"")
show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills("Ahmed")

#4
def say_hello(name = "Unknown" , age = "Unknown" , country = "Unknown"):
    return(f"Hello {name} Your Age Is {age} And You Live In {country}")
print(say_hello("Osama", 38, "Egypt"))
print(say_hello())
