# def quick_sort(s):
#     if len(s) <= 1:
#         return s
#     b = s[0]
#     r, l, c = [], [], []
#     for i in range(len(s)):
#         if s[i] < b:
#             l.append(s[i])
#         if s[i] > b:
#             r.append(s[i])
#         if s[i] == b:
#             c.append(s[i])
#     return quick_sort(l) + c + quick_sort(r)


# a,b,c=int(input()),list(map(int,input().split())),0
# for i in range(a-1):
#     for j in range(a-1-i):
#         if b[j]>b[j+1]:
#             c+=1
#             b[j],b[j+1]=b[j+1],b[j]
# print(*b)
# print(c)

# def greet(name):
#     return ("Hello, " + name + ". Good morning!")
# a = greet(input())
# print(a)

# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# import numpy as np
# def find_difference(a, b):
#     return np.prod(a) - np.prod(b) if np.prod(a) > np.prod(b) else np.prod(b) - np.prod(a)
# print(find_difference(a,b))


# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
#
# def find_difference(a, b):
#     def mult(u):
#         q = 1
#         for s in u:
#             q *= s
#         return q
#
#     if mult(a) > mult(b):
#         return mult(a) - mult(b)
#     return mult(b) - mult(a)
#
# print(find_difference(a,b))

# def create_file_with_numbers(n):
#     with open(f'range_{n}.txt', 'a') as f:
#         for i in range(1, n + 1):
#             f.write(str(i) + '\n')


# import json
# p = 'manager_sales.json'
# with open(p, 'r') as f:
#     data = json.load(f)
# mx = 0
# dm = {}
# for e in data:
#     s = 0
#     for i in e['cars']:
#         s += int(i['price'])
#     if s > mx:
#         mx = s
#     dm[f"{e['manager']['first_name']} {e['manager']['last_name']}"] = s
#
# print(*sorted(dm.items(),key=lambda x:-x[1])[0])


# import json
# file = open('manager_sales.json', encoding='utf-8')
# data = json.load(file)
# print(*sorted([[row['manager']['first_name'], row['manager']['last_name'], sum([car['price'] for car in row['cars']])] for row in data], key=lambda x: x[2], reverse=True)[0])


import json

# import json
#
# file = open("group_people.json", "r", encoding="utf-8")
# jfile = json.load(file)
# idd_peop = {}
# pep = []
# nw = {}
# nuw = 0
# s = 0
# maxi = 0
# for i in jfile:
#     idd_peop.setdefault(i["id_group"], i["people"])
#     for j in idd_peop:
#         pep.append(idd_peop.get(j))
# for i in pep:
#     nuw = 0
#     for k in i:
#         if k["gender"] == "Female" and k["year"] >= 1977:
#             nuw += 1
#     s += 1
#     nw.setdefault(s, nuw)
#     for s in nw:
#         if nw.get(s) > maxi:
#             maxi = nw.get(s)
#             for d in nw:
#                 if maxi == nw.get(d):
#                     print(d, maxi)


# print([i for i in range(1,int(input())+1)])


# val = 65
# for i in range(1, int(input())+1):
#     for j in range(1, i+1):
#         ch = chr(val)
#         print(ch, end=" ")
#     val = val + 1
#     print()

# a = []
# for i in range(int(input())):
#     a.append((chr(65+i))*(i+1))
# print(a)

# def all_divs(n):
#     i = 1
#     r = []
#     while (i * i <= n):
#         if n % i == 0:
#             r.append(i)
#         k = n // i
#         if i != k:
#             r.append(k)
#         i += 1
#     return sorted(r)
# print(all_divs(int(input())))

# number = int(input())
# dividers = []
# for i in range(1,number+1):
#     if number % i == 0:
#         dividers.append(i)
# print(dividers)


# vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
# a = []
# for i in vector:
#     for j in i:
#         a.append(j)
#
# print(*a)

# nums = [1,2,3,4,5]
# a = [i**2 for i in nums]
# b = list(map(lambda i: i**3, nums))

