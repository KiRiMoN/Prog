import re
a = input()
m1 = []
m2 = []
n = re.findall(r'\d+', a)
n = [int(i) for i in n]
for i in range(len(a)) :
    if a[i].isdigit() == True:
        m1.append(int(a[i]))
a = re.sub("[0-9]", "", a)
print("Рядок без цифр:\n", a, sep='')
print("Масив цифр:\n", m1, sep='')
a = ' '.join(map(lambda s: s[:-1]+s[-1].upper(), a.title().split()))
print("Перша і остання буква велика:\n", a, sep='')
max_num = max(n)
index_of_n = n.index(max_num)
print("Максимальне значення:", max_num)
for i in range(len(n)):
    if i != index_of_n:
        t = n[i] ** i
        m2.insert(i, t)
print("Масив чисел в степені індекса:\n", m2)
