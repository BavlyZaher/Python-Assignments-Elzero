#1
name = "Bavly"
age = "19"
country = "Egypt"
print(f"Hello \'{name}\', How You Doing \ \"\"\" Your Age Is \"{age}\"\" + And Your Country Is: {country}")

#2 By Using Triple Quotes Or Escape New line
print(f"""Hello \'{name}\', How You Doing \ 
\"\"\" Your Age Is \"{age}\"\" +
And Your Country Is: {country}""")
print(f"Hello \'{name}\', How You Doing \ \n\"\"\" Your Age Is \"{age}\"\" + \nAnd Your Country Is: {country}")

#3
name1 = 'Elzero'
print(f"Second Letter Is \"{name1[1]}\"")
print(f"Third Letter Is \"{name1[2]}\"")
print(f"Last Letter Is \"{name1[-1]}\"")

#4
print(f"\"{name1[1:4]}\"")
print(f"\"{name1[::2]}\"") # هيبدأ من الأول للأخر وهيمشي حرف ويسيب حرف
print(f"\"{name1[-2::-2]}\"") # هيبدأ من الأخر من الحرف الي قبل الاخير للأول وهيمشي حرف ويسيب حرف

#5
name2 = "#@#@Elzero#@#@"
print(name2.strip("#@"))

#6
num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"
print(f"{num1.zfill(4)}\n{num2.zfill(4)}\n{num3.zfill(4)}\n{num4.zfill(4)}\n{num5.zfill(4)}")

#7
name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20,"@"))
print(name_two.rjust(20,"@"))

#8
name_one1 = "OSamA"
name_two2 = "osaMA"
print(name_one1.swapcase())
print(name_two2.swapcase())

#9
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))

#10 By Using 2 Methods
name3 = "Elzero"
print(name3.index("z")) # if the letter wasn't found there would be Error
print(name3.find("z")) # if the letter wasn't found there would be -1

#11
msg1 = "I <3 Python And Although <3 Elzero Web School"
print(msg1.replace("<3","Love",1))

#12
print(msg1.replace("<3","Love"))

#13 By Using 3 Methods
name0 = "Bavly"
age0 = 19
country0 = "Egypt"
print(f"My Name Is {name0}, And My Age Is {age0}, And My Country Is {country0}")
print("My Name Is {:s}, And My Age Is {:d}, And My Country Is {:s}".format(name0,age0,country0))
print("My Name Is %s, And My Age Is %d, And My Country Is %s" % (name0,age0,country0))