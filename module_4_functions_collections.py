import random

## Generate source dictionary
def generate_dictionary(some_params, num, max):
    element_params = random.sample(some_params, num)
    dict_item = {}
    for element in element_params:
        dict_item[element] = random.randint(0, max)
    return dict_item

## Keys for dictionaries
params = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'n', 'm']

new_list = []
for i in range(0, 4):
    # Dictionaries  Generating
    new_list.append(generate_dictionary(params, 5, 100))
print(new_list)

def result_dict():
    result_dict = {}

    for key in params:
        # This comment belongs to 3 rows below for better understanding.Check if my list has a dictionary with the key value
        max_value = None
        for dict_item in new_list:
            if key in dict_item:
                # Save the index of the dictionary with the maximum key value
                if max_value is None:
                    max_value = new_list.index(dict_item)
                else:
                    if dict_item[key] > new_list[max_value][key]:
                        max_value = new_list.index(dict_item)
        # Add item to the resulting list if a key is in the new_list at least once
        if max_value is not None:
            result_dict[key + '_' + str(max_value)] = new_list[max_value][key]
    return result_dict


print(result_dict())

