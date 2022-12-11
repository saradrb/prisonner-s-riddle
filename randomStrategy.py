import random
import time
from permutation import create_permutation

def random_for_one_prisoner(permutation, number, print_msg):
    x = 0
    rand = []
    temp = random.randint(0, len(permutation))
    while (x < len(permutation)/2):
        while temp in rand:
            temp = random.randint(1, len(permutation))
        rand = rand + [temp]
        if (permutation[temp - 1] == number):
            if print_msg:
                print("Le prisonier n°" + str(number) + " a trouvé son numéro dans le tiroir n°" + str(temp) + " au bout de "+ str(x)+" essais.")
                time.sleep(0.1)
            return True
        x += 1
    if print_msg:
        print("Après " + str(x) + " essais, le prisonnier n°" + str(number) + " n'a pas trouvé son numéro dans un tiroir.")
        time.sleep(0.1)
    return False

def random_for_group_of_prisoner(len, print_msg):
    tab = create_permutation(len)
    x = 0
    while (x < len):
        if (random_for_one_prisoner(tab, x + 1, print_msg) == False):
            if print_msg:
                print("La stratégie aléatoire a échoué au bout de " + str(x + 1) + " prisonniers.\n")
                time.sleep(0.1)
            return False
        x += 1
    if print_msg:
        print("Victoire! La stratégie aléatoire est un succès, tous les prisonniers ont trouvé leur numéro!\n")
        time.sleep(0.1)
    return True