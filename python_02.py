number = 10 # 10은 리터럴이다? 그래서 동일한 주소값이 나온다
print(type(number))

print(id(10))   #id() 주소값
print(id(number))
number += 1
print(id(number))
number -= 1
print(id(number))

print(type("test"))
print(type([]))
print(type(()))
print(type({}))

print(type([1,2,3,4]))
print(type((1,2,3,4)))
print(type({"id": 1, "name": "김준일"}))

list1 = [1, 2, 3, 4]
tp = (5, 6, 7, 8)
dict1 = {"id": 1, "name": "김준일"}

print(list1[0])
print(tp[0])
print(dict1["id"])

list1.append(5)
print(list1)
print(tp.index(7))
list2 = list(tp)
print(list2)
print(dict1.keys())
print(dict1.values())
print(list(dict1.items())[0])