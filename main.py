import random

# HomeTask 1
# lst=[]
# for i in range(10):
#     n=random.randrange(0,20,2)
#     lst.append(n)
# print(lst)

# HomeTask 2
# cnt=0
# for i in range(100):
#     n=random.random()
#     if n>=0.3 and n<=0.7:
#         cnt+=1
# print(cnt)

#HomeTask 3
# students = ['Islom', 'JONIK', 'BOSS', 'JOJO', 'JOKI', 'ali', 'yusuf', 'yosin', 'yoska']
# cnt = random.sample(students, 3)
# print(cnt)

#HomeTask 4
# lst = ["apple","banana","orange","grape","lemon"]
# random.shuffle(lst)
# print(lst)
# random.shuffle(lst)
# print(lst)
# random.shuffle(lst)
# print(lst)

#HomeTask 5
# lst=[]
# lst2=[]
# for i in range(10):
#     n=random.randint(1,10)
#     lst.append(n)
# random.shuffle(lst)
# lst2.append(lst[0])
# lst2.append(lst[1])
# lst2.append(lst[2])
# print(lst2)

# n = random.sample(range(1, 100), 7)  
# n.sort(reverse=True)
# print(n)

#HomeTask 7
# lst=[]
# for i in range(10):
#     n=random.randint(1,5)
#     lst.append(n)
# grades = 0
# for i in lst:
#     grades+=i
# print("grade:",lst)
# print("average:",grades/len(lst))

#HomeTask 8
# lst=[]
# for i in range(20):
#     n=random.randint(1,30)
#     lst.append(n)
# lst2=random.sample(lst,5)
# print("chosen:",lst2)
# print("sum",sum(lst2))

#HomeTask 9
lst = ["red","green","blue"]
red=0
green=0
blue=0
for i in range(1000):
    rand = random.choices(lst,[5,3,2])
    if rand==["red"]:
        red+=1
    if rand==["green"]:
        green+=1
    if rand==["blue"]:
        blue+=1
print("red:",red)
print("green:",green)
print("blue:",blue)