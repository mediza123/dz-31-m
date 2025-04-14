def calculate_powered_elements():
    user_input_elements = input("Введите числа через пробел: ").split()
    exponent = int(input("Введите степень: "))
    
    powered_elements = []
    for item in user_input_elements:
        try:
            number = int(item)
            powered_elements.append(str(number ** exponent))
        except ValueError:
            powered_elements.append(item * exponent)
    
    print("Вывод:", " ".join(powered_elements))

calculate_powered_elements()
