import random
n=100
a=0
b=100
c=random.randint(1,100)
while 0<=n and n <= 100:
    n = input ("please guess a number from " + str(a) + "-"+ str(b))
    n = int(n)
    if c < n <= b :
        b = n
    elif a <= n < c :
        a = n
    elif n == c :
        print ("congratulations!!! this is the right number")
        break


