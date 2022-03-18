def get_dict(strings):
    dictionary = {}
    for string in strings:
        lines = string.split("\n")
        s = []
        for item in lines[2:]:
            d = {}
            ing = item.split("|")
            d['ingredient_name'] = ing[0]
            d['quantity'] = ing[1]
            d['measure'] = ing[2]
            s.append(d)
        dictionary[lines[0]] = s
    return dictionary


def get_shop_list_by_dishes(dishes, person_count: int, cook_book_):
    shop_list_ = {}
    for dish in dishes:
        for ingridient in cook_book_[dish]:
            shop_list_.setdefault(ingridient['ingredient_name'], {'measure': None, 'quantity': 0})
            shop_list_[ingridient['ingredient_name']] = {'measure': ingridient["measure"],
                        'quantity': (int(shop_list_[ingridient['ingredient_name']]['quantity']) + int(
                                        ingridient['quantity']) * person_count)}
    return shop_list_


with open('recipes.txt') as file:
    text = file.read().split("\n\n")[:-1]

cook_book = get_dict(text)
print(cook_book)
print('__________________________________________')

shop_list = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2, cook_book)
print(shop_list)
