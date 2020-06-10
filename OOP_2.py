import random

f = 9325
print(f,'- номер залікової книжки')
C5 = f % 5
print('C5 =', C5, '- операція *')
C7 = f % 7
print('C7 =', C7)
C11 = f % 11
print('C11 =', C11)

import random

class lab_1:
    @staticmethod
    def matr(self):
        a=[]
        o = int(input('Уведіть константу: '))
        k = int(input('Уведіть кількість рядків: ')) #рядок
        l = int(input('Уведіть кількість стовпців: ')) #стовпець
        print('Маємо матрицю: ')
        for i in range (k):
            b = []
            for i in range (l):
                b.append(random.randint(0,100))
            a.append(b)
        for i in a:
            print(i)
        for k in a:
            print('Cереднє значення рядка: %.2f' % (sum(k)/len(k)))



lab_1.matr("self")