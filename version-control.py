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

def decode():
    pass

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
            decode()

        elif option == '3':
            quit = True

        else:
            print('Invalid Input! Try again\n')