def user():
    numbers = 0
    my_list = []
    while numbers < 6:
        try:
            my_list.append(int(input(f"Podaj {numbers+1} liczbę: ")))
            numbers += 1
        except ValueError:
            print("To nie jest liczba")
    print(my_list)
user()