# top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
# if 'Бригада' in top:
#     top.remove('Бригада')
#     top.append('Сверхъестественное')
# if 'Друзья' in top:
#     top.remove('Друзья')
#     top.insert(2,'Настоящий детектив')
# print(top)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(filter(lambda x: x % 2 == 0, numbers)))

# days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
# a = list(filter(lambda x: True if len(x) == 4 or x[0] == 'S' else False, days))
# a.sort()
# for i in a:
#     print(i)

# subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
#                  ('Physics', 93), ('History', 78), ('French', 78),
#                  ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
#
# for i in sorted(subject_marks, key=lambda i: (-i[1], i[0]), reverse=False):
#     print(*i)

# models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#           {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#           {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
#           {'make': 'Apple', 'model': 10, 'color': 'Silver'},
#           {'make': 'Oppo', 'model': 9, 'color': 'Red'},
#           {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
#           {'make': 'Honor', 'model': 3, 'color': 'Black'}]
# for i in sorted(models, key=lambda i: i['color']):
#     print(f"Производитель: {i['make']}, модель: {i['model']}, цвет: {i['color']}")


# class Cat:
#     name = ''
#     age = ''
#     color = ''
#
# a = Cat()
# a.name = 'Murzik'
# a.age = 3
# a.color = 'Black'
#
# b = Cat()
# b.name = 'Zhora'
# b.age = 2
# b.color = 'Brown'
#
# print(a.__dict__, b.__dict__, sep='\n')

# class Marks:
#     history = 30; math = 50; art = 70
#     def all(self, x, y, z):
#         self.history = x
#         self.math = y
#         self.art = z
# a = Marks()
# a.__setattr__('biology',100)
# a.all(40,60,80)
# print(a.__dict__)

# class Lion:
#     def roar(self):
#         print('Rrrrrrr!!!')
# simba = Lion()
# simba.roar()

# class Counter:
#
#     def increment(self):
#         self.count += 1
#
#     def display(self):
#         print(f"Текущее значение счетчика = {self.count}")
#
#     def reset(self):
#         self.count = 0
#
#     def start_from(self, start=0):
#         self.count = start

# from math import sqrt
# class Point():
#     def set_coordinates(self, x, y):
#         self.x = x
#         self.y = y
#     def get_distance(self, another):
#         if isinstance(another, Point):
#             return sqrt(((self.x - another.x)**2) + ((self.y - another.y)**2))
#         else:
#             print('Передана не точка')

# class Coordinates:
#     'Coordinates'
#     def __init__(self, x = 0, y = 0):
#         self.x = x
#         self.y = y
# a = Coordinates(10,15)
# print(a.x, a.y)

# 1. Пользователь вводит с клавиатуры числа, до тех пор,
# пока не введет число 0. На основе введенных
# данных нужно сформировать список,
# состоящий из квадратов введенных чисел.
# n = int(input())
# a = []
# while True:
#     if n == 0:
#         break
#     a.append(n)
#     n = int(input())
# print([i**2 for i in a])

# from math import sqrt
# class Point:
#     def set_coordinates(self, x, y):
#         self.x = x; self.y = y
#     def get_distance(self, another):
#         if isinstance(another, Point):
#             return sqrt(((self.x - another.x)**2) + ((self.y - another.y)**2))
#         else:
#             print('Передана не точка')

# class Laptop:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#         self.laptop_name = f'{brand} {model}'
# hp = Laptop('hp', '15-bw0xx', 57000)
# print(hp.laptop_name)

# class SoccerPlayer:
#     def __init__(self, name, surname, goals = 0, assists = 0):
#         self.name = name
#         self.surname = surname
#         self.goals = goals
#         self.assists = assists
#     def score(self, goals = 1):
#         self.goals += goals
#     def make_assist(self, assits = 1):
#         self.assists += assits
#     def statistics(self):
#         print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')

