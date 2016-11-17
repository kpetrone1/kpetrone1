# # Caesar Cipher Program
# # using for loop
# # by WebCraftie

# # creating variable
# userMessage = "Tragedy! Send tacos immediately."
# userMessage = userMessage.lower()
# shiftValue = 1
# encryptedMsg = ''

# # running the for loop
# for character in userMessage:
#     if character.isalpha() == True:    # only apply to letters, not to punctuation
#         x = ord(character) - 97   # convert character into equivalent number that's tied to this method # 97 = ord value of a 
#         x += shiftValue
#         x = x % 26      # "if this value is divisible by 26, it will...produce the remainder"
#         encryptedMsg += chr(x + 97 )      # going back from the number into the equivalent letter # whatever you do to one side of the equation, you have to do to the other (adding back 97)
#     else:
#         encryptedMsg += character

# # printing the result
# print(encryptedMsg)3


def create_moved_dict(move):
        '''
        Creates a dictionary that maps every letter to a
        character moved down the alphabet by the input move. 
        move: an integer, 0 <= move < 26
        Returns: a dictionary
        Example: an_instance_of_Text.create_moved_dict(2) would generate
        {'a': 'c', 'b': 'd', 'c':'e', ...}  
        '''
        # old URL of Source: https://www.youtube.com/watch?v=dAo0NC8wR-8
        pass  # delete this line and replace with your code here
        # URL of Source: http://www.stealthcopter.com/blog/2009/12/python-cryptography-caesar-shift-encryption-shift-cipher/
        alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        new_alphabet = {}
        for i in range(0, len(alphabet)):
            new_alphabet[alphabet[i]] = alphabet[(i+move)%len(alphabet)]        # take the key in the original alphabet and incorporate it to be the key in the new alphabet; assign a value  equal to the [letter (aka "i") + move] and find the modulo of that number by 26 so that the remainder of the ltters will loop around to the beginning (ex: so when shift = 2, z = b and z does not equal nothing at the end)
            return new_alphabet
       
print(create_moved_dict(3))
       