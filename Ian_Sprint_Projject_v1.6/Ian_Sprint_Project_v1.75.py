import random 
def print_menu():
    print('1. Kilometers to miles')
    print('2. Miles to kilometers') 
    print('3. Celcious to farenheit')
    print('4. Fahrenheit to celcius')
def km_miles():
    km = float((input("Please enter the length in kilometers: ")))
    miles = km/1.60934
    print('Length in miles {0}'.format(miles))
    print("Fun fact: ", random.choice(distance_facts))
def miles_km():
    miles = float((input("Please enter the length in miles: ")))
    km = miles*1.60934
    print('Length in kolimeters {0}'.format(km))
    print("Fun fact: ", random.choice(distance_facts))
def celcious_farenheit():
    celcius = float(input("Please enter the temperature in celcius: "))
    farenheit = celcius*9/5+32
    print('Temperature in farenheit {0}'.format(farenheit))
    print("Fun facts: ", random.choice(temperature_facts))
def farenheit_celcious():
    farenheit = float(input("Please enter the temperaure in farenheit: "))
    celcius = (farenheit - 32)*5/9
    print('Temperature in celcius {0}'.format(celcius))
    print("Fun fact: ", random.choice(temperature_facts))
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
temperature_facts = [
    "Earth's core is 9,392 F",
    "212 F is the boilling point of water",
    "The highest recorded temperature on Earth in dead Valley, california where it reahed 134 f"
]
distance_facts = [
    "The largest recorded flight of a chicken was 13 seconds.",
    "The largest street in the world is Yonge street in Toronto Canada measuring in 1896 km. ",
    "Cats can jump to 7 times their tail length"
]