# myDict = {
#     "name": "Dias",
#     "age": 24,
#     "university": "KazNU",
#     "mariage": False
# }
# myDict.clear() #Очищает словарь
# print(myDict)
#
# myTuple = ("name", "age", "university")
# myValues = 0
# myDict = dict.fromkeys(myTuple, myValues) #Создает словарь с ключами из myTuple
# print(myDict) #А значения берет из myValues
#
# print(myDict.get("name"))
# print(myDict["name"]) #Нет никакой разницы от get
#
# print(myDict.items()) #Возвращает все что лежит в словаре в виде листа внутри которого кортежи
#
# myList = list(myDict.items()) #items можно конвертировать в лист
# print(myList) #А потом достать конкретную пару
#
# myList = list(myDict) #Если конвертировать в лист, вы получите только ключи
# print(myList)
#
# print(myDict.keys()) #Возвращает нам все ключи в виде листа
# print(myDict.values()) #Возвращает нам все значения в виде листа
#
# myDict.pop("mariage") #Удаляет из словаря пару по ключу, который вы укажете в скобках
# print(myDict)
#
# myDict.popitem() #Удаляет последнюю пару внутри словаря
# print(myDict)
#
# print(myDict.setdefault("name")) #Если данный ключ уже есть, выводит его значение
# myDict.setdefault("nation") #Если данного ключа нет, то добавляет его со значением None
# print(myDict)
#
# myDict.update({"nation": "kazakh"}) #Если такой уже есть, то обновляет. Если нет, то добавляет
# print(myDict)
from itertools import count

# myDict = {
#     "postId": 1,
#     "id": 1,
#     "name": "id labore ex et quam laborum",
#     "email": "Eliseo@gardner.biz",
#     "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus"
# }
#
# # 1) Поменять местами первый и последний элементы
# firstElem = myList[0]
# lastElem = myList[-1]
# myList[0] = lastElem
# myList[-1] = firstElem
# print(myList)
#
# # 2) Найти цифру 2 в листе myList. Если она есть, вывести на экран "yes", если нет, то "No"
# if myList.count(2) == 0:
#     print("No")
# else:
#     print("Yes")
#
# if 2 in myList:
#     print("yes")
# else:
#     print("no")
#
# # 4) Удалить первые два элемента из листа
# myList.pop(0)
# myList.pop(0)
# print(myList)
#
# # 5) Найти, есть ли отрицательные элементы в листе
# myList.sort()
# if myList[0] < 0:
#     print("Yes")
# else:
#     print("No")
#
# # 6) Найти длину листа
# print(len(myList))
#
# myDict = {
#     "postId": 1,
#     "id": 1,
#     "name": "id labore ex et quam laborum",
#     "email": "Eliseo@gardner.biz",
#     "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus"
# }
#
# # 1) Вывести на экран "name"
# print(myDict["name"])
#
# # 2) Вывести длину значения "email"
# print(len(myDict["email"]))
#
# # 3) Вывести все ключи
# print(myDict.keys())
#
# # 4) Вывести все значения
# print(myDict.values())
#
# # 5) Вывести длину значения под ключом "body"
# print(len(myDict["body"]))
#
# # 6) Заменить пару "email" на "justcode@gmail.com" или на любую другую
# myDict.update({"email": "justcode@gmail.com"})
# print(myDict)
#
# # 7) Добавить пару дата и ее значение
# myDict.update({"date": "14.05.2022"})
# print(myDict)
#
# # 8) Увеличить значение id на +1
# myDict["id"] = myDict["id"] + 1
# myDict.update({"id": myDict["id"] + 1})
# print(myDict)
#
# # 9) Удалить пару "postId"
# myDict.pop("postId")
# print(myDict)
#
# myList = [5, 6, 1, 7, 9]
# for i in range(0, len(myList)):
#     myList[i] = myList[i] + 1
# print(myList)
#
# for i in myList:  # С помощью этого цикла, нельзя никак изменить лист
#     print(i + 1)
# print(myList)

dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
dictionary_1.update(dictionary_2)
print(dictionary_1)

dictionary = {i: i ** 3 for i in range(1, 11)}
print(dictionary)

keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']
dictionary_3 = dict(zip(keys, values))
print(dictionary_3)
