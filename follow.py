import random
import time
import networkx as nx
import matplotlib.pyplot as plot

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
        drawers[i]=j
    
    return drawers
def case_follow_for_one_prisonner(tab,number_p):
    bool=False
    tries=0
    opened_drawers= []
    num_drawer=number_p
    while( tries<=(len(tab)/2) and not(bool) ):

        opened_drawers+=[num_drawer]
        
        
        if (tab[num_drawer-1]== number_p):
            bool=True
        else:
            num_drawer=tab[num_drawer-1]
        tries +=1   

    if (bool):
        print("le prisonnier numéro "+str(number_p)+" a trouve son numéro dans le tiroir "+str(num_drawer)+"  au bout de "+str(tries)+ " essais")
        time.sleep(0.1)
       
    else:
        print("après "+str(tries)+" essais le prisonnier numéro " + str(number_p) + " n'a pas trouve son numéro dans un tiroir")
        time.sleep(0.1)
    return bool    

def case_follow_for_group_of_prisonner(len):
    tab=create_tab(len)
    print("tableau: ")
    print(tab)
    print("\n\n\n")
    prisonner=1
    win=False
    
    while(prisonner<=len):
        bool=case_follow_for_one_prisonner(tab,prisonner)
        if(bool):
            prisonner += 1
        else:
            print("La stratégie Suivre a echoué au bout du " + str(prisonner) + " prisonnier(s)")
            return win
    if(bool):
        win=True
        print("Victoire! La stratégie Suivre est un succes, tous les prisonniers ont trouve leur numero selon ")
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

def graph(size):
    prisoners=[p for p in range(1,size+1)]
    drawers=create_drawers(size)
    print(drawers)
    G=nx.DiGraph()
    G.add_nodes_from(prisoners)
    edges=[(u,v) for u,v in drawers.items()]
    G.add_edges_from(edges,weight=1)
    nx.draw(G, with_labels=True)
    plot.show()



#graph(40)
#how_many_try_to_resolve_the_case_follow(20)
