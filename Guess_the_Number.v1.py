import random

def Guess_the_Number():
    """
    Palyer must guess random number
    :return: "You win!"
    """
    random_number = random.randint(1, 100)
    print("Guess number 1 - 100.")
    while True:
        user_number = input("Your number: ")
        try:
# if input isn"t  int() print exception
            if int(user_number) == ValueError:
                break
            if int(user_number) == random_number:
                break
            elif int(user_number) > random_number:
                print("To big!")
            elif int(user_number) < random_number:
                print("To small!")
        except:
            print("Write number!")
    return "You win!"

print(Guess_the_Number())