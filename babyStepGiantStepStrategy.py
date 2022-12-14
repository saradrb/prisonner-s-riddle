from math import ceil, sqrt
import time
from permutation import create_permutation

# #(source: Wikipedia)
# #Entrée: un groupe cyclique G d'ordre n, ayant un générateur g et un élément h.
# def baby_step_giant_step(g, h, n):
#     #m ← [√n]+1
#     m = ceil(sqrt(n)) + 1

#     #Pour j tel que 0 ≤ j < m:    //Baby-Step
#     #Calculer gj et sauvegarder la paire (j, gj), par exemple dans une table de hachage. 
#     tbl = {pow(g, j, n): j for j in range(m)}

#     #Calculer g−m (l'inverse de gm ou encore gn - m). 
#     c = pow(g, m * (n - 2), n)

#     #Pour i tel que 0 ≤ i < m:   //Giant-Step
#     #Vérifier si 𝛾 est le second composant (gj) d'une paire quelconque dans la table.
#     #Si oui, retourner im + j.
#     #Si non, 𝛾 ← 𝛾 • g−m.
#     for i in range(m):
#         y = (h * pow(c, i, n)) % n
#         if y in tbl:
#             return i * m + tbl[y]

#     # Solution not found
#     return None
# #Sortie: une valeur x vérifiant g^x = h ou None si rien trouvé

def baby_step_giant_step_revisited(g, n, tab):
    m = ceil(sqrt(n)) + 1
    tbl = []
    # baby step
    for j in range(m):
        tbl = tbl + [pow(g, j, n)]
    for j in range(m):
        if tbl[j] not in tab:
            return tbl[j]
    return None

def baby_step_giant_step_for_one_prisoner(permutation, number, print_msg):
    x = 0
    rand = []
    while (x < len(permutation) / 2):
        tempNum = 0
        temp = baby_step_giant_step_revisited(number + tempNum + x,len(permutation), rand)
        while (temp == None):
            tempNum += 1
            temp = baby_step_giant_step_revisited(number + tempNum + x,len(permutation), rand)
        rand = rand + [temp]
        if (permutation[temp] == number):
            if print_msg:
                print("Le prisonier n°" + str(number) + " a trouvé son numéro dans le tiroir n°" + str(temp) + " au bout de "+ str(x)+" essais.")
                time.sleep(0.1)
            return True
        x += 1
    if print_msg:
        print("Après " + x + " essais, le prisonnier n°" + str(number) + " n'a pas trouvé son numéro dans un tiroir.")
        time.sleep(0.1)
    return False

def baby_step_giant_step_for_group_of_prisoner(len, print_msg):
    tab = create_permutation(len)
    x = 0
    while (x < len):
        if (baby_step_giant_step_for_one_prisoner(tab, x + 1, print_msg) == False):
            if print_msg:
                print("La stratégie baby-step giant-step a échoué au bout de " + str(x + 1) + " prisonniers.")
                time.sleep(0.1)
            return False
        x += 1
    if print_msg:
        print("Victoire! La stratégie baby-step giant-step est un succès, tous les prisonniers ont trouvé leur numéro!")
        time.sleep(0.1)
    return True