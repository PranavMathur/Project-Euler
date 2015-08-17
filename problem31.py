from time import *

start = time()

count = 0

for twoHundreds in range(0, 2):
    maxOneHundreds = int(200-200*twoHundreds)
    for oneHundreds in range(0, maxOneHundreds+1):
        maxFiftys = int(200-(200*twoHundreds+100*oneHundreds))
        for fiftys in range(0, maxFiftys+1):
            maxTwentys = int(200-(200*twoHundreds+100*oneHundreds+50*fiftys))
            for twentys in range(0, maxTwentys+1):
                maxTens = int(200-(200*twoHundreds+100*oneHundreds+50*fiftys+20*twentys))
                for tens in range(0, maxTens+1):
                    maxFives = int(200-(200*twoHundreds+100*oneHundreds+50*fiftys+20*twentys+10*tens))
                    for fives in range(0, maxFives+1):
                        maxTwos = int(200-(200*twoHundreds+100*oneHundreds+50*fiftys+20*twentys+10*tens+5*fives))
                        for twos in range(0, maxTwos+1):
                            maxOnes = int(200-(200*twoHundreds+100*oneHundreds+50*fiftys+20*twentys+10*tens+5*fives+2*twos))
                            for ones in range(0, maxOnes+1):
                                if 200*twoHundreds+100*oneHundreds+50*fiftys+20*twentys+10*tens+5*fives+2*twos+ones == 200:
                                    count += 1

print(count)
print(time()-start)
                        