# class Zebra:
#     def __init__(self, c = 1):
#         self.c = c
#     def which_stripe(self):
#         self.c += 1
#         if self.c % 2 == 0:
#             print('Полоска белая')
#         else:
#             print('Полоска черная')

# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#     def full_name(self):
#         return f'{self.last_name} {self.first_name}'
#     def is_adult(self):
#         return True if self.age >= 18 else False
# p1 = Person('Jimi', 'Hendrix', 55)
# print(p1.full_name())
# print(p1.is_adult())

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def description(self):
#         return f'{self.name} is {self.age} years old'
#     def speak(self, roar):
#         self.roar = roar
#         return f'{self.name} says {self.roar}'

# class Stack:
#     def __init__(self):
#         self.values = []
#     def is_empty(self):
#         return False if self.values else True
#     def push(self, item):
#         self.values.append(item)
#     def pop(self):
#         return self.values.pop() if self.is_empty() is False else print('Empty Stack')
#     def peel(self):
#         if self.is_empty() is False:
#             return self.values[-1]
#         else:
#             print('Empty Stack')
#             return None
#     def size(self):
#         return len(self.values)

# class BankAccount:
#
#     def __init__(self, name, balance, passport):
#         self.__name = name
#         self.__balance = balance
#         self.__passport = passport
#
#     def print_public_data(self):
#         print(self.name, self.balance, self.passport)
#
#     def print_protected_data(self):
#         print(self._name, self._balance, self._passport)
#
#     def print_private_data(self):
#         print(self.__name, self.__balance, self.__passport)
#
# acc1 = BankAccount('Bob', 1000, 123456)
# acc1.print_private_data()

# class UserMail:
#
#     def __init__(self, login, email):
#         self.login = login
#         self.__email = email
#
#     def get_email(self):
#         return self.__email
#
#     def set_email(self, new_mail):
#         if new_mail.count("@") == 1 and new_mail.find("@") < new_mail.rfind("."):
#             self.__email = new_mail
#         else:
#             print("Ошибочная почта")
#
#     email = property(fget=get_email, fset=set_email)


# class BankAccount:
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#
#     def get_balance(self):
#         print('get balance')
#         return self.__balance
#
#     def set_balance(self, value):
#         print('set balance')
#         if not isinstance(value, (int,float)):
#             raise ValueError('balance should be a int or a float')
#         self.__balance = value
#
#     def delete_balance(self):
#         print('delete balance')
#         del self.__balance
#
#     my_balance = property()
#     my_balance = my_balance.getter(get_balance)
#     my_balance = my_balance.setter(set_balance)
#     my_balance = my_balance.deleter(delete_balance)


# class Money:
#     def __init__(self, dollars, cents):
#         self.total_cents = dollars * 100 + cents
#
#     @property
#     def dollars(self):
#         return self.total_cents // 100
#
#     @dollars.setter
#     def dollars(self, value):
#         if isinstance(value, int) and value >= 0:
#             self.total_cents = value * 100 + self.total_cents % 100
#         else:
#             print('Error dollars')
#
#     @property
#     def cents(self):
#         return self.total_cents % 100
#
#     @cents.setter
#     def cents(self, value):
#         if isinstance(value, int) and 0 < value < 100:
#             self.total_cents = (self.total_cents - self.total_cents % 100) + value
#         else:
#             print('Error cents')
#
#     def __str__(self):
#         return f'Ваше состояние составляет {self.dollars} долларов ' \
#                f'{self.cents} центов'

# class Rec:
#
#     def __init__(self, a, b):
#         self.__a = a; self.__b = b
#         self.__per = None
#
#     @property
#     def a(self):
#         return self.__a
#
#     @property
#     def b(self):
#         return self.__b
#
#     @a.setter
#     def a(self, value):
#         self.__a = value
#         self.__per = None
#
#     @b.setter
#     def b(self, value):
#         self.__b = value
#         self.__per = None
#
#     @property
#     def per(self):
#         if self.__per is None:
#             self.__per = (self.a + self.b) * 2
#         return self.__per
#
# a = Rec(10,4)
# print(a.per)

