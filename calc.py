import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def equation(operation,first_number,second_number):
    if operation == "1":
        logging.info("Dodaję %d i %d" % (first_number,second_number))
        print(f"Wynik to {first_number + second_number}")
    elif operation == "2" :
        logging.info("Odejmuję %d i %d" % (first_number,second_number))
        print(f"Wynik to {first_number - second_number}")
    elif operation == "3" :
        logging.info("Mnożę %d i %d" % (first_number,second_number))
        print(f"Wynik to {first_number * second_number}")
    elif operation == "4" :
        logging.info("Dzielę %d przez %d" % (first_number,second_number))
        print(f"Wynik to {first_number / second_number}")
    else:
        logging.info("Niepoprawnie zdefiniowałeś działanie")

if __name__ == "__main__":
    
    while 3>0:
        operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
        if operation == "1" or operation == "2" or operation == "3" or operation == "4":
            break
        else:
            print("Niepoprawnie zdefiniowałeś działanie, to na prawdę proste - odszukaj na klawiaturze cyfry 1,2,3,4.")

    while 3>0:
        first_number = (input("Podaj składnik 1. "))
        try:
            float(first_number)
            first_number = float(first_number)
            break
        except:
            print("Nie wprowadzono poprawnie liczby, stać Cię na więcej...")
    
    while 4>0:
        second_number = (input("Podaj składnik 2. "))
        try:
            float(second_number)
            second_number = float(second_number)
            break
        except:
            print("Nie wprowadzono poprawnie liczby, spróbuj jeszcze raz i nie poddawaj się...")

    if operation == "4" and second_number == 0:
        print("Jesteś zdemoralizowany, chcesz dzielić przez zero!! Do widzenia")
        exit(1)

    equation(operation,first_number,second_number)