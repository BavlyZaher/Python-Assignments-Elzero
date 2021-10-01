#1
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = set(my_list)
unique_list = list(unique_list)
print(unique_list)
print(type(unique_list))
unique_list.pop(-1)
print(unique_list)

#2
nums = {1, 2, 3}
letters = {"A", "B", "C"}
print(nums | letters) # First Method
print(nums.union(letters))
nums.update(letters)
print(nums)


#3
my_set = {1, 2, 3}
letters = {"A", "B", "C"}
print(my_set)
my_set.clear()
print(my_set)
my_set.update("A","B") # ممكن استخدم add بس هي بتقبل عنصر واحد فقط في كل مرة
print(my_set)
my_set.discard("C")

#4
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))

#5
Dictionary = { "HTML" : "90%",
"CSS" : "80%",
"Python" : "30%",
}
Dictionary.update({"AI":"20%"}) # Or Dictionary["AI"] = "20%"
a = list(Dictionary) # حولتها لليست علشان اجيب المفتاح لوحده
print(f"{a[0]} Progress Is {Dictionary['HTML']}")
print(f"{a[1]} Progress Is {Dictionary['CSS']}")
print(f"{a[2]} Progress Is {Dictionary.get('Python')}")
print(f"{a[-1]} Progress Is {Dictionary.get('AI')}")

