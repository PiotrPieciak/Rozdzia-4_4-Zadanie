import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

#Funkcja dla operacji dodawania i mnożenia
def equation_multi_sum(operation,num_for_equ,result):
    if operation == "1":
        text_num_for_equ = ""
        for i in num_for_equ:
            text_num_for_equ = text_num_for_equ + str(i) + "   "
        logging.info(f"Dodaję liczby: {text_num_for_equ} ")
        for i in num_for_equ:
            result += i
        print(f"Wynik to {result}")
    else:
        text_num_for_equ = ""
        result = 1 
        for i in num_for_equ:
            text_num_for_equ = text_num_for_equ + str(i) + "   "
        logging.info(f"Mnożę liczby: {text_num_for_equ} ")
        for i in num_for_equ:
            result *= i
        print(f"Wynik to {result}")

#Funkcja dla operacji odejmowania i dzielenia
def equation_subtract_devide(operation,first_number,second_number):
    if operation == "2" :
        logging.info("Odejmuję %d i %d" % (first_number,second_number))
        print(f"Wynik to {first_number - second_number}")
    else:
        logging.info("Dzielę %d przez %d" % (first_number,second_number))
        print(f"Wynik to {first_number / second_number}")

#funkcja informująca o podaniu nieprawidłowej zmiennej
def wrong_number():
    print("Nie wprowadzono poprawnie liczby, spróbuj jeszcze raz. ")

#Funkcja pobierająca dane w przypadku odejmowania i dzielenia
def collect_numbers(text):
        while True:
            number = input(text)
            try:
                number = float(number)
                return number
            except:
                wrong_number()

#Początek głównego programu
if __name__ == "__main__":

    result = 0
    num_for_equ=[]
#Prosimy uzytkownika o zdefiniowanie rodaju operacji + - * /
    while True:
        operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
        if  operation in ["1" ,"2" , "3" , "4"]:
            break
        else:
            wrong_number()

# Dla Operacji Dodawania i mnożenia użyjemy osobnej funkcji gdyż wymagają zmiennej ilości składników.
    if operation in ["1","3"]:
        while True:
            count_number = input("Podaj liczbę składników których chesz uzyć do zdefiniowanego działania: ")
            try:
                count_number = int(count_number)
                if count_number < 2:
                    print("liczba składników do wykonania zadanego diałania to min 2.")
                else:    
                    break
            except:
                wrong_number()
        for i in range(count_number):
            while True:
                num_for_equ.append(input("Podaj %d z %d liczb która będzie użyta do zdefiniowanego działania: " % (i+1,count_number)))
                try:
                    num_for_equ[i] = float(num_for_equ[i])
                    break
                except:
                    wrong_number()
                    del num_for_equ[i]
        #Uruchamiamy fucnkcę wyłącznie dla przypadku mnożenia lub dodawania
        equation_multi_sum(operation,num_for_equ,result)
        
# Dla operacji odejmowania i dzielenia użyjemy prostszej funkcji, gdyż wymagają jedynie 2 argumentów
    else:
        first_number = collect_numbers("Podaj pierwszą liczbę: ")
        #Obsługa przypadku dzielenia przez zero i pobranie drugiej zmiennej
        while True:
            second_number = collect_numbers("Podaj drugą liczbę: ")
            if second_number != 0:
                break
            else:
                wrong_number()
    
        #Uruchamiamy funkcję wyłącznie dla przypadku dzielenia lub odejmowania
        equation_subtract_devide(operation,first_number,second_number)



       