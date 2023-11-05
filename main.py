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
MAX = 10000
print("Введите число") 
is_prime = [True for _ in range(MAX)]
for i in range(2, int(MAX ** (1 / 2)) + 1):
  if is_prime[i]:
    for j in range(i ** 2, MAX, i):
      is_prime[j] = False 
primes = [i for i in range(MAX) if is_prime[i]] 
while True:
  n = int(input())
  if not n:
    break
  print("число:",n,"сумма:")
  print(sum(primes[:n]))
    
#Задача 7
x, y, z = map(int, input().split())
can_fit = True
while True:
    box = list(map(int, input().split()))
    if box[0] == 0:
        break
    if x < box[0] or y < box[1] or z < box[2]:
        can_fit = False
print("Да" if can_fit else "Нет")

#Задача 8
a = input().split()
b = a[0]
c = len(a) - 1
d = 0
while d != c:
    if len(b) > len(a[d]): b = a[d]
    else: pass
    d += 1
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
word = ''
while True:
    a = input()
    if a == 'стоп': break
    word += a + ' '
word = word.split('!')
for str in word:
    if str.strip() != '':
        print(f'{str.strip()}!')



