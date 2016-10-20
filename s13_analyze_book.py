import random
import string


def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break
        line = line.replace('-', ' ')                   #? What are we doing here? Why?
        strippables = string.punctuation + string.whitespace

        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()

        # word = line.strip(string.whitespace + string.punctuation)         #? Could this work?
            # update the histogram
            hist[word] = hist.get(word, 0) + 1          #? develop understanding
            
    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):            
            break


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())
    

def different_words(hist):
    """Returns the number of different words in a histogram."""
    return count(hist.keys())                               #? correct? (my personal code)


def most_common(hist):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    words_in_order_of_frequency = []
    for key, value in hist.items():                         #? Explanation of "key, value"? What would happen if one reverses the order to "value, key"? 
        words_in_order_of_frequency.append(value,key)       #? Why do we switch order to "value, key"? Does order of "key" and "value" here have to match order of "key" and "value" in line above? Would it be incorrect to say "key, value" instead of "value, key"?
    
    words_in_order_of_frequency.sort()
    words_in_order_of_frequency.reverse()
    return words_in_order_of_frequency

    

    # for word in line:                                     # (original thinking)
    #     words_in_order_of_frequency.append()              # (original thinking)
    

def print_most_common(hist, num=10):
    """Prints the most commons words in a histogram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    words_in_order_of_frequency = most_common(hist)
    print('The most common words are:')
    for freq, word in words_in_order_of_frequency[:num]:        #? Does "[:num]" say range 0 to num (not including num)? or does it say range from beginning to num? Are previous two questions identical? Does "beginning" always = 0?
        print(word, '\t', freq)

    # index = 0
    # while index < num:
    #     print(words_in_order_of_frequency[index])



    # for index in range(num):




    # for item in range(num):
    #     print value 


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.
    d1, d2: dictionaries
    """
res = {}                                        #? For what does "res" stand?
   for key in d1:
       if key not in d2:
           res[key] = None                      #? What does this mean? What does "res[key]" mean specifically? What does "= None" do?
    return res
       
    
    # keys_in_d1_but_not_in_d2 = {}             # (original thinking)
    # for key in d1:
    #     if key not in d2:
    #         keys_in_d1_but_not_in_d2 += key
    # return keys_in_d1_but_not_in_d2
    

def random_word(hist):
    """Chooses a random word from a histogram.
    The probability of each word is proportional to its frequency.
    """
    words_in_order_of_frequency = []            #? #What does this whole block instruct? # Is this really a list of words in order of frequency? For what does "t" stand in Prof.'s solution code here and in previous functions above?
    for word, freq in hist.items():
        words_in_order_of_frequency.extend([word] * freq)

    return random.choice(words_in_order_of_frequency)


def main():
    hist = process_file('s13_Pride and Prejudice.txt', skip_header=True)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)

    words = process_file('words.txt', skip_header=False)

    diff = subtract(hist, words)
    print("The words in the book that aren't in the word list are:")
    for word in diff.keys():
        print(word, end=' ')

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()