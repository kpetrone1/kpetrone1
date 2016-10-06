def binary_search(my_list, x):
    '''
    this function adopts bisection/binary search to find the index of a given
    number in an ordered list
    my_list: an ordered list of numbers from smallest to largest
    x: a number
    returns the index of x if x is in my_list, None if not.
    '''

    '''
    From Session 8 Handout on Strings from Professor Zhi Li:
    https://blackboard.babson.edu/webapps/blackboard/execute/content/file?cmd=view&content_id=_712254_1&course_id=_15079_1&framesetWrapped=True
    '''
    
    index = 0
    while index < len(my_list)/2:   # while the index is less than half of the length of the whole list  (I divided "len(my_list)" by 2, although I am not positive if that was a correct change)
        if my_list[index] == x:     # if the index is equal to the letter,...
            return index            # return the index, which is the number of the element in the list, c?
        index = index + 1           # add 1 to the index to continue the "while"" loop by finding the value of the index for the next letter
    return - 1                      # subtract 1 to return the index



    # my_list = []
    # x 


    # if my_list[]


    # pass


test_list = [1, 3, 5, 235425423, 23, 6, 0, -23, 6434]
test_list.sort()

print(binary_search(test_list, -23))
print(binary_search(test_list, 0))
print(binary_search(test_list, 235425423))
print(binary_search(test_list, 30))

# expected output
# 0
# 1
# 8
# None
