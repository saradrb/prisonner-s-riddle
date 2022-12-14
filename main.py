from strategy import Strategy
from window import open_window
from randomStrategy import random_for_group_of_prisoner
from followStrategy import follow_for_group_of_prisoner, create_graph
from babyStepGiantStepStrategy import baby_step_giant_step_for_group_of_prisoner
from permutation import create_drawers
from histogram import how_many_tries_to_solve_strategy

def ask_histogram(strategy_name) :
    while (1) :
        print("Voulez-vous effectuer l'énigme plusieurs fois afin d'obtenir un histogramme à la fin ? [Y/N]")
        histogram = input().upper()
        if (histogram == "Y" or histogram == "N") : break
        else : print("Veuillez entrer [Y] ou [N].")
            
    if (histogram == "N") :
        return False
    else :
        while (1) :
            print("Combien de fois voulez-vous effectuer l'énigme ? (Attention : plus ce nombre est élevé et plus l'éxécution prend du temps)")
            try :
                no_repetition = int(input())
                break
            except :
                print("Veuillez entrer un nombre.")
        how_many_tries_to_solve_strategy(strategy_name, no_prisoner, print_msg, no_repetition)
        return True


if __name__ == '__main__' :
    print("Bienvenue dans le simulateur de l'énigme des 100 prisonniers.")

    while (1) :
        print("Que voulez-vous faire ?")
        print("   - Voir le détaillé d'une solution. [D]")
        print("   - Voir la probabilité de succès des différentes solutions. [P]")
        action = input().upper()
        if (action == "D" or action == "P") : break
        else : print("Veuillez entrer [D] ou [P].")

    if (action == "P") :
        open_window()
    else :
        while (1) :
            print("Quel solution voulez-vous effectuer ?")
            print("  - Stratégie aléatoire [A]")
            print("  - Statégie suivre [S]")
            print("  - Stratégie baby-step giant-step [B]")
            strategy = input().upper()
            if (strategy == "A" or strategy == "S" or strategy == "B") : break
            else : print("Veuillez entrer [A], [S] ou [B].")

        while (1) :
            print("Sur combien de prisonniers voulez-vous effectuer l'énigme ?")
            try :
                no_prisoner = int(input())
                break
            except :
                print("Veuillez entrer un nombre.")
        
        while (1) :
            print("Voulez vous afficher le détail de la solution ? [Y/N]")
            detail = input().upper()
            if (detail == "Y" or detail == "N") : break
            else : print("Veuillez entrer [Y] ou [N].")
        
        if (detail == "Y") : print_msg = True
        else : print_msg = False

        if (strategy == "A") :
            if (not ask_histogram(Strategy.RANDOM)) :
                random_for_group_of_prisoner(len, print_msg)

        elif (strategy == "S") :
            if (not ask_histogram(Strategy.FOLLOW)) :
                drawers = create_drawers(no_prisoner)
                follow_for_group_of_prisoner(drawers, no_prisoner, print_msg)
                while (1) :
                    print("Voulez-vous afficher le graphe des permutations rencontré ? [Y/N]")
                    permutationGraph = input().upper()
                    if (permutationGraph == "Y" or permutationGraph == "N") : break
                    else : print("Veuillez entrer [Y] ou [N]")

                if (permutationGraph == "Y") : create_graph(drawers, no_prisoner)

        else :
            if (not ask_histogram(Strategy.BABY_STEP_GIANT_STEP)) :
                baby_step_giant_step_for_group_of_prisoner(no_prisoner, print_msg)

