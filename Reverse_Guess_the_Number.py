def reverse_guess_the_number():
    """
    Computer will try guess your number.
    :return:
    """
    print("Choose in Your mind  number from 1 to 1000 and i guess your number.")
    min_number = 0
    max_number = 1000
    while True:
            guess = int((max_number - min_number + 1)) / 2 + min_number
            print(f"Guess is {int(guess)}")
            answer = input("""Type 1, 2 or 3 if number is:
                    1 - to big 
                    2 - to small
                    3 - right answer
                    Write number:
                    """)
            try:
#If input() isn"t int() program run exception: ValueError
                if int(answer) == ValueError:
                    break
                elif int(answer) == 3:
                    break
                elif int(answer) == 1:
                    max_number = guess
                elif int(answer) == 2:
                    min_number = guess
                else:
                    print("Write number 1, 2 or 3.")
            except ValueError:
                print("Write number 1, 2 or 3.")
    return "I win!"


print(reverse_guess_the_number())
