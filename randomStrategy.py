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

# def create_histogram(number_of_try, tab_result):
#     left = [0,number_of_try]
#     tick_label = ['fails', 'success']

#     plt.bar(left, tab_result, tick_label = tick_label, width = 50, color = ['red', 'green'])
#     plt.xlabel('Results')
#     plt.ylabel('Number of tries')
#     plt.title('Prisonners Random Strat')
#     plt.show()

# def how_many_tries_to_solve_random(len, print_msg, trytest):
#     j = 0
#     i = 0
#     k = 0
#     while (k < trytest):
#         if (random_for_group_of_prisoner(len, print_msg) == False):
#             i += 1
#         else:
#             j+= 1
#         k += 1
#     create_histogram(trytest, [i, j])

# def randomStrat():
#     print("Bonjour, voici une implémentation de la stratégie random, veuillez choisir le nombre de prisonniers voulu :")
#     number = int(input())
#     print("Vous avez choisi " + str(number) + ". Voulez-vous voir le déroulé avec les différents affichage ?")
#     print("PS: au dessus de 20 prisonniers, cela peux prendre des millions d'essais avant une reussite, l'affichage pourrait tout ralentir. [y/n]")
#     choice = str(input())
#     print("Voulez vous faire plusieurs essais pour obtenir un graphe ? (Attention : si vous avez mis un trop gros nombre le graphe peut prendre très longtemps à s'afficher) [y/n]")
#     choice2 = str(input())

#     if (choice.lower() == 'y'):
#         choice = True
#     else:
#         choice = False

#     if (choice2.lower() == 'y'):
#         print("Combien d'essais ?")
#         trytest = int(input())
#         #how_many_tries_to_solve_random(number, choice, trytest)
#     else:
#         print(random_for_group_of_prisoner(number, choice))

#random_strat()