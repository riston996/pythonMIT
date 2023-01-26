"""

How many samples ?
it is not possible to assume what is the correct sample

How accurrate?
It is not possible to get the exactly right

Satistics can be correct but answer can be wrong






"""



from pylab import * 
import random, math 
 
##def flipTrial(numFlips): 
##    heads, tails = 0, 0 
##    for i in range(0, numFlips): 
##        coin = random.randint(0, 1) 
##        if coin == 0: heads += 1 
##        else: tails += 1 
##    return heads, tails 
## 
##def simFlips(numFlips, numTrials): 
##    diffs = [] 
##    for i in range(0, numTrials): 
##        heads, tails = flipTrial(numFlips) 
##        diffs.append(abs(heads - tails)) 
##    diffs = array(diffs) 
##    diffMean = sum(diffs)/len(diffs) 
##    diffPercent = (diffs/float(numFlips))*100 
##    percentMean = sum(diffPercent)/len(diffPercent) 
##    hist(diffs)     
##    axvline(diffMean, color = 'r', label = 'Mean') 
##    legend() 
##    titleString = str(numFlips) +  ' Flips, ' + str(numTrials) + ' Trials' 
##    title(titleString) 
##    xlabel('Difference between heads and tails') 
##    ylabel('Number of Trials') 
##    figure() 
##    plot(diffPercent)         
##    axhline(percentMean, color = 'r', label = 'Mean') 
##    legend() 
##    title(titleString) 
##    xlabel('Trial Number') 
##    ylabel('Percent Difference between heads and tails')
##
##
##simFlips(1000,1000)
##show()

##def throwDarts(numDarts, shouldPlot): 
##    inCircle = 0 
##    estimates = [] 
##    for darts in range(1, numDarts + 1, 1): 
##        x = random.random() 
##        y = random.random() 
##        if math.sqrt(x*x + y*y) <= 1.0: 
##            inCircle += 1 
##        if shouldPlot: 
##            piGuess = 4*(inCircle/float(darts)) 
##            estimates.append(piGuess) 
##        if darts%1000000 == 0: #So I know it's making progress 
##            piGuess = 4*(inCircle/float(darts)) 
##            #dartsStr = locale.format('%d', darts, True) 
##            print('Estimate with', 'darts:', piGuess) 
##    if shouldPlot: 
##        xAxis = arange(1, len(estimates)+1) 
##        semilogx(xAxis, estimates) 
##        titleString = 'Estimations of pi, final estimate: ' + str(piGuess) 
##        title(titleString) 
##        xlabel('Number of Darts Thrown') 
##        ylabel('Estimate of pi') 
##        axhline(3.14159) 
##    return 4*(inCircle/float(numDarts)) 
## 
##def findPi(numDarts, shouldPlot=False): 
##    piGuess = throwDarts(numDarts, shouldPlot) 
##    print('Estimated value of pi with', 'darts:', piGuess) 
## 
##findPi(10000, True) 
##findPi(100000000) 
##show() 



##def getSpringData(fname): 
##    springData = open(fname, 'r') 
##    distances = [] 
##    forces = [] 
##    for line in springData: 
##        if line[0] == '#': continue 
##        line = line[:-1] 
##        elems = line.rsplit(':') 
##        distances.append(float(elems[0])) 
##        forces.append(float(elems[1])) 
##    return pylab.array(distances), pylab.array(forces) 
## 
##distances, forces = getSpringData('springData.txt') 
##pylab.scatter(distances, forces) 
##pylab.xlabel('Distance (Meters)') 
##pylab.ylabel('|Force| (Newtons)') 
##pylab.title('Force vs. Distance for Spring') 
##
## 
##
##k, b = pylab.polyfit(distances, forces, 1) 
##yVals = k*distances + b 
##pylab.plot(distances, yVals, c = 'r', linewidth = 2) 
##pylab.title('Force vs. Distance, k = ' + str(k))
