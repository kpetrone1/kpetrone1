# >> HOMEWORK: DICTIONARIES <<
# Exercise 1

<<<<<<< HEAD
# def histogram(s):
#     d = {}
#     for c in s:
#         d[c] = s.get(c, 0)        #? How does one add an entire item (that is, BOTH the key and its corresponding value) to a dictionary?
#     return d

# name = 'kaija'

# print(histogram(name))
=======
def histogram(s):
    d = {}
    for c in s:
        number_of_(c) = len(h.get(c))
        d.append(c, ':', number_of_(c))               #? How does one add an entire item (that is, BOTH the key and its corresponding value) to a dictionary?
        return d
>>>>>>> 7545d57119443c089fd7dcefa53c4a5f78b9b133


# Exercise 4
# 1. 
<<<<<<< HEAD


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
    
=======
document = open('words.txt')
for line in document:
    word = line.strip()

def check_if_word_is_in_dictionary(s):              # define a function that determines if s (the string) is in the dictionary
    d = {}                                          # new dictionary
    if s in document:
      d.append[s]                                   #? When using append and other such functions, should we use curved parentheses or square brackets?      
                                                    #? Is there a proper way to end the function "check_if_word_is_in_dictionary" or can I leave it at this?
# 2.
def has_duplicates(l):                              # l = given list
    for word in l:
        if count > 1                                # if the "for" loop already specifies that the count is for a "word in l", can I simply say "count > 1" or do I have to say "count(word) > 1" or do I even have to say "l.count(word) > 1"?
            return True
>>>>>>> 7545d57119443c089fd7dcefa53c4a5f78b9b133
