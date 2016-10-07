# >> HOMEWORK: DICTIONARIES <<
# Exercise 1

def histogram(s):
    d = {}
    for c in s:
        number_of_(c) = len(h.get(c))
        d.append(c, ':', number_of_(c))               #? How does one add an entire item (that is, BOTH the key and its corresponding value) to a dictionary?
        return d


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
# 2.
def has_duplicates(l):                              # l = given list
    for word in l:
        if count > 1                                # if the "for" loop already specifies that the count is for a "word in l", can I simply say "count > 1" or do I have to say "count(word) > 1" or do I even have to say "l.count(word) > 1"?
            return True
