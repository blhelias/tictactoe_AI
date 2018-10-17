import random
import numpy as np
from collections import Counter
import numpy as np
import copy

mat = np.load("./data/morpion_mat.npy")
matrice_fini = []

for i in mat:
    matrice_fini.append(i.tolist())

def end(grille):
    l1 = [grille[0], grille[1], grille[2]]
    l2 = [grille[3], grille[4], grille[5]]
    l3 = [grille[6], grille[7], grille[8]]
    c1 = [grille[0], grille[3], grille[6]]
    c2 = [grille[1], grille[4], grille[7]]
    c3 = [grille[2], grille[5], grille[8]]
    d1 = [grille[0], grille[4], grille[8]]
    d2 = [grille[2], grille[4], grille[6]]
    end = [l1, l2, l3, c1, c2, c3, d1, d2]

    for i in end:
        if i[0] == i[1] == i[2] and i[0]!=0:
            return(i[0])

    if(0 in grille)==False:
        return(-1)

    return(0)

def vect_cumul(old_vect):
    vect = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for k in range(len(old_vect)):
        proba_cum = 0
        for p in range(k+1):
            proba_cum = proba_cum + old_vect[p]
        vect[k] = proba_cum
    return(vect)       
                
def joue_rand(grille, n):
    case = random.randint(0, 8)
    while grille[case] != 0:
        case = random.randint(0, 8)
    grille[case] = n
    return(grille, case)

def IA_fini(grille):
    for i in matrice_fini:
        #on regarde si la grille présente à déjà été rencontré
        if i[0] == (grille):
            # on prend le vecteur des probas cumulées
            vect = vect_cumul(i[1])   
            rand = random.random()
            for j in range (len(vect)):
                if  rand <= vect[j]:
                    grille[j] = 2
                    return(grille, j)
    grille, case = joue_rand(grille, 2)
    return(grille, case)

def get_grille(grille):
    res = []
    for i in range(3):
        for j in range(3):
            res.append(grille[i][j]['value'])
    return(res)

def f_1(grille, choix):
    y, x = choix // 3, choix % 3
    print(grille)
    grille[x][y]['value'] = 2
    return grille
