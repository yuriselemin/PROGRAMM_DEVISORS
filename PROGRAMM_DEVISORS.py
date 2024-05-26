# Функция для проверки, является ли число простым

simple_numbers = []
composite_numbers = []


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# Функция для вывода всех делителей числа
def print_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    print(divisors)


# Основная программа
while True:
    # Ввод числа пользователем
    number = int(input("Введите число: "))

    # Проверка на простое число
    if is_prime(number):
        print(f"Число {number} является простым.")
        print_divisors(number)
        simple_numbers.append(number)
    else:
        print(f"Число {number} является составным.")
        print_divisors(number)
        composite_numbers.append(number)

    continue





def continue_program():
    answer = input("Хотите ввести еще одно число? (y/n): ")
    if answer == 'y':
        return True
    elif answer == 'n':
        return False
    else:
        print("Неверный ответ. Попробуйте снова.")
        return continue_program()






