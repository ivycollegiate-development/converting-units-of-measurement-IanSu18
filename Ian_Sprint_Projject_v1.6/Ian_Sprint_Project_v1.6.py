def print_menu():
    print()
    print()
def km_miles():
    km = float((input("Please enter the length in kilometers: ")))
    miles = km/1.60934
    print('Length in miles {0}'.format(miles))
def miles_km():
    miles = float((input("Please enter the length in miles: ")))
    km = miles*1.60934
    print('Length in kolimeters {0}'.format(km))

if __name__ == '__main__':
    print_menu()
    choice = input('Which would you like to do today?: ')
    if choice == '1':
        km_mile()
    if choice == '2':
        miles_km()

