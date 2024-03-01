#Exercice 1 : Ecrire une fonction, qui à partir d'une liste L de nombres entiers et d'un entier x, 
#détermine l’index de la première occurrence de x. Si la valeur x n’est pas présente dans la liste, 
#la fonction retourne la valeur -1.

def exercice1(L,x): #valider

    result = 0
    for i in L:
        if i == x:
            result = L.index(x)

    if result != L.index(x):
        result = -1
    return result
L = [1,2,3,4,5,2,10]
print(exercice1(L,1))

#Exercice 2 : Ecrire une fonction, qui à partir d'une liste L de nombres entiers et d'un entier x, 
#détermine l’index de la dernière occurrence de x. Si la valeur x n’est pas présente dans la liste, 
#la fonction retourne la valeur -1.

#Exercice 3 : Ecrire une fonction, qui à partir d'une liste L de nombres entiers et d'un entier x détermine, l’index de la dernière occurrence de x. Si la valeur x n’est pas présente dans la liste, la fonction retourne la valeur de la liste la plus proche de x par excès.

#Exercice 4 : Ecrire une fonction, qui à partir d'une liste L de nombres entiers et d'un entier x, détermine l’index de la dernière occurrence de x. Si la valeur x n’est pas présente dans la liste, la fonction retourne la valeur de la liste la plus proche de x par defaut.

#Exercice 5 : Ecrire une fonction, qui à partir d'une liste L de nombres entiers et d'un entier x, vérifie que la valeur x apparait une et une seule fois dans la liste. La fonction retourne un booléen.

#Exercice 6 : Ecrire une fonction, qui à partir d'une liste L de nombres entiers, indique s'il existe deux éléments consécutifs dont la somme est égale à 10. La fonction renvoie un booléen.

#Exercice 7 : Ecrire une fonction, qui à partir d'une liste L de nombres entiers relatifs, vérifie qu’en valeur absolue, la somme des éléments des éléments négatifs est inférieure à la somme des éléments positifs. La fonction renvoie True ou False.

#Exercice 8 : Ecrire une fonction, qui à partir d'une liste L contenant un nombre pair de nombres entiers, permute les éléments deux à deux.

#Exercice 9 : Ecrire une fonction, qui à partir d'une liste L de nombres entiers, détermine les couples d'entiers consécutifs. Ces couples sont stockées sous la forme d’une liste de tuples. Si aucun couple n’est trouvé, la fonction retourne une liste vide.

#Exercice 10 : Ecrire une fonction qui construit une liste en prenant alternativiement les valeurs de deux listes L1 et L2 (de taille identique).

#Exercice 11 : Ecire une fonction, qui à partir de deux nombres n et m passés en argument, construit une liste de taille n contenant des sous listes de taille m dont les éléments ont une valeur aléatoire entière comprise entre 1 et 10.

#Exercice 12 : Écrire une fonction, qui à partir d’une liste de listes de nombres entiers, construit une liste ne contenant que le dernier élément de chaque sous liste.

#Exercice 13 :Écrire une fonction, qui à partir d'une matrice implémentée par une liste de listes, ajoute 1 à chaque élément pour les lignes paires et retire 1 à chaque élément pour les lignes impaires.

#Exercice 14 : Écrire une fonction, qui à partir d’une liste L de listes, détermine si le nombre d'éléments de chaque sous liste est identique. La fonction renvoie un booléen.

#Exercice 15 : Écrire une fonction, qui à partir d’une liste L de listes et d'une valeur x, détermine le nombre d'occurences de cette valeur. Proposer deux versions de ce programme l'une avec une gestion des index et une autre sans.

#Exercice 16 : Écrire une fonction, qui à partir d’une liste L de listes de nombres entiers et d'une valeur x, détermine les couples d'index (ligne , colonne) correspondant aux valeurs de x. Cette fonction renvoie une liste de tuples.

#Exercice 17 : Ecrire une fonction, qui à partir d’une liste de listes L de nombres entiers, détermine la valeur maximum ainsi que le couple d'index de ce maximum. Cette fonction renvoie un tuple composé du maximum et d'un tuple contenant le couple d'index. (il est interdit d’utiliser la fonction max(liste) de python).

#Exercice 18 : Ecrire une fonction, qui à partir d’une liste de listes L de nombres entiers, détermine la somme des maximums des différentes sous listes (il est interdit d’utiliser la fonction max(liste) de python).

#Exercice 19 : Écrire une fonction, qui à partir d’une liste L de listes L de nombres entiers, détermine le maximum de chaque sous liste et l'ajoute à la fin chaque sous liste. Proposer deux versions de ce programme l'une avec une gestion des index et une autre sans.

#Exercice 20 : Écrire une fonction, qui à partir d'une matrice carrée (nxn) contenant des nombres entiers implémentée par une liste L de listes,détermine la somme des éléments de la diagonale.
