def print_menu():
    print("1. Pounds to kg.")
    print("2. kg to pound")

def kg_pound():
    kg = float(input('Please enter the weight in kilograms: '))
    pound = kg/0.45359237
    print(pound, 'pounds')
def pound_kg():
    pound = float(input('Please entr the weight in pound: '))
    kg = pound*0.45359237
    print(kg, 'kg')
if __name__ == '__main__':
    print_menu()
    choice = input('What do you want to do today?: ')
    if choice == '1':
        kg_pound()
    if choice == '2':
        pound_kg()