#уроки
#a=int(input("какой урок:"))
#start = 540 #9 часов, перевел в минуты
#work = 45 # урок
#n=a
#b=start+(work*a)
#while n!=1:
#    if n%2!=0:
#        b=b+15
#        n=n-1
#    elif n%2==0:
#        b=b+5
#        n=n-1
#        
#
#print(str(b//60) + " " + str(b%60))


#Число из промежутка

#x=int(input("целое число x:"))
#if x<100 or x>9999:
#    print ("Число должно быть в диапазоне от 100 до 9999.")
#else:
#    b=str(x)
#    if len(b)==4:
#     h=(int(b[0])+int(b[1])+int(b[2])+int(b[3]))
#     print("сумма цифр:",int(h))
#    elif len(b)==3:
#     g=(int(b[0])*int(b[1])*int(b[2]))
#    print ("произведение:",g)

#Бассейн Яши

#n=int(input("число n:"))
#m=int(input("число m:"))
#x=int(input("число x:"))
#y=int(input("число y:"))
#if n<m and n<x and n<y:
#    print ("наименьшее число:",n)
#elif m<n and m<x and m<y:
#    print ("наименьшее число:",m)
#elif x<n and x<m and x<y:
#      print ("наименьшее число:",x)
#elif y<x and y<m and y<n :
#    print ("наименьшее число:",y)


#калькулятор

#n=int(input("число 1:"))
#m=int(input("число 2:"))
#x=str(input("операция:"))
#if x== "/" :
#    if m == 0:
#        print ("ошибка")
#    else:
#        print ("ваше число:", (n/m))
#elif x == "+":
#    print ("ваше число:", (n+m))
#elif x == "-":
#    print ("ваше число:", (n-m))
#elif x == "*":
#    print ("ваше число:", (n*m))
#elif x == "mod":
#    if m == 0:
#        print ("ошибка")
#    else:
#        print ("ваше число:", (n%m))
#elif x == "pow":
#    print ("ваше число:", ((n**m)))
#elif x == "div":
#    print ("ваше число:", (n//m))

#передача "зодоровье'

#a=int(input("сколько можно минимум:"))
#b=int(input("сколько можно максимум:"))
#h=int(input("сколько сейчас:"))
#if a>b:
#    print ("неправильные цифры")
#elif a<=h<=b:
#    print ("нормально")
#elif h<a:
#    print ("ПРОСПИСЬ")
#elif h>b:
#    print ("спи чуть поменьше пожалуйста 😥")

#светофор

#a=int(input("сколько времени прошло:"))
#d=0
#while d<=a:
#    if d+3>a:
#        print ("зеленый")
#        break
#    else:
#        d=d+3
#    if d+2>a:
#        print ("красный")
#        break
#    else:
#        d=d+2

# пингвины

# a = "   _~_   "
# b = "  (o o)  "
# c = "  / V \  "
# d = " /( _ )\ "
# e = "  ^^ ^^  "
# f = int(input("Сколько пингвинов:"))

# if f > 9 or f < 1:
#     print("нужно число от 1 до 9")
# else:
#     a = a*f
#     b = b*f
#     c = c*f
#     d = d*f
#     e = e*f

#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(e)





# АА серединка


# a = str(input("Введите слово:"))
# countA = 0
# countLen = 0

# if a[0] != "a" and a[(len(a)-1)] != "a" and a[0] != "A" and a[(len(a)-1)] != "A":
#     while countLen < len(a):
#         if a[countLen] == "A" or a[countLen] == "a":
#             countA += 1
#             countLen += 1
#         else:
#             countLen += 1
#     if countA == 2:
#         print("+")
#     else:
#         print("-")
# else: 
#     print("-")



# Счастливый билет

# a = str(input("Введите номер билета:"))

# summ1 = int(a[0]) + int(a[1]) + int(a[2])
# summ2 = int(a[3]) + int(a[4]) + int(a[5])

# if len(a) < 6 or len(a) > 6:
#     print("Билет состоит из 6 цифр!!")
# else:
#     if summ1 == summ2:
#         print("Счастливый")
#     else:
#         print("обычный")






