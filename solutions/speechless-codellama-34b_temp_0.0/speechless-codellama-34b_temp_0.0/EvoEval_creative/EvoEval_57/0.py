def magical_cafe(menu, magic_spell):
    new_menu = {}
    for (dish, price) in menu.items():
        new_dish = ''
        for i in range(len(dish)):
            new_dish += magic_spell[i % len(magic_spell)]
        new_menu[new_dish] = price
    return new_menu