import random

def create_permutation(n):
    i = 1
    x = []
    while (i <= n):
        x = x + [i]
        i += 1
    random.shuffle(x)
    return x

def create_drawers(n):
    i = 1
    tab = create_permutation(n)
    drawers = {}
    for i, j in enumerate(tab):
        drawers[i + 1] = j
    return drawers