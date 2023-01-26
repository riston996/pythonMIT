import math

x = 2
y = 3
prime = []

print(x,y,prime)

prime.append(x)
prime.append(y)

print(x,y,prime)
print(len(prime))

for k in range (3,7920):
    dum = 2
    for r in range (0,len(prime)):
        if k % prime[r] == 0:
             dum = 1
        else :
            set = 2
    if dum == 2 :
        prime.append(k)

#print(prime)
print(len(prime))
print(prime[999])
print(math.log(2,10))

n = int(input("Enter a number \n"))


j = 0

for i in range (0,n):
    j = j + math.log(prime[i],10)


print(j)



     
