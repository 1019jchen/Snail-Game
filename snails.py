import random
n = 10000 #change this to make values of n bigger or smaller
N = 1000 #change this to make values of N bigger or smaller

locations = [0]*n

def groupFinder():
  counter = 1 #stores the number of groups
  randNums = [] #will be a list from 1 to n in order. We will randomly sample from this
  for i in range(n):
    randNums.append(i)
  for i in range(n):
    locations[i] = randNums.pop(random.randrange(len(randNums)))
  for i in range(n-1,0,-1):
    if locations[i] > locations[i-1]:
      counter += 1
    else:
      locations[i-1] = locations[i]
  return counter

trials = [0] * N #stores the results from N trials
for i in range(N):
  trials[i] = groupFinder()
print(sum(trials)/len(trials))
