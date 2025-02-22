#Все пятизначные и кратность

a = 0
for i in range (10000, 100000):
   if i%133==125 and i%134==111:
        a += 1
   

#таблица умножения

 a=int(input("ввдите число от 1 до 9:"))
 if a>9:
    print("найдите другой калькулятор, по лучше!")
 elif 1<=a<=9:
    for i in range(1, 11):
     print ("{}*{}={}".format(a,i,a*i))

#Цветы

#a=(input("цвет цветов:"))
#b=(input("название цветов:"))
#if a.find("синие") or a.find("белые") and b.find("розы"):
#        print ("Ане понравятся эти цветы")
#else:
#        print ("no")

#любители чая

#a=int(input("входные данные 1:"))
#g=(a//2)*a//2
#if a%2==0 and 2<=a<=100:
#        print("выходные данные:",g)
#else:
#        print("некорректные данные (͡๏̯͡๏)")

#улица

a=int(input("вход 1:"))
b=int(input("ввод b:"))
if a<b and a>0 and b>0:
        if b%2==0:
                print("вывод:",abs(b-a)//2)
        elif b%2==1:
                print("вывод:",abs(b-a)//2)
elif a>b and a>0 and b>0:
        if a%2==0:
                print("вывод:",abs(a-b)//2)
        elif a%2==1:
                print("вывод:",abs(a-b)//2)
elif a>b*10**9 or b>a*10**9:
        print ("слишком больше число")

#шаттл до рутнока

#a=int(input("вход 1:"))
#if a%2==0:
#        print (a//2)
#elif a%2==1:
#        print ((a//2)+1)

#цикл for

#a=int(input("вводные данные 1:"))
#b=int(input("вводные данные 2:"))
#g,h=0,0
#for n in range(a,b+1):
#    if n%3==0:
#        g+=1
#        h+=n
#        print  (h/g)
#

#кино

#n = int(input("Boys:"))
#m = int(input("Girls:"))
#
#result = " "
#
#for i in range(1, n + m + 1):
#    if n == m:
#        if result[i-1] == "G":
#            result += "B"
#        else:
#            result += "G"    
#    elif n > m:
#        if n - m == 1:
#            if result[i-1] == "B":
#                result += "G"
#            else:
#                result += "B" 
#        else:
#            if i == 1:
#                result += " "
#            if ((result[i-1] != "B" and result[i-1] != " ") or result[i] != "B") :
#                result += "B"
#            else:
#                result += "G"   
#    elif m > n:
#        if n - m == 1:
#            if result[i-1] == "B":
#                result += "G"
#            else:
#                result += "B" 
#        else:
#            if i == 1:
#                result += " "
#            if (result[i-1] != "G" and result[i-1] != " ") or result[i] != "G" :
#                result += "G"
#            else:
#                result += "B"   
#      
#
#
#print(result)
#
#
#if (n==m and (n%2 != 0 and m%2 != 0)) or ((result[len(result)-1] != result[len(result)-2]) and result.count("B") == n and result.count("G") == m):
#    print(result)
#else:
#    print("NO SOLUTION")