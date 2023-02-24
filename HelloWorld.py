#bài tập 14
def fac(n) :
    if n == 1 :
        return 1
    return n * fac(n - 1) 

x = 0.5
eps = 0.0000001
mu = 2
first = 1
second = first + x**mu / fac(mu)
while abs(first - second) > eps:
    mu += 2
    first = second
    second = first + x**mu / fac(mu)
print("KQ bài 14: ", second)

#bài tập 13

x = 0.5
eps = 0.0000001
mu = 3
first = x
second = first + x**mu / fac(mu)
while abs(first - second) > eps:
    mu += 2
    first = second
    second = first + x**mu / fac(mu)
print("KQ bài 13: ", second)

#bài tập 12

x = 0.5
eps = 0.00000001
mu = 3
first = x
second = first + x**mu / (mu)
while abs(first - second) > eps:
    mu+=2
    first = second
    second = first + x**mu / (mu)
print("KQ bài 12: ", 2*second)

#bài tập 11

x = 0.5
eps = 0.000001
mu = 2
dau = -1
first = 0.5
second = first - x**mu / (mu)
while abs(first - second) > eps:
    mu-=-1
    first = second
    second = first - (dau * x**mu / mu)
    dau = -dau
print("KQ bài 11: ", second)

#bài tập 10

x = 0.5
eps = 0.000000001
mu = 3
dau = -1
first = x
second = first - x**mu / mu
while abs(first - second) > eps:
    mu+=2
    first = second
    second = first - (dau * x**mu / mu)
    dau = -dau
print("KQ bài 10: ", second)

#bài tập 9

x = 0.5
eps = 0.000001
mu = 1
dau = -1
first = 1
second = first - x**(mu + 1) / fac(mu + 2)
while abs(first - second) > eps:
    mu+=2
    first = second
    second = first - (dau * x**(mu + 1) / fac(mu + 2))
    dau = -dau
print("KQ bài 9: ", second)

#bài tập 8

x = 0.5
eps = 0.000001
mu = 3
tu = 3
mau = 4
first = 0.5
count = 1
n = 0
temp = 0    
second = first + 0.5*x**mu / mu
while abs(first - second) > eps:
    mu += 2
    count+=1
    n = count
    temp = 0.5 * x**mu / mu
    first = second
    while(n>0):
        temp = temp*(tu/mau)
        tu = tu + 2
        mau = mau + 2
        n-=1
    second = first + temp
print("KQ bài 8: ", second)        

#bài tập 7

x = 0.5
eps = 0.000001
mu = 2
dau = -1
first = 1
second = first - x**mu / fac(mu)
while abs(first - second) > eps:
    mu+=2
    first = second
    second = first - (dau * x**mu / fac(mu))
    dau = -dau
print("KQ bài 7: ", second)

#bài tập 6

x = 0.5
eps = 0.00001
mu = 3
dau = -1
first = 0.5
second = first - x**mu / fac(mu)
while abs(first - second) > eps:
    mu+=2
    first = second
    second = first - (dau * x**mu / fac(mu))
    dau = -dau
print ("KQ bài 6: ", second)

#bài tập 5

first = 1
x = 0.5
mu = 1
dau = -1
eps = 0.00001
n
temp = 1
second = first - 0.5*x**mu
while abs(first - second) > eps:
    tu = 3
    mau = 4
    mu -= -1
    n = mu
    temp = 0.5 * x**mu
    first = second
    while(n>1):
        temp = temp * (tu/mau)
        tu = tu + 2
        mau = mau + 2
        n-=1
    dau = -dau
    second = first + dau*temp
print("KQ bài 5: ", second)        

#bài tập 4

first = 1
x = 0.5
mu = 1
dau = -1
eps = 0.000001
n 
temp = (0.5) * x**mu
second = first + 0.5 * x**mu
while abs(first - second) > eps:
    tu = 1
    mau = 4
    mu -=- 1
    n = mu
    temp = 0.5 * (x**mu)
    first = second
    while(n>1):
        temp = temp * (tu/mau)
        tu = tu + 2
        mau = mau + 2
        n-=1
    second = first + dau * temp
    dau = -dau
print("KQ bài 4: ", second) 

#bài tập 3

first = 0.5
x = 0.5
temp = 2
eps = 0.000001
second = -1*first - (x**temp/temp)
while abs(first - second) > eps:
    temp -= -1
    first = second
    second = first - (x**temp/temp)
print("KQ bài 3: ", second)

#bài tập 2

first = 1
x = 0.5
temp = 1
dau = -1
eps = 0.000001
second = first + dau*(((temp + 1)*(temp + 2))/2)*x**temp
while abs(first - second) > eps:
    temp -= -1
    dau = -dau
    first = second
    second = first + dau*(((temp + 1)*(temp + 2))/2)*x**temp
print("KQ bài 2: ", second)

#bài tập 1

first = 1
x = 0.5
eps = 0.000001
mu =1
second = first + x**mu / fac(mu)
while abs(first - second) > eps:
    mu -= -1
    first = second
    second = first + x**mu / fac(mu)
print("KQ bài 1: ", second)