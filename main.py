#Задача 1
while True:
    a = input()
    if len(a) != 0: print(len(a))
    else: break

#Задача 2
n = 0
while True:
    a = input()
    if a[0] == '-': n += 1
    elif a == '36.6':
        break
print(n)

#Задача 3
list = list()
while True:
    a = int(input())
    if a > 1000 or a < -1000:
        break
    else:
        list.append(a)
max1 = max(list)
list.remove(max1)
max2 = max(list)
print(max2)

#Задача 4
a = input().split()
b = int(a[0])
c = len(a)
n = 0
while n != c:
    if int(b) > int(a[n]): b = int(a[n])
    else: pass
    n += 1
print(b)

#Задача 5
while True:
    a = int(input())
    if a == 0: break
    elif a % 3 == 0 and a % 7 == 0: print('Караул!')
    elif a % 3 == 0: print('Несчастливое')
    elif a % 7 == 0: print('Опасное')
    else: print(a)

#Задача 6

#Задача 7
a = input().split()
b = input().split()
vbig = int(a[0])*int(a[1])*int(a[2])
vskinny = 0
k = 0
while True:
    if int(b[k]) == 0: break
    v = int(b[k])*int(b[k+1])*int(b[k+2])
    k += 3
    vskinny += v
if vbig >= vskinny: print('Да')
else: print('Нет')

#Задача 8
a = input().split()
b = a[0]
c = len(a) - 1
n = 0
while n != c:
    if len(b) > len(a[n]): b = a[n]
    else: pass
    n += 1
print(b)

#Задача 9
c = input()
if c == 'стоп':
    exit()
c = int(c)
d = ''
while True:
    a = input()
    if a == 'стоп': break
    elif a in '+-/*': d = a; continue
    elif d == '+': c += int(a)
    elif d == '-': c -= int(a)
    elif d == '/': c /= int(a)
    elif d == '*': c *= int(a)
print(int(c))

#Задача 10
phrase = ''
while True:
    a = input()
    if a == 'стоп': break
    phrase += a + ' '
phrase = phrase.split('!')
for str in phrase:
    if str.strip() != '':
        print(f'{str.strip()}!')



