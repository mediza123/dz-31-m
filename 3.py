def find_common_elements():
    first_number_list = list(map(int, input("Введите первый список: ").split()))
    second_number_list = list(map(int, input("Введите второй список: ").split()))
    
    first_number_set = set(first_number_list)
    second_number_set = set(second_number_list)
    common_elements = first_number_set & second_number_set
    
    print("Общие элементы:", " ".join(map(str, sorted(common_elements))))

find_common_elements()
