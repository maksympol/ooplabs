f = 9325
print(f,'- номер залікової книжки')
C2 = f % 2
print('C2 =', C2, '- операція -')
C3 = f % 3
print('C3 =', C3, '- константа')
C5 = f % 5
print('C5 =', C5, '- операція *')
C7 = f % 7
print('C7 =', C7)
class lab_1:
    @staticmethod
    def func(self):
        s = 0
        a = int(input("Input a " ))
        n = int(input("Input n "))
        b = int(input("Input b "))
        m = int(input("Input m "))
        if a <= n and b <= m:
            for i in range(a, n+1):
                for j in range(b, m+1):
                    s += (i*j)/(i+1)
            print("S =", s)
        else:
            print('Помилка')
lab_1.func("self")