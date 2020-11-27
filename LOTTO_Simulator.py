import random


def user():
    """Create list with user numbers"""
    numbers = 0
    my_list = []
    while numbers < 6:
        try:
            user_num = int(input(f"Podaj {numbers+1} liczbę: "))
            if user_num in range(1, 50):
                if user_num not in my_list:
                    my_list.append(user_num)
                    numbers += 1
                else:
                    print("Liczba została już wybrana")
            else:
                print("Podaj liczbę z przedziału 1 - 49")
        except ValueError:
            print("To nie jest liczba")
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
        print(f"Niestety nie trafiłeś żadnej liczby")
    elif compare == 1:
        print("Trafiłeś jedynie 1 liczbę")    
    elif compare == 2:
        print("Trafiłeś jedynie 2 liczby")    
    elif compare == 3 or compare == 4:
        print("Gratulacje, trafiłeś {compare} liczby!")
    elif compare == 5:
        print("Gratulacje, trafiłeś {compare} liczb!")
    elif compare == 6:
        print("Gratulacje, trafiłeś wszystkie liczby!")


computer()
