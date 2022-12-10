from math import ceil, sqrt
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


#Entrée: un groupe cyclique G d'ordre n, ayant un générateur g et un élément h.
def babystepgiantstep(g, h, n):
    #m ← [√n]+1
    m = ceil(sqrt(n)) + 1

    #Pour j tel que 0 ≤ j < m:    //Baby-Step
    #Calculer gj et sauvegarder la paire (j, gj), par exemple dans une table de hachage. 
    tbl = {pow(g, j, n): j for j in range(m)}

    #Calculer g−m (l'inverse de gm ou encore gn - m). 
    c = pow(g, m * (n - 2), n)

    #Pour i tel que 0 ≤ i < m:   //Giant-Step
    #Vérifier si 𝛾 est le second composant (gj) d'une paire quelconque dans la table.
    #Si oui, retourner im + j.
    #Si non, 𝛾 ← 𝛾 • g−m.
    for i in range(m):
        y = (h * pow(c, i, n)) % n
        if y in tbl:
            return i * m + tbl[y]

    # Solution not found
    return None
#Sortie: une valeur x vérifiant g^x = h ou None si rien trouvé

def baby_step_giant_step_revisité(g, n, tab):
    m = ceil(sqrt(n)) + 1
    tbl = []
    #baby step
    for j in range(m):
        tbl = tbl + [pow(g, j, n)]
    for j in range(m):
        if tbl[j] not in tab:
            return tbl[j]
    return None

    
    

def do_baby_step_giant_step_one_case(tab, number, bool):
    x = 0
    rand = []
    while (x < len(tab)/2):
        temp_numb = 0
        temp = baby_step_giant_step_revisité(number + temp_numb + x,len(tab),rand)
        while (temp == None):
            temp_numb += 1
            temp = baby_step_giant_step_revisité(number + temp_numb + x,len(tab),rand)
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

def case_bsgs_for_a_group_of_prisonner(len, bool):
    tab = create_tab(len)
    x = 0
    while (x < len):
        if (do_baby_step_giant_step_one_case(tab, x + 1, bool) == False):
            if bool:
                print("La stratégie babystep giant step à echoué au bout du " + str(x + 1) + "prisonnier(s)")
                time.sleep(0.1)
            return False
        x += 1
    if bool:
        print("La stratégie babystep giant step à marcher pour les " + str(len) + "prisonniers")
        time.sleep(0.1)
    return True

def create_histograme(number_of_try, tab_result):
    left = [0,number_of_try]
    tick_label = ['failed', 'success']

    plt.bar(left, tab_result, tick_label = tick_label, width= 50, color = ['red', 'green'])
    plt.xlabel('result')
    plt.ylabel('try')
    plt.title('Baby Step Giant Step Strat')
    plt.show()

def how_many_try_to_resolve_the_case_bsgs(len, bool, trytest):
    j = 0
    i = 0
    k = 0
    while (k < trytest):
        if (case_bsgs_for_a_group_of_prisonner(len, bool) == False):
            i += 1
        else:
            j+= 1
        k += 1
    create_histograme(trytest, [i,j])
    
def bsgs_strat():
    print("Bonjour voici une implementation  de la méthode babystep giant step de résolution,veuillez choisir sur combien de prisonnier vous voulez la faire ")
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
        how_many_try_to_resolve_the_case_bsgs(number, choice, trytest)
    else:
        print(case_bsgs_for_a_group_of_prisonner(number, choice))
bsgs_strat()