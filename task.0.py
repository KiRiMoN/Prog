import random
top_1=[]
top_2=[]
k=0
l=0
for i in range(30):
    top_1.append(random.randint(-100,100))
print(top_1)
for i in range(30):
    if top_1[i]==max(top_1):
        k=i
print("Максимальний елемент:",max(top_1), "Індекс:", k)
for i in range(30):
    if (top_1[i]%2)!=0:
        top_2.append(top_1[i])
        l=1
if l==0:
    print("Немає відьємних чисел")
print("Список відьємних чисел:\n",sorted(top_2,reverse=True))

