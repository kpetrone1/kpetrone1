str = "this is the text in the string."
newStr = ""

for letter in str:
    if (ord(letter) in range (65, 91) or ord(letter) in range (97,121)):
        letter = chr(ord(letter)+2)

        elif(letter == 'y' or letter == 'z'):
            letter 