# class Robot:
#
#     population = 0
#
#     def __init__(self, name):
#         self.name = name
#         print(f'Робот {name} был создан')
#         Robot.population += 1
#
#     def destroy(self):
#         print(f'Робот {self.name} был уничтожен')
#         Robot.population -= 1
#
#     def say_hello(self):
#         print(f'Робот {self.name} приветствует тебя, особь человеческого рода')
#
#     @classmethod
#     def how_many(cls):
#         print(f"{cls.population}, вот сколько нас еще осталось")
#
# a = Robot('Robik')
# b = Robot('R2D2')
# c = Robot('Cluster')
# print(Robot.how_many())


# class Person:
#
#     def __init__(self, name, surname, gender = 'male'):
#         self.name = name; self.surname = surname
#         if gender == 'female':
#             self.gender == 'female'
#         elif gender == '' or gender == 'male':
#             self.gender == 'male'
#         else:
#             print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
#             self.gender = 'male'
#
#     def __str__(self):
#         if self.gender == 'male':
#             return f'Гражданин {self.surname} {self.name}'
#         if self.gender == 'female':
#             return f'Гражданка {self.surname} {self.name}'


# class Vector:
#
#     def __init__(self, *args):
#         self.values = [i for i in args if isinstance(i, int)]
#
#     def __str__(self):
#         if self.values:
#             return f"Вектор{tuple(sorted(self.values))}"
#         return 'Пустой вектор'

# def decor(fn):
#     def wrapper(*args, **kwargs):
#         print('You are doing this: ' + str(fn.__name__))
#         return fn(*args, **kwargs)
#     return wrapper
# 
# @decor
# def calc_sqrt(x):
#     return f'The result is {x**0.5}'
# 
# a = calc_sqrt(4)
# print(a)

# class BankAccount:
#
#     def __init__(self, name, balance):
#         self.name = name; self.balance = balance
#
#     def __add__(self, other):
#         if isinstance(other, BankAccount):
#             return self.balance + other.balance
#         if isinstance(other, (int, float)):
#             return self.balance + other
#         raise NotImplemented
#
#     def __mul__(self, other):
#         if isinstance(other, BankAccount):
#             return self.balance * other.balance
#         if isinstance(other, (int, float)):
#             return self.balance * other
#         if isinstance(other, str):
#             return self.name + other
#         raise NotImplemented
#
#     def __radd__(self, other):
#         return self + other
#
# a = BankAccount('Ivan', 900)

# class Vector:
#
#     def __init__(self, *agrs):
#         self.values = sorted(v for v in agrs if isinstance(v, int))
#
#     def __str__(self):
#         if self.values:
#             return f'Вектор{tuple(self.values)}'
#         return 'Пустой вектор'
#
#     def __add__(self, val):
#         if isinstance(val, int):
#             return Vector(*map(lambda x: x + val, self.values))
#         elif isinstance(val, Vector):
#             if len(self.values) == len(val.values):
#                 temp = map(lambda x: x[0] + x[1], zip(self.values, val.values))
#                 return Vector(*temp)
#             return print('Сложение векторов разной длины недопустимо')
#         return print(f'Вектор нельзя сложить с {val}')
#
#     def __mul__(self, val):
#         if isinstance(val, int):
#             return Vector(*map(lambda x: x * val, self.values))
#         elif isinstance(val, Vector):
#             if len(self.values) == len(val.values):
#                 temp = map(lambda x: x[0] * x[1], zip(self.values, val.values))
#                 return Vector(*temp)
#             return print('Умножение векторов разной длины недопустимо')
#         return print(f'Вектор нельзя умножать с {val}')


# class City:
#
#     def __init__(self, name):
#         if isinstance(name, str):
#             self.name = name.title()
#
#     def __str__(self):
#         return self.name
#
#     def __bool__(self):
#         return self.name[-1] not in ['a', 'e', 'i', 'o', 'u']

