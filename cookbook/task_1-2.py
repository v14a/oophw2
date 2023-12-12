with open('cookbook/recipes.txt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        title = line.strip()
        component = int(f.readline())
        components_list = []
        for item in range(component):
            component_dict = {} 
            ingredient_name, quantity, measure = f.readline().split('|')
            component_dict['ingredient_name'] = ingredient_name.strip()
            component_dict['quantity'] = int(quantity.strip())
            component_dict['measure'] = measure.strip()
            components_list.append(component_dict)
            cook_book[title] = components_list
        f.readline()
    
def get_shop_list_by_dishes(dishes, person_count):
    shoping_list = {}
    for dish in dishes:
        if dish in cook_book:
                component = cook_book.get(dish)
                for ingredient in component:
                    measure_dict = {}
                    count = ingredient['quantity'] * person_count
                    if ingredient['ingredient_name'] in shoping_list.keys():
                        count += count
                    measure_dict['measure'] = ingredient['measure']
                    measure_dict['quantity'] = count
                    shoping_list[ingredient['ingredient_name']] = measure_dict
        else:
            print(f'{dish}: рецепт не найден')
    return shoping_list