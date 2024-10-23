#Variables
quit = False



def encode():
    print('Please enter your password to encode: ', end='')
    encrypted = ''
    password = input()
    for element in password:
        if element == '0':
            encrypted += '3'
        elif element == '1':
            encrypted += '4'
        elif element == '2':
            encrypted += '5'
        elif element == '3':
            encrypted += '6'
        elif element == '4':
            encrypted += '7'
        elif element == '5':
            encrypted += '8'
        elif element == '6':
            encrypted += '9'
        elif element == '7':
            encrypted += '0'
        elif element == '8':
            encrypted += '1'
        elif element == '9':
            encrypted += '2'
    print('Your password has been encrypted and stored!\n')
    return encrypted

def decode(encrypted):
    res = ''
    for element in encrypted:
        if element == '0':
            res += '7'
        elif element == '1':
            res += '8'
        elif element == '2':
            res += '9'
        elif element == '3':
            res += '0'
        elif element == '4':
            res += '1'
        elif element == '5':
            res += '2'
        elif element == '6':
            res += '3'
        elif element == '7':
            res += '4'
        elif element == '8':
            res += '5'
        elif element == '9':
            res += '6'
    return res

if __name__ == '__main__':
    while not quit:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')
        print('Please enter an option: ', end='')
        option = input()

        #option
        if option == '1':
            password = encode()

        elif option == '2':
            decoded_pass = decode(password)
            print(f'The encoded password is {password}, and the original password is {decoded_pass}.')
            print()

        elif option == '3':
            quit = True

        else:
            print('Invalid Input! Try again\n')