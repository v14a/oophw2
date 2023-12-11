with open('recipes.txt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        title = line.strip()
        component = int(f.readline())
        components_list = []
        for l in range(component):
            component_dict = {}
            ingredient_name, quantity, measure = f.readline().split('|')
            component_dict['ingredient_name'] = ingredient_name.strip()
            component_dict['quantity'] = quantity.strip()
            component_dict['measure'] = measure.strip()
            components_list.append(component_dict)
            cook_book[title] = components_list
        f.readline()