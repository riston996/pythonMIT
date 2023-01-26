##"""Assumes x >= 0 and epsilon > 0
## Return y s.t. y*y is within epsilon of x"""
##def squareRootBi(x, epsilon):
##    assert x >= 0, 'x must be non-negative, not' + str(x)
##    assert epsilon > 0, 'epsilon must be positive, not' + str(epsilon)
##    low = 0
##    high = max(x,1)
##    guess = (low + high)/2.0
##    ctr = 1
##    while abs(guess**2 - x) > epsilon and ctr <= 100:
##     #print 'low:', low, 'high:', high, 'guess:', guess
##     if guess**2 < x:
##         low = guess
##     else:
##        high = guess
##     guess = (low + high)/2.0
##     ctr += 1
##    assert ctr <= 100, 'Iteration count exceeded'
##    print('Bi method. Num. iterations:', ctr, 'Estimate:', guess)
##    return guess 


##"""Assumes x >= 0 and epsilon > 0
##Return y s.t. y*y is within epsilon of x"""
##def squareRootNR(x, epsilon):
##    assert x >= 0, 'x must be non-negative, not' + str(x)
##    assert epsilon > 0, 'epsilon must be positive, not' + str(epsilon)
##    x = float(x)
##    guess = x/2.0
##    guess = 0.001
##    diff = guess**2 - x
##    ctr = 1
##    while abs(diff) > epsilon and ctr <= 100:
##     #print 'Error:', diff, 'guess:', guess
##     guess = guess - diff/(2.0*guess)
##     diff = guess**2 - x
##     ctr += 1
##    assert ctr <= 100, 'Iteration count exceeded'
##    print('NR method. Num. iterations:', ctr, 'Estimate:', guess)
##    return guess 

##Techs = ['MIT', 'Cal Tech']
##print(Techs)
##Ivys = ['Harvard', 'Yale', 'Brown']
##print(Ivys)
##Univs = []
##Univs.append(Techs)
##print(Univs)
##Univs.append(Ivys)
##input()
##print(Univs)
##input()
##for e in Univs:
## print(e)
## for c in e: print(c)
##input()
##Univs = Techs + Ivys
##print(Univs)
##input()
##Ivys.remove('Harvard')
##print(Univs) 
##Ivys[1] = -1 
##print(Ivys) 

##EtoF = {'one': 'un', 'soccer': 'football'}
##print(EtoF['soccer'])
###print(EtoF[0])
##print(EtoF)
##NtoS = {1: 'one', 2: 'two', 'one': 1, 'two': 2}
###print(NtoS.keys())
###print(NtoS.keys)
##print(NtoS['one'])
##print(NtoS)

##L = [['un', 'one'], ['deux', 'two']] 
##def keySearch(L, k):
##    for elem in L:
##        if elem[0] == k: return elem[1]
##    return None
##
##print keySearch(L, 'deux') 
