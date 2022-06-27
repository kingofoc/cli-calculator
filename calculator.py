#Created by Chukwuebuka Kingsley
#Simple CLI Calculator Program

calc_guide = ('''
    Operations
    + for addition
    - for subtraction
    * for multiplictaion
    / for division
    % for modulus
    quit for switching off
    ''') #a variable that stores the option a user enters

print (calc_guide)

while True:
    choice = input('Enter an operation: ')

    if choice == 'quit':
        print ('The calculator is off')
        
        break
    elif choice != '+' and choice != '-' and choice != '*' and choice != '/' and choice != '%':
        print(f'{choice} is not a valid operation')
        
    else:
        fnum = int(input("Enter First Number: ")) #gets the first number from the user and stores in the variable 'fnum'
        snum = int(input("Enter Second Number: ")) #gets the second number from the user and stores in the variable 'snum'
    
    if choice == '+':
        print(f"{fnum} + {snum} = {fnum + snum}")
    elif choice == '-':
        print(f'{fnum} - {snum} =', fnum - snum)
    elif choice == '*':
        print(f'{fnum} * {snum} =', fnum * snum)
    elif choice == '/':
        if snum == (0):
            print (f'Error: {snum} is not divisible!')
        else:
            print(f'{fnum} / {snum} =', fnum / snum)
    elif choice == '%':
        if snum == (0):
            print (f'Error: {snum} is not divisible!')
        else:
            print(f'{fnum} % {snum} =', fnum % snum)
