# a = 0
# while a<=10:
#     print(a)10
#     a += 1
# nota = int(input("digite a nota"))
# while nota > 10:
#     nota = int(input("digite a nota correta"))
a = int(input('digit a primeiro nota: '))
while a > 10 :
    a = int(input('voce digit valor da 1º nota invalid digit valor correct  : '))
b = int(input('digit a segunda   nota:: '))
while b > 10 :
    b = int(input('voce digit um da 2º nota invalid digit valor correct  : '))
c = int(input('digit a terceira  nota:: '))
while c > 10 :
    c = int(input('voce digit valor da 3º nota invalid digit valor correct  : '))
d = int(input('digit a quart    nota:: '))
while d > 10 :
    d = int(input('voce digit valor da 4º nota invalid digit valor correct  : ' ))
media = (a + b + c + d) / 4
# if a <= 10 and b <= 10 and c <= 10 and d <= 10
if media > 6:
    print("voce foi aprovado")
else:
    print("sua media foi menor que 06 voce não foi aprovado")

print(media)







# a = int(input("digite um numero :  "))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#             # print(x, resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)
# else:
#     print('o numero {} nao e primo', format(a))
#     print(resto)



# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div = div + 1
# if div == 2:
#     print('o numero {} e primo',format(a))
# else:
#     print('o numero {} nao e primo', format(a))
#     print(resto)
# for x in range(101):
#     print(x)
#
#     if










# a = int(input('digite a primeiroa nota: '))
# if a > 10 :
#     a = int(input('voce digitou um valor invalido digite valor da nota correto  : '))
# b = int(input('digite a segunda   nota:: '))
# if b > 10 :
#     b = int(input('voce digitou um valor invalido digite valor da nota correto  : '))
# c = int(input('digite a terceira  nota:: '))
# if c > 10 :
#     c = int(input('voce digitou um valor invalido digite valor da nota correto  : '))
# d = int(input('digite a quarta    nota:: '))
# if c > 10 :
#     c = int(input('voce digitou um valor invalido digite valor da nota correto  : ' ))
# media = (a + b + c + d) / 4
# # if a <= 10 and b <= 10 and c <= 10 and d <= 10
# if media > 6:
#     print("voce foi aprovado")
# else:
#     print("sua media foi menor que 06 voce não foi aprovado")
#
# print(media)
