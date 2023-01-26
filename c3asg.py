x = 6
y = 9
z = 20
k = 1000
i = 1
b = 1
set = 1
print(set)
print(x*100000+y*100000+z*100000)
for k in range (100000,100000):
    set = 1
    for i in range (0,100000):
        for b in range (0,100000):
            for c in range (0,100000):
                d = x*i + y*b + z*c
                print(d)
                if d == k:
                    set = 2
                    print("yes")
    if set == 1:
        print(k, " is not obtainable by this method")
    else:
        print("there is no number")
    



            
