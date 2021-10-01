#1
print(type(15)) #Intger
print(type(15.15)) #Float
print(type(15+10j)) #Complex
print(type(15+10J)) #Complex
print(type(complex(15,10))) #Complex

#2
num = 1+2j
print(f"Imaginary Part {num.imag}")
print(f"Real Part {num.real}")

#3 By Three Methods
num1 = 10
print(f"{num1:.10f}") 
print("{:.10f}".format(num1))
print("%.10f" % (num1))

#4
num2 = 159.650
print(int(num2))
print(type(int(num2)))

#5
print(100 - 115)
print(50 * 30)
print(21 % 4)
print(110 / 11)
print(97 // 20)