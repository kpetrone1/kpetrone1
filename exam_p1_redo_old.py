def speak_Chinese(number):
    '''
    number: a integer, 0<=number<=999
    Returns: a string that is the number in Chinese
    '''
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4':'si', '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10':'shi', '100':'bai'}
    input_number = str(number)
    if number >= 0 and number <11:
        Chinese_number = trans.get(str(input_number),0)
        return Chinese_number
    else:
        if number >= 11 and number < 20:
            ten = trans.get('10',0)
            digit_index = 0
            if input_number[0] != 1:
                digit_index += 1
                digit = trans.get(str(input_number[digit_index]),0)
                Chinese_number = ten + ' ' + digit
                return Chinese_number
            else:
                pass
        if number >= 20 and number < 100:
            ten = trans.get('10',0)
            digit_index = 0
            digit = trans.get(str(input_number[digit_index]),0)
            if digit == 'ling':
                Chinese_number = digit + ' ' + ten
                return Chinese_number
            else:
                Chinese_number = digit + ' ' + ten + ' '
                digit_index += 1
                digit = trans.get(str(input_number[digit_index]),0)
                Chinese_number += digit
                return Chinese_number
            






            
            # else:                       # if the digit does = zero, do not print it at the end
            #     Chinese_number = digit + ' ' + ten
            #     return Chinese_number
            
             
        



        

        # if input_number[0] != 1

            # return Chinese_number 





    # input_number = str(number)
    # if number in range(11):
    #     for digit in number:
    #         digit = 1
    #         return trans.get(str(input_number[digit]),0)

print(speak_Chinese(11))
print(speak_Chinese(9))
print(speak_Chinese(27))
print(speak_Chinese(50))
def main():
    print(speak_Chinese(36))
    print('In Chinese: 36 = san shi liu')
    print(speak_Chinese(20))
    print('In Chinese: 20 = er shi')
    print(speak_Chinese(16))
    print('In Chinese: 16 = shi liu')
    print(speak_Chinese(109))
    print('In Chinese: 109 = yi bai ling jiu')
    print(speak_Chinese(999))
    print('In Chinese: 999 = jiu bai jiu shi jiu')


if __name__ == '__main__':
    main()
