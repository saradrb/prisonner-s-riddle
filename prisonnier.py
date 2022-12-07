import random
import time


def create_tab(n):
    i = 0
    x = []
    while (i < n):
        x = x + [i]
        i += 1
    random.shuffle(x)
    return x

def case_random_for_one_prisonner(tab, number, bool):
    x = 0
    rand = []
    temp = random.randint(0, len(tab))
    while (x < len(tab)/2):
        while temp in rand:
            temp = random.randint(0, len(tab))
        rand = rand + [temp]
        if (tab[temp - 1] == number):
            if bool:
                print("le prisonnier numéro " + str(number) + " a trouver son nombre dans le tirroir numéro " + str(temp) + " au de "+ str(x)+" essais")
                time.sleep(0.1)
            return True
        x += 1
    if bool:
        print("après 50 essais le prisonnier numéro " + str(number) + " n'a pas trouver son numéro dans un tiroir")
        time.sleep(0.1)
    return False

def case_random_for_a_group_of_prisonner(len, bool):
    tab = create_tab(len)
    x = 0
    while (x < len):
        if (case_random_for_one_prisonner(tab, x, bool) == False):
            if bool:
                print("La stratégie aléatoire à echoué au bout du " + str(x + 1) + "prisonnier(s)")
                time.sleep(0.1)
            return False
        x += 1
    if bool:
        print("La strateégie aléatoire à marcher pour les " + str(len) + "prisonniers")
        time.sleep(0.1)
    return True

def how_many_try_to_resolve_the_case_random(len, bool):
    i = 0
    while (case_random_for_a_group_of_prisonner(len, bool) == False):
        i += 1
    return i
print("Bonjour voici une implementatio de la méthode random de résolution,veuillez choisir sur combien de prisonnier vous voulez la faire")
print("tapez votre nombre")
number = int(input())
print("Vous avez choisi " + str(number) + " voulez vous voir le déroulez avec les différents affichage ?")
print("PS: au dessus de 20 prisonnier cela peux prendre des millions d'éssais avant une reussite, l'affichage pourrait tout ralentir")
print("[y/n]")
choice = str(input())

if (choice == 'y' or choice == 'Y'):
    print(case_random_for_a_group_of_prisonner(number, True))
else: 
    print(case_random_for_a_group_of_prisonner(number, False))
