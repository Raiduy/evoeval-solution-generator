
def compare(game, guess):
    return [abs(g - gs) for (g, gs) in zip(game, guess)]