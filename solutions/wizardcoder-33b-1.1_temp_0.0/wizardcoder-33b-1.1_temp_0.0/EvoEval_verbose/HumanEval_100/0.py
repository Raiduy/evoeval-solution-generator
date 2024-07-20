
def make_a_pile(n):
    pile = [n]
    while n > 1:
        if n % 2 == 0:
            n = n + 2
        else:
            n = n + 1
        pile.append(n)
    return pile