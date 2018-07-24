sum = 0
for i in range(0,1000,1):
    if ((i%3==0) | (i%5==0)):
        sum+=i
        i = i + 1
print (sum)
