# exercise 1
i = 100
while True:
    print("The value of i is " + str(i))
    i = i - 2
# to make sure it doesn't go on infinitely
    if i < 0:
        break
# continue to next sequence of code
        continue

# exercise 2
badlist = [42, 'purple', (90210, 58), 100, 'monkey', 'dishwasher']
goodlist = []

# for loop with x meaning any variable
for x in badlist:
# checking if variable type is a string  
    if type(x) is str:
# appending strings into goodlist 
        goodlist.append(x)
        print(goodlist)
        
