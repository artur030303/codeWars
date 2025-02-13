# new_set= {1,2,3,4,5,6,2,3,4,5,6}
# print(new_set)

# another_set = {1,2,3,'a','c',0.34}
# print(another_set)

# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}

# print(set1 | set2) # объединение
# print(set1 & set2) # пересечение
# print(set1 - set2) # разность
# print(set1 ^ set2)  # симметрическая разность


# set1.add(10)
# print(set1)

# set1.remove(4)
# print(set1)

# set1.remove('a')
# print(set1)

# programmers = {'ivanov','petrov','sidorov'}
# managers = {'ivanov','moxov','goroxov'}

# all_employees = programmers | managers
# print(all_employees)

# who_programmers_and_menegers = programmers & managers
# print(who_programmers_and_menegers)

# programmers_who_not_menegers = programmers - managers
# print(programmers_who_not_menegers)


# d = {}
# print(type(d))

# d1 = {'a': 1, 'b': 2}

# d2 = dict(a='1', b = '2')

# print(d2)

# d3 = dict.fromkeys(['a','b',1, (1,2)]) # создание словари без значений
# print(d3)

# d4 = dict.fromkeys(['a','b','c',('a','b')], 333)
# print(d4)

# создание словаря при помощи генератора словарей (dict comprehension, по аналогии со списками) :

# d5 = {a: a ** 2 for a in range(7)}
# print(d5)

# d6 = {b: b + 1 for b in range(10)}
# print(d6)

d= dict(a=1,b=2,c=3,d=13)
# print(d)

# print(d['a'])

# d[1]=15
# print(d)
# d['c']= 100
# print(d)

# b= d.get('b')
# f = d.get('f')
# print(b)
# print(f)


# d.update({'c': 1000})
# print(d)
# print(len(d))

# keys = d.keys()
# values = d.values()
# items = d.items()
# print(keys)
# print(values)
# print(items)

for key in d.keys():
    print(key,d[key])