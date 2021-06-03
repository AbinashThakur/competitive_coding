def get_element(value):
    dict_value = {}
    for i in range(len(value)):
        val = value[i]
        if dict_value.get(val):
            dict_value[val] += 1
        else:
            dict_value[val] = 1
    
    
    for key, value in dict_value.items():
        if value == 1:
            return key
        else:
            pass
        

x = [1, 1, 3, 3, 4, 4, 5, 5, 7, 7, 8, 8, 9]

print(get_element(x))