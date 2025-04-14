def transform_dictionary_to_sets():
    original_dict = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
    
    dict_keys = set(original_dict.keys())
    dict_values = set(original_dict.values())
    combined_set = dict_keys.union(dict_values)
    
    print(f"Множество ключей: {dict_keys}")
    print(f"Множество значений: {dict_values}")
    print(f"Объединение множества: {combined_set}")

transform_dictionary_to_sets()