# class Quadrilateral:
#
#     def __init__(self, *args):
#         if len(args) == 1:
#             self.width = self.height = args[0]
#         else:
#             self.width = args[0]
#             self.height = args[1]
#
#     def __str__(self):
#         if not abs(self.width - self.height):
#             return f'Куб размером {self.width}х{self.height}'
#         return f'Прямоугольник размером {self.width}х{self.height}'
#
#     def __bool__(self):
#         return self.width == self.height

# class Vector1:
#
#     def __init__(self, dct):
#         self.dct = dct
#
#     def __repr__(self):
#         return str(self.dct)
#
#     def key_ex(self, key):
#         if not isinstance(key, (str, int, tuple)) or \
#                 key not in self.dct:
#             raise KeyError
#         return True
#
#     def __getitem__(self, item):
#         if self.key_ex(item):
#             return self.dct[item]
#
#     def __setitem__(self, key, value):
#         if self.key_ex(key):
#             self.dct[key] = value
#
#     def __delitem__(self, key):
#         if self.key_ex(key):
#             del self.dct[key]
#
#
# class Vector:
#
#     def __init__(self, *args):
#         self.values = list(args)
#
#     def __repr__(self):
#         return str(self.values)
#
#     def __getitem__(self, item):
#         len_s = len(self.values)
#         if isinstance(item, slice):
#             if item.stop not in range(-len_s, len_s):
#                 raise IndexError("Index out of range")
#             else:
#                 return self.values[item.start:item.stop:item.step]
#         elif isinstance(item, int):
#             if item in range(-len_s, len_s):
#                 return self.values[item]
#             raise IndexError("Index out of range")
#         raise SyntaxError("SyntaxError: invalid syntax")

# class NewInt(int):
#
#     def __init__(self, d):
#         self.d = d
#
#     def repeat(self, n=2):
#         self.n = n
#         self.answ = str()
#         for i in range(self.n):
#             self.answ = self.answ + str(self.d)
#         return int(self.answ)
#
#     def to_bin(self):
#         return int(bin(int(self.d))[2:])

# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError
#         return args[0].strip(self.__chars)

# or with the help of closure

# def StripChars(chars):
#     def stringStrip(string):
#         if not isinstance(string, str):
#             raise ValueError
#         return string.strip(chars)
#     return stringStrip
#
# s1 = StripChars('?:!.; ')
# print(s1('  ::hey there;;  '))


# def f(x):
#     return x * 2
# a = {}
# for i in range(int(input())):
#     n = int(input())
#     if n not in a:
#         a[n] = f(n)
#     print(a[n])
#
#


# import re
# s = 'M1g9d2C8q19M13b11h11g13r2u13V14Y19k5b11l19V17H4I3x14l10H6V1u15w16d4F17n15r4V6p11T2N1Z13f9x19f2n5H13'
# res = re.findall(r'([a-z]+)(\d{,2})', s, flags=re.IGNORECASE)
# a = []
# for i in res:
#     a.append([i][0][0] * int([i][0][1]))
# print(*a, sep='')


# from collections import Counter
# with open('dataset_3363_3.txt', 'r') as file:
#     s = file.read()
#     w = s.split()
#     wc = Counter(w).most_common()
#     print(wc)
#
# with open('dataset_3363_3.txt') as file:
#     s = file.read().lower().strip().split()
#     y, m = 0, ''
#     for i in s:
#         z = s.count(i)
#         if z > y:
#             y = z
#             m = i
#         elif z == y and i < m:
#             m = i
#     print(m, y)

# c, l = 0, []
# with open('dataset_3363_4.txt') as file:
#     for s in file:
#         s = s.strip().split(';')
#         for i in s[1::]:
#             c += int(i)
#         print(c/3)
#         s.append(c/3)
#         l.append(s)
#         c = 0
#
# m, p, r = 0, 0, 0
# for i in l:
#     m += int(i[1])
#     p += int(i[2])
#     r += int(i[3])
# print(m/len(l), p/len(l), r/len(l))

