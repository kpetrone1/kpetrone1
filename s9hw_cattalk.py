#Exercise 3
#1.

fin = open('words.txt')
for line in fin:
    word = line.strip()
    print(word)

for letter in word:
    previous = word[0]
    for c in word:
        if c = previous and previous = previous -1:
            return three_in_a_row
        if three_in_a_row in word and three_in_a_row in word:
            return word