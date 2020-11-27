import random


def user():
    """Create list with user numbers"""
    numbers = 0
    my_list = []
    while numbers < 6:
        try:
            user_num = int(input(f"Please put {numbers+1} number: "))
            if user_num in range(1, 50):
                if user_num not in my_list:
                    my_list.append(user_num)
                    numbers += 1
                else:
                    print("Number is already taken")
            else:
                print("Please put number in range 1-49")
        except ValueError:
            print("It is not integer")
    my_list.sort()
    return my_list


def computer():
    """Create computer numbers and compare"""
    user_list = user()
    com_numbers = 0
    com_list = []
    while com_numbers < 6:
        com_num = random.randint(1, 49)
        if com_num not in com_list:
            com_list.append(com_num)
            com_numbers += 1
    com_list.sort()
    print(user_list)
    print(com_list)
    compare = len(set(user_list) & set(com_list))
    if compare == 0:
        print(f"Unfortunetly you did not guess any number")
    elif compare == 1:
        print("You guessed 1 number")    
    elif compare == 2:
        print("You guessed 2 numbers")    
    elif compare == 3 or compare == 4:
        print("Congratulations! You guessed {compare} numbers!")
    elif compare == 5:
        print("Congratulations! You guessed {compare} numbers!")
    elif compare == 6:
        print("Congratulations! You guessed all numbers!")


computer()
