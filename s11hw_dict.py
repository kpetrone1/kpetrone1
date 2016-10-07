# >> HOMEWORK: DICTIONARIES <<
# Exercise 1

# def histogram(s):
#     d = {}
#     for c in s:
#         d[c] = s.get(c, 0)        #? How does one add an entire item (that is, BOTH the key and its corresponding value) to a dictionary?
#     return d

# name = 'kaija'

# print(histogram(name))


# Exercise 4
# 1. 


def check_if_word_is_in_wordlist(s): 
    document = open('words.txt')
    d = {}  
    for line in document:
        word = line.strip()             # define a function that determines if s (the string) is in the dictionary
                                            # new dictionary
        if word in d:
            d[word] += 1                # the value of word in dictionary increases by 1
        else:
            d[word] = 1 
    return s in d

print(check_if_word_is_in_wordlist('apple'))
print(check_if_word_is_in_wordlist('kaija'))
                                    
# 2.
def has_duplicates(l):                              # l = given list
    d = {}
    for i in l:
        if i not in d:
            d[i] = 1
        else:
            return True
    return False

name = ['k','a','i','j','a']
print(has_duplicates(name))
    