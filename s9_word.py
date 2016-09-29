fin = open('words.text')
for line in fin:



def read_long_words():
    """
    prints only the words with more than 20 characters      #! print vs. return: pay attention to whether instructions request to print or to return
    """
    fin = open('words.txt')
    for line in fin:
        word = line.strip()


def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
        return True











'''
fin = open('words.text')
for line in fin:
    word = line.strip()
    print(word)
'''

#Exercise 1
#1.
fin = open('words.txt')
for line in fin:
    if len(word) > 20:
        print(word)




# # fin = open('words.txt')
# # line = repr(fin.readline())
# # print(line)                                                 #added
# # # https://docs.python.org/3/library/functions.html#repr

# fin = open('words.txt')
# for line in fin:
#     word = line.strip()
#     print(word)


# def read_long_words():
#     """
#     prints only the words with more than 20 characters
#     """
#     pass


# def has_no_e(word):
#     """
#     returns True if the given word doesn’t have the letter “e” in it.
#     """
#     pass


# def avoids(word, forbidden):
#     """
#     takes a word and a string of forbidden letters, and that returns True
#     if the word doesn’t use any of the forbidden letters.
#     """
#     pass


# def uses_only(word, available):
#     """
#     takes a word and a string of letters, and that returns True if the word
#     contains only letters in the list.
#     """
#     pass


# def uses_all(word, required):
#     """
#     takes a word and a string of required letters, and that returns True if
#     the word uses all the required letters at least once.
#     """
#     pass


# def is_abecedarian(word):
#     """
#     returns True if the letters in a word appear in alphabetical order
#     (double letters are ok).
#     """
#     pass
