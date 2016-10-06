names = ['Rose', 'Jerry', 'Alex']
scores = [95, 75, 85]
i = names.index('Jerry')
print(scores[i])


grades = {'Jerry':75, 'Rose':95}
print(grades['Jerry'])

grades['Brian'] = 90
print(grades)

print(len(grades))
print('Jerry' in grades)
print(90 in grades.values())


def histogram(s):
    d = {}               # empty dictionary
    for c in s:
        if c not in d:   # c is a letter in a string
            d[c] = 1
        else:
            d[c] += 1
    return d

h = histogram('Bookkeeper')
print(h)