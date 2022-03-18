print('Hello, How are you?')
print('Wanna play a game?')
print('I can guess your number between 0 & 500.')
while True:
    yes_no = input('To start the game press any button. ')
    print('Now think of a number between 0 and 500')
    epsilon = 500
    high = 500
    low = 0
    num_guesses = 0
    guess = int(high + low) / 2.0
    print('Is your number', guess, '?')
    while guess <= epsilon:
        choice = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

        if choice == 'h':
            high = guess
            guess = int(high + low) / 2.0
            print('Is your number', guess, '?')
        elif choice == 'l':
            low = guess
            guess = int(high + low) / 2.0
            print('Is your number', guess, '?')
        elif choice == 'c':
            print('HAHA Got you:)')
            break
        else:
            print('Wrong choice mate')
    break










