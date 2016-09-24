
result = 0
for i in range(1,11,2):
    print('current i:', i)
    result += i
print(result)

result = 0
for i in range(11):
    if i%2 ==1:                 #??? means it's an odd number
        print('current i:', i)
    result += i
print(result)

#even numbers
result = 0
for i in range(11):
    if i%2 ==0:                 
        print('current i:', i)
    result += i
print(result)


#while statement
def countdown(n):
    while n>0:
        print(n)
        n=n-1           #???Prof wrote "n-=1" for this line; why?
    print('Blastoff!')

countdown(5)

'''
iteration=0
count=0
while iteration <5:
    for letter in "hello, world":
        count += 1      #counting number of characters (including space and comma) in phrase
    print("Iteration " + str(iteration) + ";
    count is: "")


iteration -- second version
'''

while True:
    line = input('>')
    if line == 'done':
        break
    print(line)

print('Done!')

'''
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count +=
'''

result = 0
i = 1       #starting point
while i < 11:
    result = result+1       #? shoudld this be result + i, not +1?
    i = i + 1

print(result)


#even
result = 0                  #result = variable and we're instructing it to start at zero
i = 1       #starting point
while i < 11:
    if i %2 ==0:
        result = result+i
    i = i + 1

print(result)