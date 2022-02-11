n = int(input("input:"))
a = 1
b = 1
c = a + b
d = b + c
x = c + d
i = 4

if n == 1 :
	print ("1")
elif n == "2" :
	print ("1")
elif n == "3" :
	print ("2")
elif n == "4" :
	print ("3")
else :
	while i != int(n)  :
		x = c + d 
		c = d
		d = x
		i = i+1
	print (x)