# Длинна отрезка

# import math
# ax, ay = input("Введите коорды точки A:").split()
# bx, by = input("Введите коорды точки B:").split()
# print(math.dist((float(ax), float(ay)), (float(bx), float(by))))




# Поездка на дачу

# import math
# a = input("Расстояние до дачи:")
# b = input("Расход бензина:")
# c = input("Цена литра бензина:")
# g = float(b) / 100
# f = g * float(a) * float(c) * 2
# e = math.modf(f)
# print("Поездка обойдётся в", int(e[1]), " рубля", math.ceil(e[0]*100), "коп")

#Запишите в виде логического выражения и на языке программирования следующие
#истинные высказывания:

# # (X нечетное) и (Y нечётное)
# (x%2==0) and (y%2==0)
# (x < 20 и y > 20) или (x > 20 и y < 20) 
# (x < 20 and y > 20) or (x > 20 and y < 20) 
# x = 0 или y = 0
# x == 0 or y == 0
# x < 0 и y < 0 и z < 0
# x < 0 and y < 0 and z < 0
# (x%5==0 и y%5!=0 и z%5!=0) или (x%5!=0 и y%5==0 и z%5!=0) или (x%5!=0 и y%5!=0 и z%5==0)
# (x%5==0 and y%5!=0 and z%5!=0) or (x%5!=0 and y%5==0 and z%5!=0) or (x%5!=0 and y%5!=0 and z%5==0)
# (x > 100 и y < 100 и z < 100) или (x < 100 и y > 100 и z < 100) или (x < 100 и y < 100 и z < 100) 
# (x > 100 and y < 100 and z < 100) or (x < 100 and y > 100 and z < 100) or (x < 100 and y < 100 and z < 100)

#максимум по выбору 
#a = input("Введите число 1:")
#b = input("Введите число 2:")
#c = input("Введите число 3:")
#d = input("Введите число 4:")
#
#if a > b and a > c and a > d:
#    print(a)
#if b > a and b > c and b > d:
#    print(b)
#if d > b and d > c and d > a:
#    print(d)
#if c > b and c > a and c > d:
#    print(c)

#математический перевод
#a) 
#x= int(input ())
#a = -1 / x**2 
#print (a)

#д)
#a=int(input())
#b=int(input())
#g=5.45*(a+2*b)/(2-a)
#print (g)

#e) не заработал :(
#from math import sqrt
#a=int(input())
#b=int(input())
#c=int(input())
#h=-b+sqrt(
#    b**2-4*a*c
#    )/2*a
#print (h) 

#ж)
#a=int(input())
#b=int(input())
#c=int(input()) 
#g=(-b+(1/a))/(2/c)
#print (g)

#арифметика 
#a=int(input("целое число 1:"))
#b=int(input("целое число 2:"))
#g=a+b
#h=a-b
#j=a/b
#print (int(g,h,j))

#малевия 

#import math 
#
#shape = input("Введите форму комнаты:")
#
#if shape != "прямоугольник" and shape != "круг" and shape != "треугольник":
#    print("Неправильная форма")
#elif shape == "прямоугольник":
#    a = float(input("Введите сторону A:"))
#    b = float(input("Введите сторону B:"))
#
#    print("Площаль комнаты:",a*b)
#elif shape == "круг":
#    a = float(input("Введите радиус:"))
#
#    print("площаль комнаты:", math.pi * a ** 2)
#elif shape == "треугольник":
#    a = float(input("Введите сторону A:"))
#    b = float(input("Введите сторону B:"))
#    c = float(input("Введите сторону C:"))
#    p = (a + b + c) / 2
#
#    print("площаль комнаты:", math.sqrt(p*(p-a)*(p-b)*(p-c)))

# с трубами не так все плохо !

#from math import *
#a=float(input("внешний радиус трубы:"))
#b=float(input("толщина стенки:"))
#g=float(input("длина:"))
#h=pi*a**2*g # внешний
#j=pi*(a-b)**2*g # внутренний
#n=h-j # материал
#k=round(n,2)
#print (k)