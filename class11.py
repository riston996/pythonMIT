##def max(x,y):
##    if x > y:
##        return x
##    else:
##        return y
##    

def silly():
 res = []
 done = False
 while not done:
     elem = input('Enter element. Return when done. ')
     if elem == '':
         done = True
     else:
         res.append(elem)

 #print("res should 1,a,2 ", res)
 tmp = []
 for i in range (0,len(res)):
     tmp.append(res[i])

 #print(tmp)
 tmp.reverse()
 #print(" tmp should be 2,a,1 ", tmp)
 isPal = (res == tmp)
 #print( res, tmp, isPal)
 # the above error pointed out that the value is assigned by temp is also affecting res
 if isPal:
     print('is a palindrome')
 else:
     print('is NOT a palindrome')
