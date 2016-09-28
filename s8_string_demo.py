team = 'New England Patriots'
print(team[0])
#print(team[1.5])

print(len(team))

print(team[len(team)-1])

last = team[-1]
print(last)


# index = 0
# while index < len(team):
#     letter = team[index]
#     print(letter)
#     index += 1


prefixes = 'JKLMNOPQ'
for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        suffix = 'uack'
    else:
        suffix = 'ack'
    print(letter + suffix)

print(team[0:11])

print(team[12:20])

print(team[:11])

print(team[12:])
print(team[4:3])


print(team[::2])