# from math import pi
# print(2 * pi * float(input()))

# import sys
# s = ''
# s2 = ''
# for i in range(1,len(sys.argv)):
#     s = s + sys.argv[i]+' '
# s2 = s
# print(s2,end=' ')

# kata codewars

# s = input()
# def bald(s):
#     n=s.count('/')
#     if n==0:
#         return [s.replace('/','-'),'Clean!']
#     elif n==1:
#         return [s.replace('/','-'),'Unicorn!']
#     elif n==2:
#         return [s.replace('/','-'),'Homer!']
#     elif 3<=n<=5:
#         return [s.replace('/','-'),'Careless!']
#     elif n>5:
#         return [s.replace('/','-'),'Hobo!']
#
# print(bald(s))

# kata

# import math
#
# n = int(input())
#
# def smallest(n):
#     a = 1
#     for i in range(1, n + 1):
#         a = int((a * i)/math.gcd(a, i))
#     return a
#
# print(smallest(n))

# kata

# items = list(input().split())
# a, b = int(input()), int(input())
# def inverse_slice(items, a, b):
#     return items[:a]+items[b:]
# print(inverse_slice(items, a, b))


# kata

# def repeat_str(repeat, string):
#     return int(repeat)*string
# print(repeat_str(5, 'hello'))

# kata
# def twice_as_old(dad_years_old, son_years_old):
#     return abs((son_years_old * 2) - dad_years_old)
# print(twice_as_old(29,0))

# a, b, c, d = map(int, input().split())
# print('',*range(c, d + 1), sep='\t')
# for i in range(a, b + 1):
#     print(i, *range(i * c, (i * d) + 1, i), sep='\t')


# kata


# a = input().upper()
#
# def plane_seat(a):
#     m = ''
#     if len(a) == 3:
#         m = a[0] + a[1]
#         if (int(m) in range(1, 21)) and (a[2] in 'ABC'):
#             return 'Front-Left'
#         elif (int(m) in range(1, 21)) and (a[2] in 'DEF'):
#             return 'Front-Middle'
#         elif (int(m) in range(1, 21)) and (a[2] in 'GHK'):
#             return 'Front-Right'
#         if (int(m) in range(20, 41)) and (a[2] in 'ABC'):
#             return 'Middle-Left'
#         elif (int(m) in range(20, 41)) and (a[2] in 'DEF'):
#             return 'Middle-Middle'
#         elif (int(m) in range(20, 41)) and (a[2] in 'GHK'):
#             return 'Middle-Right'
#         if (int(m) in range(40, 61)) and (a[2] in 'ABC'):
#             return 'Back-Left'
#         elif (int(m) in range(40, 61)) and (a[2] in 'DEF'):
#             return 'Back-Middle'
#         elif (int(m) in range(40, 61)) and (a[2] in 'GHK'):
#             return 'Back-Right'
#         elif int(m) > 60 or a[2] not in 'ABCDEFGHK':
#             return 'No Seat!!'
#     elif len(a) == 2:
#         if (int(a[0]) in range(1, 21)) and (a[1] in 'ABC'):
#             return 'Front-Left'
#         elif (int(a[0]) in range(1, 21)) and (a[1] in 'DEF'):
#             return 'Front-Middle'
#         elif (int(a[0]) in range(1, 21)) and (a[1] in 'GHK'):
#             return 'Front-Right'
#         if (int(a[0]) in range(20, 41)) and (a[1] in 'ABC'):
#             return 'Middle-Left'
#         elif (int(a[0]) in range(20, 41)) and (a[1] in 'DEF'):
#             return 'Middle-Middle'
#         elif (int(a[0]) in range(20, 41)) and (a[1] in 'GHK'):
#             return 'Middle-Right'
#         if (int(a[0]) in range(40, 61)) and (a[1] in 'ABC'):
#             return 'Back-Left'
#         elif (int(a[0]) in range(40, 61)) and (a[1] in 'DEF'):
#             return 'Back-Middle'
#         elif (int(a[0]) in range(40, 61)) and (a[1] in 'GHK'):
#             return 'Back-Right'
#         elif a[1] not in 'ABCDEFGHK':
#             return 'No Seat!!'
#
# print(plane_seat(a))

