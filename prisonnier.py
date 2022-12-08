import random
import time
import matplotlib.pyplot as plt


def create_tab(n):
    i = 1
    x = []
    while (i <= n):
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
            temp = random.randint(1, len(tab))
        rand = rand + [temp]
        if (tab[temp] == number):
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
        if (case_random_for_one_prisonner(tab, x + 1, bool) == False):
            if bool:
                print("La stratégie aléatoire à echoué au bout du " + str(x + 1) + "prisonnier(s)")
                time.sleep(0.1)
            return False
        x += 1
    if bool:
        print("La strateégie aléatoire à marcher pour les " + str(len) + "prisonniers")
        time.sleep(0.1)
    return True
def create_histograme(number_of_try, tab_result):
    left = [0,number_of_try]
    tick_label = ['failed', 'success']

    plt.bar(left, tab_result, tick_label = tick_label, width= 50, color = ['red', 'green'])
    plt.xlabel('result')
    plt.ylabel('try')
    plt.title('Prisonners Random Strat')
    plt.show()

def how_many_try_to_resolve_the_case_random(len, bool, trytest):
    j = 0
    i = 0
    k = 0
    while (k < trytest):
        if (case_random_for_a_group_of_prisonner(len, bool) == False):
            i += 1
        else:
            j+= 1
        k += 1
    create_histograme(trytest, [i,j])

def random_strat():
    print("Bonjour voici une implementatio de la méthode random de résolution,veuillez choisir sur combien de prisonnier vous voulez la faire")
    print("tapez votre nombre")
    number = int(input())
    print("Vous avez choisi " + str(number) + " voulez vous voir le déroulez avec les différents affichage ?")
    print("PS: au dessus de 20 prisonnier cela peux prendre des millions d'éssais avant une reussite, l'affichage pourrait tout ralentir")
    print("[y/n]")
    choice = str(input())
    print("Voulez vous faire plusieurs essaie pour obtenir un graphe ? (attention si vous avez mis un trop gros nombre le graphe peut prendre très longtemps à s'afficher)")
    print("[y/n]")
    choice2 = str(input())

    if (choice == 'y' or choice == 'Y'):
        choice = True
    else:
        choice = False

    if (choice2 == 'y' or choice2 == 'Y'):
        print("Combien d'essais ?")
        trytest = int(input())
        how_many_try_to_resolve_the_case_random(number, choice, trytest)
    else:
        print(case_random_for_a_group_of_prisonner(number, choice))

random_strat()

