import random

n = [] # [-77,78,82,23,57,29,-73,-20,90,84]

for i in range(10):
    n.append(random.randrange(-100, 100))

print(n)
max = n[0]
temp = 0

#for i in range(10):
#    for j in range(10-i):

for i in range(len(n)):
        temp += n[i]

        if(temp > max):
            print(temp)
            max = temp
        elif(temp <= 0):
            temp = 0

print(max)