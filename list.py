import random

mylist = []
for _ in range(0, random.randint(5, 20)):
    mylist.append(random.randint(-100, 100))
print(mylist)

# 3) Отсортировать лист по убыванию
mylist.sort()
print(mylist)
mylist.reverse()
print(mylist)
# 7) Добавить в конец листа элементы 5, 55
mylist.append(5)
mylist.append(55)
print(mylist)
# 8) Вывести на экран, первые 3 элемента листа
print(mylist[0:3])
# 9) Удалить последний элемент листа, если его длина нечетная
print(len(mylist))
for i in range(len(mylist)):
    if i % 2 == 0:
        mylist.pop()
        print(mylist)
        break
# 10) Вывести элемент, который находится по середине листа (Если такого нету, то 0)
a = len(mylist)
if a / 2 == 0:
    print("0")
else:
    print(a / 2)

