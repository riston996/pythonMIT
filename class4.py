##def sqrt(x):
## """Returns the square root of x, if x is a perfect square.
## Prints an error message and returns None otherwise"""
## ans = 0
## if x >= 0:
##     while ans*ans < x: ans = ans + 1
##     if ans*ans != x:
##         print(x, 'is not a perfect square')
##         return None
##     else: return ans
## else:
##     print(x, 'is a negative number')
##     return None
##
##
##y = sqrt(16)
##
##print(y)

#to show scope in function does not impact the main
##def f(x):
## x = x + 1
## return x
##
##
##x = 3
##z = f(x)
##print(x)
##print(z)     
##



##def solve(numLegs, numHeads):
##     for numChicks in range(0, numHeads + 1):
##         numPigs = numHeads - numChicks
##         totLegs = 4*numPigs + 2*numChicks
##         if totLegs == numLegs:
##             return (numPigs, numChicks)
##     return (None, None)
##    
##def barnYard():
##     heads = int(int(input('Enter number of heads: ')))
##     legs = int(int(input('Enter number of legs: ')))
##     pigs, chickens = solve(legs, heads)
##     if pigs == None:
##         print('There is no solution')
##     else:
##         print('Number of pigs:', pigs)
##         print('Number of chickens:', chickens)


##def isPalindrome(s):
##    if len(s) <= 1:
##        return True
##    else:
##        return s[0] == s[-1] and isPalindrome(s[1:-1])


"""Return fibonacci of x, where x is a non-negative int"""
def fib(x):
 if x == 0 or x == 1:
     return 1
 else:
     return fib(x-1) + fib(x-2) 

    
