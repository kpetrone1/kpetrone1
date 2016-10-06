def nested_sum(t):
    """Computes the total of all numbers in a list of lists.
    t: list of list of numbers
    returns: number
    Expected output:
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> nested_sum(t)
    21
    """

    total = 0
    for i in t:             
        total += sum(i)
    return total


def cumsum(t):
    """Computes the cumulative sum of the numbers in t.
    t: list of numbers
    returns: list of numbers
    Expected output:
    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]
    """

    result = []         # empty list
    total = 0
    for i in t:
        total += i
        result.append(total)
    return result


def middle(t):
    """Returns all but the first and last elements of t.
    t: list
    returns: new list
    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    """
    # return t(1:-1)                                  # ?
    # pop(t[1:-1])                                    # ?
    return t[1:-1]


def chop(t):
    """Removes the first and last elements of t.
    t: list
    returns: None
    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    """
    # return t.pop(t[0,-1])
    return t.pop(0,-1)


def is_sorted(t):
    """Checks whether a list is sorted.
    t: list
    returns: boolean                                #?
    Expected output:
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """
    if t = sorted(t):
        return bool                 # Do I have to write "return bool" or can I simply write "bool"?
    

def is_anagram(word1, word2):
    """Checks whether two words are anagrams
    Two words are anagrams if you can rearrange the letters from one to 
    spell the other.
    word1: string or list
    word2: string or list
    returns: boolean
    Expected output:
    >>> is_anagram('stop', 'pots')
    True
    >>> is_anagram('different', 'letters')
    False
    >>> is_anagram([1, 2, 2], [2, 1, 2])
    Ture
    """
    new_word = []
    for letter in word1:
        if letter in word2:
            new_word.append(letter)
        if word1[0:] = new_word and word2[0:] = new_word            # If the elements (aka letters) in word1 are equal to the elements or new_word, return True. I'm trying to determine whether the elements in the two lists are identical. How can I do this? What if I want the elements to be in the same order? What if order is not important? What if I want the function to return True if the elements from Word1 appear in New_Word, but not necessarily ALL of the elements of Word1 appear in New_Word?
            "In the line above, I am attempting to have the code look at the elements (letters) of word1, new_word, word2 from the first element to the last element word2 = [0:]"
            return bool



def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.
    s: string or list
    returns: bool

    output:
    >>> print(has_duplicates('cba'))
    False
    >>> print(has_duplicates('abba'))
    True
    """

    for i in s:
        if s.count(i) > 1:
            return True


def has_adjacent_duplicates(s):
    """Returns True if there are two same adjacent elements.
    s: string or list
    returns: bool
    output:
    >>> print(has_adjacent_duplicates('cba'))
    False
    >>> print(has_adjacent_duplicates('abca'))
    Flase
    >>> print(has_adjacent_duplicates('abbc'))
    True
    """
    pass

    for i in s:
        if s.count(i) > 1:
            return letter               # if this "return" is nested within another function, will it be returned in the output code or will only the value corresponding to the FINAL "return" function listed be presented in the output?
            letter_location_1 = int([])               # index location of first instance of duplicate letter
            letter_location_2 = int([])               # index location of second instance of duplicate letter
            if abs(letter_location_1 - letter_location_2) == 1:     # if the difference between the two locations (i.e. the index numbers) is equal to 1, then those letters are presented next to each other
                return bool

def main():
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))

    t = [1, 2, 3]
    print(cumsum(t))

    t = [1, 2, 3, 4]
    print(middle(t))
    chop(t)
    print(t)

    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))

    print(is_anagram('stop', 'pots'))
    print(is_anagram('different', 'letters'))
    print(is_anagram([1, 2, 2], [2, 1, 2]))

    print(has_duplicates('cba'))
    print(has_duplicates('abba'))


if __name__ == '__main__':
    main()