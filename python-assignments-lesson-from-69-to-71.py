#1
values = (0, 1, 2)

if any(values): # بيتأكد ان لو أي قيمة من قيم المجموعة صحيحة

  my_var = 0 # هيعمل متغير قيمته صفر

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var] 

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]): # بيتأكد ان كل القيم من الليست صحيحة لغاية العنصر الرابع او السادس او الليست كله

  print("Good") # لو تمت احد العمليات هيطبع Good

else:

  print("Bad") # لو متمتش احد العمليات هيطبع Bad
#Good

#2
v = 40

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820
# ناتج دالة pow = 0 لأنه ناتج باقي القسمة
# ومجموع الليست = 780 = 40 توافيق 2

#3
n = 20

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

  print("Good")


# Output => Good

#4
def my_all(things):
  a = []
  for thing in things:
    if bool(thing) == True :
      a.append(True)
    else:
      a.append(False)
  if False in a :
    return(False)
  else:
    return(True)
print(my_all([1, 2, 3])) # True
print(my_all([1, 2, 3, []])) # False

def my_any(things):
  a = []
  for thing in things:
    if bool(thing) == True :
      a.append(True)
    else:
      a.append(False)
  if True in a :
    return(True)
  else:
    return(False)
print(my_any([0, 1, [], False])) # True
print(my_any([(), 0, False])) # False

def my_min(things):
  a = []
  for thing in things:
    a.append(thing)
    a.sort()
  return(a[0])
print(my_min([10, 100, -20, -100, 50])) # -100
print(my_min((10, 100, -20, -100, 50))) # -100

def my_max(things):
  a = []
  for thing in things:
    a.append(thing)
    a.sort()
  return(a[-1])
print(my_max([10, 100, -20, -100, 50, 700])) # 700
print(my_max((10, 100, -20, -100, 50, 700))) # 700