import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def equation(operation,first_number,second_number,num_for_equ,result):
    if operation == "1":
        logging.info(f"Dodaję liczby: {num_for_equ} ")
        for i in num_for_equ:
            result += i
        print(f"Wynik to {result}")
    elif operation == "2" :
        logging.info("Odejmuję %d i %d" % (first_number,second_number))
        print(f"Wynik to {first_number - second_number}")
    elif operation == "3" :
        result = 1 
        logging.info(f"Mnożę liczby: {num_for_equ} ")
        for i in num_for_equ:
            result *= i
        print(f"Wynik to {result}")
    elif operation == "4" :
        logging.info("Dzielę %d przez %d" % (first_number,second_number))
        print(f"Wynik to {first_number / second_number}")
    else:
        logging.info("Niepoprawnie zdefiniowałeś działanie")

if __name__ == "__main__":

    result = 0
    num_for_equ=[]
    while 3>0:
        operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
        if operation == "1" or operation == "2" or operation == "3" or operation == "4":
            break
        else:
            print("Niepoprawnie zdefiniowałeś działanie, to na prawdę proste - odszukaj na klawiaturze cyfry 1,2,3,4.")

    if operation == "1" or operation =="3":
        while 4>0:
            count_number = input("Podaj liczbę składników których chesz uzyć do zdefiniowanego działania: ")
            try:
                int(count_number)
                count_number = int(count_number)
                if count_number < 2:
                    print("liczba składników do wykonania zadanego diałania to min 2.")
                else:    
                    break
            except:
                print("Nie wprowadzono poprawnie liczby składników zdefiniowanego działania. Napisz dla ilu liczb chcesz wykonać dodawanie lub mnożenie.")
        for i in range(count_number):
            while 3>0:
                num_for_equ.append(input("Podaj %d z %d liczb która będzie użyta do zdefiniowanego działania: " % (i+1,count_number)))
                try:
                    float(num_for_equ[i])
                    num_for_equ[i] = float(num_for_equ[i])
                    break
                except:
                    print("Nie wprowadzono poprawnie liczby, stać Cię na więcej...")
                    del num_for_equ[i]
        first_number = 0
        second_number = 0
    else:
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
        num_for_equ=0
        result=0

    equation(operation,first_number,second_number,num_for_equ,result)