def print_menu():
    print('1. Kilometers ot miles')
    print('2. Miles to kilometers') 
    print('3. Celcious to farenheit')
    print('4.Faerenheit to celcious')
def km_miles():
    km = float((input("Please enter the length in kilometers: ")))
    miles = km/1.60934
    print('Length in miles {0}'.format(miles))
def miles_km():
    miles = float((input("Please enter the length in miles: ")))
    km = miles*1.60934
    print('Length in kolimeters {0}'.format(km))
def celcious_farenheit():
    celcious = float(input("Please enter the temperature in celcious: "))
    farenheit = celcious*9/5+32
    print('Temperature in farenheit {0}'.format(farenheit))
def farenheit_celcious():
    farenheit = float(input("Please enter the temperaure in farenheit: "))
    celcious = (farenheit - 32)*5/9
    print('Temperature in celcious {0}'.format(celcious))
if __name__ == '__main__':
    print_menu()
    choice = input('Which would you like to do today?: ')
    if choice == '1':
        km_miles()
    if choice == '2':
        miles_km()
    if choice == '3':
        celcious_farenheit()
    if choice == '4':
        farenheit_celcious()
