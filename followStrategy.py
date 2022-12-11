
import pandas as pd
import time
import networkx as nx
import matplotlib.pyplot as plot
import seaborn as sb
from permutation import *

def follow_for_one_prisoner(drawers, number_p, print_msg):
    bool = False
    tries = 0
    opened_drawers = []
    num_drawer = number_p
    while(tries < (len(drawers) / 2) and not(bool)):
        opened_drawers += [num_drawer]
        if (drawers[num_drawer] == number_p):
            bool = True
        else:
            num_drawer = drawers[num_drawer]
        tries += 1   

    if print_msg :
        if bool:
            print("Le prisonnier n°" + str(number_p) + " a trouvé son numéro dans le tiroir n°" + str(num_drawer) + " au bout de " + str(tries) + " essais.")
            time.sleep(0.1)
        else:
            print("Après " + str(tries) + " essais, le prisonnier n°" + str(number_p) + " n'a pas trouvé son numéro dans un tiroir.")
            time.sleep(0.1)
    return bool    

def follow_for_group_of_prisoner(drawers, len, print_msg):
    prisoner = 1
    win = False
    
    while(prisoner <= len):
        bool = follow_for_one_prisoner(drawers, prisoner, print_msg)
        if bool:
            prisoner += 1
        else:
            if print_msg:
                print("La stratégie suivre a echoué au bout de " + str(prisoner) + " prisonniers.\n")
            return win
    if bool:
        win = True
        if print_msg:
            print("Victoire! La stratégie suivre est un succès, tous les prisonniers ont trouvé leur numéro!\n")
            time.sleep(0.1)
        return win

def find_permutation_cycles(drawers):
    j = 0
    cycles = {}
    cycle = []
    visited = [False] * len(drawers)
    for number in range(1, len(drawers) + 1):
        if (visited[number - 1] == False):
            i = number
            if (drawers[i] == number):
                cycles[j] = number
                visited[i - 1] = True
                j += 1
            else:
                while (drawers[i] != number):
                    cycle += [i]
                    visited[i - 1] = True
                    i = drawers[i]
                cycle += [i]
                visited[i - 1] = True
                cycles[j] = cycle.copy()
                visited[i - 1] = True
                j += 1
                cycle.clear()  
    return cycles
    
def create_graph(drawers, size):
    prisoners = [p for p in range(1, size + 1)]
    G = nx.DiGraph()
    G.add_nodes_from(prisoners)
    edges = [(u,v) for u, v in drawers.items()]
    G.add_edges_from(edges,weight = 1)

    cycles = find_permutation_cycles(drawers)

    nbCycle = len(cycles)
    colorPalet = sb.color_palette(n_colors = nbCycle)
    colorMap = {}

    for num_cycle,nodes in cycles.items():
        if(type(nodes) == int):
            nodes = [nodes]
        for node in nodes:
            colorMap[node] = num_cycle
            
    myCycle = pd.DataFrame.from_dict(colorMap, orient = "index", columns = ["nbCycle"])
    myCycle["color"] = myCycle["nbCycle"].apply(lambda x: colorPalet[x])
    myCycle = myCycle.sort_index()

    pos = None
    nx.draw(G, pos, node_color = myCycle["color"].values, with_labels = True)
    plot.show()
