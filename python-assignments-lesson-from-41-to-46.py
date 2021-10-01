#1
num1 = int(input("Put Num1 Here => ").strip())
num2 = int(input("Put Num2 Here => ").strip())
operation = input("Put Operation Here \"+\" Or \"-\" Or \"*\" Or \"/\" Or \"%\" => ").strip()
if operation == "+" :
    print(num1+num2)
elif operation == "-" :
    print(num1-num2)
elif operation == "*" :
    print(num1*num2)
elif operation == "/" :
    print(num1/num2)
elif operation == "%" :
    print(num1%num2)
else:
    print("Wrong Operation")

#2
age = 16
print("App Is Suitable For You") if age > 16 else print("App Is Not Suitable For You")

#3
age = int(input("Put Age Here => "))
if age > 10 and age < 100:
    print(f"Your Age In Months Is {age*12:,} Months")
    print(f"Your Age In Weeks Is {age*12*4:,} Weeks")
    print(f"Your Age In Days Is {age*365:,} Days")
    print(f"Your Age In Hours Is {age*365*24:,} Hours")
    print(f"Your Age In Minutes Is {age*365*24*60:,} Minutes")
    print(f"Your Age In Seconds Is {age*365*24*60*60:,} Seconds")
else:
    print("Your Age Is Out Of Range")

#4
country = input("Input Your Country => ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30
if country in countries:
    print(f"Your Country Eligible For Discount And The Price After Discount Is ${price-discount}")
else:
    print(f"Your Country Not Eligible For Discount And The Price Is ${price}")