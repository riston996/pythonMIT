# this is a code file that you can use as a template for submitting your
# solutions


##def countSubStringMatch(target, key):
##    txt  = target
##    y = 0
##    x = txt.find(key)
##    print(x)
##
##
##def countSubStringMatchRecursive(target, key):
##    txt  = target
####    y = 0
####    x = txt.find(key)
####    print(x)
##    x = 1
##    while x > 0:
##        x = txt.find(key, x + 1)
##        print(x)

##a = 'abcdef'
##b = 'abcdefs'
##
##if a == b:
##    print("same")
##else:
##    print("not same")


    

##txt = "atgacatgcacaagtatgcat"
##
##x = txt.find("atgc")
##
##print(x)
##
##y = txt.find("atgc",x + 1)
##
##print(y)
##
##z = txt.find("atgc",y + 1)
##
##print(z)

def subStringMatchExact(target,key):
    txt  = target
    tup = []
    x = 1
    while x > 0:
        x = txt.find(key, x + 1)
        if x > 0:
            tup.append(x)
        #print(x)
    return tup
    
# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
##target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

##key10 = 'a'
##key11 = 'atg'
key12 = 'atgc'
##key13 = 'atgca'
##
##subStringMatchExact(target1,key10)
##subStringMatchExact(target1,key11)
##subStringMatchExact(target1,key12)
##subStringMatchExact(target1,key13)
##subStringMatchExact(target2,key10)
##subStringMatchExact(target2,key11)
##subStringMatchExact(target2,key12)
##subStringMatchExact(target2,key13)


### the following procedure you will use in Problem 3


def constrainedMatchPair(match1,match2,len1):
    f = []
    for i in range(0,len(match1)):  
        for k in range(0,len(match2)):
            if match1[i] + 1 + len1 == match2[k]:
                f.append(match1[i])
    return f
    


def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = []
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        #print("miss is  ", miss)
        key1 = key[:miss]
        #print("k1 is  ", key1)
        key2 = key[miss+1:]
        #print("k2 is  ", key2)
        print('breaking key',key,'into',key1,key2)
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers.append(filtered)
        #print('match1',match1)
        #print('match2',match2)
        print('possible matches for',key1,key2,'start at',filtered)
    return allAnswers
        
subStringMatchOneSub(key12,target1)

