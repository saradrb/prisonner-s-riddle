
import pandas as pd
import random
import time
import networkx as nx
import matplotlib.pyplot as plot
import seaborn as sb 

def create_tab(n):
    i = 1
    x = []
    while (i <= n):
        x = x + [i]
        i += 1
    random.shuffle(x)
    return x

def create_drawers(n):
    i=1
    tab=create_tab(n)
    drawers={}
    
    for i,j in enumerate(tab):
        drawers[i+1]=j
    return drawers


def case_follow_for_one_prisonner(drawers,number_p):
    bool=False
    tries=0
    opened_drawers= []
    num_drawer=number_p
    while( tries<(len(drawers)/2) and not(bool) ):

        opened_drawers+=[num_drawer]
        
        
        if (drawers[num_drawer]== number_p):
            bool=True
        else:
            num_drawer=drawers[num_drawer]
        tries +=1   

    if (bool):
        print("le prisonnier numéro "+str(number_p)+" a trouve son numéro dans le tiroir "+str(num_drawer)+"  au bout de "+str(tries)+ " essais")
        time.sleep(0.1)
       
    else:
        print("après "+str(tries)+" essais le prisonnier numéro " + str(number_p) + " n'a pas trouve son numéro dans un tiroir")
        time.sleep(0.1)
    return bool    



def case_follow_for_group_of_prisonner(drawers,len):
    print("drawers: ")
    print(drawers)
    print("\n\n\n")
    prisonner=1
    win=False
    
    while(prisonner<=len):
        bool=case_follow_for_one_prisonner(drawers,prisonner)
        if(bool):
            prisonner += 1
        else:
            print("La stratégie Suivre a echoué au bout de " + str(prisonner) + " prisonnier(s)")
            return win
    if(bool):
        win=True
        print("Victoire! La stratégie Suivre est un succes, tous les prisonniers ont trouve leur numero ")
        time.sleep(0.1)
        return win
    

def how_many_try_to_resolve_the_case_follow(len):
    i = 1
    print("\n\n")
    print("essai numero "+str(i))
    print("\n")
    while ( case_follow_for_group_of_prisonner(len) == False):
        print("\n\n")
        print("essai numero "+str(i))
        print("\n")
        i += 1
    return i



def find_cycles(drawers):
    j=0
    cycles={}
    cycle=[]
    visited=[False]*len(drawers)
    print(drawers)
    for number in range(1,len(drawers)+1):
        if (visited[number-1]==False):
            #print(number)
            #print(visited[number-1])
            i=number
            if (drawers[i]==number):
                cycles[j]=number
                visited[i-1]=True
                j+=1
            else:
                while (drawers[i]!=number):
                    cycle+=[i]
                    visited[i-1]=True
                    i=drawers[i]
                cycle+=[i]
                visited[i-1]=True
                cycles[j]=cycle.copy()
                visited[i-1]=True
                j+=1
                cycle.clear()
               
    return cycles


    
def graph(drawers,size):
    prisoners=[p for p in range(1,size+1)]
    G=nx.DiGraph()
    G.add_nodes_from(prisoners)
    edges=[(u,v) for u,v in drawers.items()]
    G.add_edges_from(edges,weight=1)

    cycles=find_cycles(drawers)

    nb_cycle=len(cycles)
    color_palet=sb.color_palette(n_colors=nb_cycle)
    color_map = {}

    for num_cycle,nodes in cycles.items():
        print(num_cycle)
        if(type(nodes)==int):
            nodes=[nodes]
        for node in nodes:
            color_map[node] = num_cycle
            
    myCycle = pd.DataFrame.from_dict(color_map, orient="index", columns=["num_cycle"])
    myCycle["color"] = myCycle["num_cycle"].apply(lambda x: color_palet[x])
    myCycle = myCycle.sort_index()

    pos = None
    nx.draw(G, pos, node_color=myCycle["color"].values, with_labels=True)
    plot.show()

drawers=create_drawers(10)
case_follow_for_group_of_prisonner(drawers,10)
#print(len(drawers))
graph(drawers,10)


#how_many_try_to_resolve_the_case_follow(20)
