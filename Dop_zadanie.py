import random
from operator import truediv

def kluch ():
    numbers = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    x_num = random.choice (numbers)
    return x_num
kluch_ = kluch()
print(" Ключ -",kluch_)
numbers = list(range(1, kluch_))
#print(numbers)

parol = []
for i in numbers:
    for j in numbers:
        if i != j and kluch_ % (i + j) == 0:
            parol.append((i, j))



for item in parol[:]:
    if item[0] > item[1]:
        parol.remove(item)

print(* parol)
