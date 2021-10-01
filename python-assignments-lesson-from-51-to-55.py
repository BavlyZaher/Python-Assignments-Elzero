#1
my_nums = [15, 81, 5, 17, 20, 21, 13]
n = 1
my_nums.sort(reverse=True)
for num in my_nums:
    if num % 5 == 0:
        print(f"\"{n} => {num}\"")
        n+=1
print("All Numbers Printed")

#2
for i in range(1,21):
    if i == 6 or i == 8 or i == 12:
        continue
    print(str(i).zfill(2))
print("All Numbers Printed")

#3
my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}
a = 0
for name,rank in my_ranks.items():
    Rank = rank
    if rank == "A" : rank = 100
    if rank == "B" : rank = 80
    if rank == "C" : rank = 40
    print(f"My Rank in {name} Is {Rank} And This Equal {rank} Points")
    a+=rank
print(f"Total Points Is {a}") # طريقة رقم 1 لحساب المجموع

#4
students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}
list = []
for name,rank in students.items():
    print("\"------------------------------\"")
    print(f"\"-- Student Name => {name}\"")
    print("\"------------------------------\"")
    for name2,rank2 in rank.items():
        if rank2 == "A" : rank2 = 100
        if rank2 == "B" : rank2 = 80
        if rank2 == "C" : rank2 = 40
        if rank2 == "D" : rank2 = 20
        print(f"\"- {name2} => {rank2} Points\"")
        list.append(rank2)
    print(f"\"Total Points For {name} Is {sum(list)}\"") # طريقة 2 لحساب المجموع بدالة sum
    list.clear()    