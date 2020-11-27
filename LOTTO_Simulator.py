# def user():
#     numbers = 0
#     my_list = []
#     while numbers < 6:
#         try:
#             my_list.append(int(input(f"Podaj {numbers+1} liczbę: ")))
#             numbers += 1
#         except ValueError:
#             print("To nie jest liczba")
#     return my_list

def compare():
    numbers = 0
    my_list = []
    while numbers < 6:
        try:
            a = int(input(f"Podaj {numbers+1} liczbę: "))
            if a in range(1, 50) and a not in my_list:
                my_list.append(a)
                numbers += 1
            else:
                print("Podaj liczbę z przedziału 1 - 49")
        except ValueError:
            print("Proszę podać liczbę: ")
    print(my_list)


compare()
