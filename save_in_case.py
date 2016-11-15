def speak_Chinese(number):
    '''
    number: a integer, 0<=number<=999
    Returns: a string that is the number in Chinese
    '''
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4':'si', '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10':'shi', '100':'bai'}
    input_number = str(number)
    # print(input_number.slice())
    # input = str(number)

    for i in input_number:
        if len(input_number) == 1:
            return trans.get(i, 0)
        else:
            if len(input_number) > 1 and len(input_number) < 3:
                if input_number[-1] != 0:
                    Chinese_number = ''
                    Chinese_number += trans.get(str(input_number[0]),0)
                    Chinese_number += ' '
                    Chinese_number += trans.get('10',0)
                    Chinese_number += ' '
                    Chinese_number += trans.get(str(input_number[1]),0)
                    return Chinese_number
                else:
                    Chinese_number = ''
                    Chinese_number += trans.get(str(input_number[0]),0)
                    Chinese_number += ' '
                    Chinese_number += trans.get('10',0)
                    return Chinese_number
            else:
                # if len(input_number) > 2 and len(input_number) < 3:
                    Chinese_number = ''
                    Chinese_number += trans.get(str(input_number[0]),0)
                    Chinese_number += ' '
                    Chinese_number += trans.get('10',0)                         # change '10' to '100'
                    Chinese_number += ' '
                    Chinese_number += trans.get(str(input_number[1]),0)
                    Chinese_number += ' '
                    Chinese_number += trans.get(str(input_number[2]),0)
                    return Chinese_number


    # for i in input_number:
    #     if len(input_number) == 1:
    #         return trans.get(i, 0)
    #     else:
    #         if len(input_number) > 1 and len(input_number) < 3:
    #             Chinese_number = ''
    #             index_number = 0
    #             index = str(input_number[index_number])
    #             Chinese_number += trans.get(index,0)
    #             Chinese_number += ' '
    #             Chinese_number += trans.get('10',0)
    #             Chinese_number += ' '
    #             index_number += 1
    #             Chinese_number += trans.get(index,0)
    #             return Chinese_number

            # while i in range(len(input_number)):
            #     Chinese_number = trans.get(i,0)
            #     Chinese_number += trans.get('10',0)
            
            #     return Chinese_number
        
    # for i in range(len(input_number))
    #     return trans.get(i,0)

                # Chinese number = ''
                # Chinese_number = trans.get(input_number[0])

                # return trans.get(i)

print(speak_Chinese(36))

    # print(trans.values())
    # print(trans.keys())


        


#         if len(number)



#     Chinese_number = ''

#     return Chinese_number

# For testing
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
