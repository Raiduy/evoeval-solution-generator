def potion_mixing(potions, target):
    potions = [(potion.split()[0], int(potion.split()[1])) for potion in potions]
    potions.sort(key=lambda x: (x[1], x[0]))
    result = []
    for potion in potions:
        if sum((p[1] for p in result)) + potion[1] <= target:
            result.append(potion)
        if sum((p[1] for p in result)) == target:
            return [p[0] + ' ' + str(p[1]) for p in sorted(result, key=lambda x: (x[1], x[0]))]
    return []