# s = input().lower()
# c = 0
# for i in s:
#     if i == 'g' or i == 'c':
#         c += 1
# r = (c/len(s))*100
# print(r)
#
# s = input().upper()
# print((s.count('G') + s.count('C'))/len(s) * 100)

# a = [int(i) for i in input().split()]
# if len(a) == 1:
#     print(a[0])
# else:
#     for i in range(0, len(a) - 1):
#         print(a[i - 1] + a[i + 1], end=' ')
#     print(a[len(a) - 2] + a[0])


# def merge_arrays(arr1, arr2):
#     return sorted(set(arr1+arr2))
# print(merge_arrays([1,1,1,2,3],[4,5,6]))


# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# def snail(snail_map):
#     return list(array[0])+snail(zip(*array[1:])[::-1])if array else []
# print(snail(array))


# import requests
# with open('dataset_3378_2.txt', 'r') as f:
#     url = f.read().strip()
#
# r = requests.get(url)
# c = 0
#
# for j in r.text.splitlines():
#     c += 1
#
# print(len(r.text.splitlines()))


# n = int(input())
# move = {'север': 0, 'юг': 0, 'восток': 0, 'запад': 0}
# for _ in range(n):
#     m = input().split()
#     if m[0] in move:
#         move[m[0]] += int(m[1])
# x = move['восток'] - move['запад']
# y = move['север'] - move['юг']
# print(x, y)

# human = {}
# h = 'John Doe California 34 self-employeed 375-10-15 15 17 19 21 23'
# h = h.split()
# human['firstName'] = h[0]
# human['lastName'] = h[1]
# human['currentCity'] = h[2]
# human['age'] = int(h[3])
# human['job'] = h[4]
# human['tel'] = h[5]
# human['jobDates'] = []
# for i in h[6:]:
#     human['jobDates'].append(int(i))
# print(human)

# d = {}
# def update_dictionary(d, key, value):
#     if (key in d.keys()):
#         d[key].append(value)
#     elif (key*2 in d.keys()):
#         d[key*2] += [value]
#     else:
#         d[key*2] = [value]

# import requests
# from bs4 import BeautifulSoup
#
# class HabrPythonNews:
#
#     def __init__(self):
#         self.url = 'https://habr.com/ru/hub/python/'
#         self.html = self.get_html()
#
#     def get_html(self):
#         try:
#             result = requests.get(self.url)
#             result.raise_for_status()
#             return result.text
#         except(requests.RequestException, ValueError):
#             print('Server error')
#             return False
#
#     def get_python_news(self):
#         soup = BeautifulSoup(self.html, 'html.parser')
#         news_list = soup.findAll('h2', class_='post__title')
#         return news_list
#
# if __name__ == "__main__":
#     news = HabrPythonNews()
#     print(news.get_python_news())

# n, m = '', []
# while True:
#     n = input()
#     if n == 'end':
#         break
#     m.append([int(i) for i in n.split()])
# li, lj = len(m), len(m[0])
# new = [[sum([m[i-1][j], m[(i+1)%li][j], m[i][j-1], m[i][(j+1)%lj]]) for j in range(lj)] for i in range(li)]
# for i in range(li):
#     for j in range(lj):
#         print(new[i][j], end=' ')
#     print()

# n, m = [int(i) for i in input().split()]
# a = [[int(j) for j in input().split() for i in range(n)]]
# x, y = 0, 0
# mx = a[0][0]
# for i in range(n):
#     for j in range(m):
#         if a[i][j] > mx:
#             mx = a[i][j]
#             x, y = i, j
# print(x, y)

