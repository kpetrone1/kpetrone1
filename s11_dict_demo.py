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

# >> HOMEWORK: DICTIONARIES <<
# Exercise 1

def histogram(s):
    d = {}
    for c in s:
        number_of_(c) = len(h.get(c))
        d.append(c, ':', number_of_(c))               #? How does one add an entire item (that is, BOTH the key and its corresponding value) to a dictionary?
        return d


'''Scrap Paper:
        # return h.get(c)


    #     number(c) = h.get(c, 0))


    # alphabet = {}
    # for c in s:
    #     alphabet['a'] =  1
   
        
    # number_of_ch1 = h.get          # index number of first character
'''

# Exercise 4
# 1. 
document = open('words.txt')
for line in document:
    word = line.strip()

def check_if_word_is_in_dictionary(s):              # define a function that determines if s (the string) is in the dictionary
    d = {}                                          # new dictionary
    if s in document:
      d.append[s]                                   #? When using append and other such functions, should we use curved parentheses or square brackets?      
                                                    #? Is there a proper way to end the function "check_if_word_is_in_dictionary" or can I leave it at this?
                                    

'''Scrap Paper:
def check_if_word_is_in_dictionary(s):             # define a function that determines if s (the string) is in the dictionary
    d = {}                          # new dictionary
    if s in document:
      d.append[s]                 #? When using append and other such functions, should we use curved parentheses or square brackets?      
'''



# 2.
def has_duplicates(l):                              # l = given list
    for word in l:
        if count > 1                                # if the "for" loop already specifies that the count is for a "word in l", can I simply say "count > 1" or do I have to say "count(word) > 1" or do I even have to say "l.count(word) > 1"?
            return True

'''Scrap Paper:
#     list.count(l)                                 # count the number of times "l" appears in the list


#     if s 


# "def find_triple_double():
#     """Reads a word list and prints words with triple double letters."""
#     fin = open('words.txt')
#     for line in fin:
#         word = line.strip()
#         if is_triple_double(word):
#             print(word)"

'''