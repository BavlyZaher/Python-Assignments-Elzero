import os
#1
print(os.getcwd())
os.chdir(r"C:\Users\pro\Desktop\Python")
print(os.getcwd())
n = 1
while n < 51:
    if  n == 25 :
        file = open(r"C:\Users\pro\Desktop\Python\special-text.txt","a")
    else :
         file = open(fr"C:\Users\pro\Desktop\Python\txt{n}.txt","a")
         file.write(f"Elzero Web School => {n}")
    n+=1
file = open("assign.py.txt")
print(os.path.basename(file.name))
print(n)

#2
a = open("txt1.txt","a")
a.write("\nAppended => Elzero Web School" * 50)

#3
a = open("txt1.txt")
print(f"Number Of Lines Is => {len(a.readlines())}")

a = open("txt1.txt")
w = 0
c = 0
for line in a:
    line.split()
    w+=len(line.split())
    "".join(line.split())
    c+=len("".join(line.split()))
print(f"Number Of Words Is => {w}")
print(f"Number Of Chars Is => {c}")

a = open("txt1.txt")
print(f"Number Of \"l\" Char Is => {a.read().count('l')}")

#4
num = 41
while num >= 41 and num <51 :
    os.remove(f"txt{num}.txt")
    num+=1