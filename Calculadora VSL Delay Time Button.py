#formula min to ms = multiplique o valor de tempo por 60000
#formula sec to ms = multiplique o valor de tempo por 1000


m = int(input("Digite o minuto desejado:  "))
m1 = m*60000
s =  int(input('Digite o segundo desejado:  '))
s1 = s*1000
ms = m1+s1



print('Os milisegundos exatos são {}'.format(ms))