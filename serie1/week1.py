les listes : partie 3
Exercice 1 : Ecrire une fonction, qui à partir d'une liste de nombres entiers, détermine le nombre maximum d’occurrences consécutives strictement supérieures à 10. Proposer deux versions de ce programme l'une avec une gestion des index et une autre sans.

def exercice1_version_avec(L) :
    xF = 0
    xMax = 0
    for i in range(len(L)) :
        if L[i] > 10:
            xMax += 1
        else :
            if xMax > xF:
                xF = xMax
            xMax = 0
    return xF
#OK
def exercice1_version_sans(L) :
    xF = 0
    xMax = 0
    for i in L:
        if i > 10:
            xMax += 1
        else :
            if xMax > xF:
                xF = xMax
            xMax = 0
    return xF
#OK
Exercice 2 : Ecrire une fonction qui à partir d'une liste de nombres entiers, détermine l'écart maximum entre deux valeurs consécutives. Proposer deux versions de ce programme l'une avec une gestion des index et une autre sans.

def exercice2_avec(L) :
        avancement = 0
    for i in range(len(L)-1):
        if abs(L[i+1] - L[i]) > avancement:
            avancement = abs(L[i+1] - L[i])
    return avancement
#OK
def exercice2_sans(L) :
    aac = 0
    furui = L[0]
    for i in L:
        if abs(i - furui) > aac:
            aac = abs(i - furui)
        furui = i
    return aac
#OK
Exercice 3 : Ecrire une fonction, qui à partir d'une liste de nombres entiers, décale les éléments de cette liste d'un élément vers la droite (décalage circulaire, le dernier élément se retrouve alors en premier)

def exercice3(L) :
    last = L[-1]
    for i in range(len(L)- 1, 0, -1):
        L[i] = L[i-1]
    L[0] = last
    return L
#OK    
Exercice 4 : Ecrire une fonction, qui à partir d'une liste de nombres entiers, décale les éléments de cette liste d'un élément vers la gauche (décalage circulaire, le premier élément se retrouve alors en dernier)

def exercice4(L) :
    furui = L[0]
    for i in range(1, len(L)):
        L[i - 1] = L[i]
    L[-1] = furui
    return L
#OK
Exercice 5 : Ecrire une fonction, qui à partir d'une liste de nombres entiers d'une valeur x et d'un index i, insére la valeur x à l'index i sans utiliser la méthode insert().

def exercice5(L, x, i) :
    L.append(0)
    for j in range(len(L)-1, i, -1):
        L[j] = L[j - 1]
        print(L)
    L[i] = x
    return L
#OK
Exercice 6 : Ecrire une fonction, qui à partir d'une liste de nombres entiers, détermine si la liste est croissante. La fonction retourne un booléen.

def exercice6(L) :
    for i in range(len(L) - 1):
        if L[i+1] - L[i] < 0:
            return False
    return True
#OK
Exercice 7 : Ecrire une fonction, qui à partir d'une liste de nombres entiers, détermine la plus longue succession ininterrompue de valeurs rangées dans l’ordre croissant.

def exercice7(L) :
    streak = 0
    mStreak = 0
    print(len(L))
    for i in range(len(L)-1):
        print(i)
        if L[i+1] - L[i] == 1:
            mStreak += 1
        if L[i+1] - L[i] != 1 or i == len(L) -2 :
            if mStreak > streak:
                streak = mStreak
            mStreak = 0
    return streak
#OK
Exercice 8 : Ecrire une fonction, qui à partir de deux listes croissantes de taille quelconque, construit une liste croissante.

def exercice8(L1, L2) :
    i = 0
    y = 0
    L3 = []
    while i < len(L1) or y < len(L2):
        if L1[i] < L2[y] and i < len(L1):
            L3.append(L1[i])
            i += 1
        else:
            L3.append(L2[i])
            y += 1
    return L3
#
Exercice 9 : Ecrire une fonction qui construit une liste de 8 éléments contenant aléatoirement les valeurs de 1 à 8, chaque valeur devant etre unique.

def exercice9(L) :
    pass
Exercice 10 : Ecrire une fonction, qui à partir de deux listes de nombres entiers, détermine le nombre d'éléments présents dans les deux listes. Proposer deux versions, l'une avec l'opérateur in et l'autre sans.

def exercice10_avec_in(L1, L2) :
    pass
def exercice10_sans_in(L1, L2) :
    pass
Exercice 11 : Écrire une fonction, qui à partir d'une matrice contenant des nombres entiers implémentée par une liste de listes, ajoute une dernière colonne contenant la moyenne de chaque ligne (attention les sous listes peuvent avoir des tailles variables)

def exercice11(L):
    pass
Exercice 12 : Écrire une fonction, qui à partir d'une matrice contenant des nombres entiers implémentée par une liste de listes, ajoute une dernière ligne contenant le nombre de valeurs paires de chaque colonne.

def exercice12(L):
    pass
Exercice 13 : Ecrire une fonction, qui à partir d'une matrice 3x4 implémentée par une liste de listes, construit une liste de 12 élements contenant successivement les éléments de la matrice, ligne par ligne.

def exercice13(L):
    pass
Exercice 14 : Ecrire une fonction, qui à partir d'une matrice 3x4 implémentée par une liste de listes, construit une liste de 12 élements contenant successivement les éléments de la matrice, colonne par colonne.

def exercice14(L): 
    pass
Exercice 15 : Ecrire une fonction, qui à partir d'une matrice 3x3 implémentée par une liste de listes, vérifie qu'il existe au moins une ligne où tous les éléments ont la meme valeur.

def exercice15(L):
    pass
Exercice 16 : Ecrire une fonction, qui à partir d'une matrice 3x3 implémentée par une liste de listes, vérifie qu'il existe au moins une colonne où tous les éléments ont la meme valeur.

def exercice16(L):
    pass
Exercice 17 : Ecrire une fonction, qui à partir d'une matrice 3x3 implémentée par une liste de listes, vérifie que tous les éléments ont des valeurs différentes.

def exercice17(L):
    pass
Exercice 18 : Ecrire une fonction, qui à partir d'une matrice 3x3 implémentée par une liste de listes, met à 0 tous les éléments d'une ligne si la somme de ces éléments est un multiple de 5.

def exercice18(L):
    pass
Exercice 19 : Ecrire une fonction, qui à partir d'une matrice 3x3 implémentée par une liste de listes, met à 0 tous les éléments d'une colonne si la somme de ces éléments un multiple de 5.

def exercice19(L):
    pass
Exercice 20 : Ecrire une fonction, qui à partir d'une matrice 3x5 implémentée par une liste de listes, permutent les lignes et les colonnes pour ainsi obtenir une matrice 5x3.
#Exercice 7 : Ecrire une fonction, qui à partir d'une liste de nombres entiers, 
#détermine la plus longue succession ininterrompue de valeurs rangées dans l’ordre croissant



def exercice7(L) :
    streak = 0
    mStreak = 0
    for i in range(len(L)-1):
        print("OBJECT ", i)
        if L[i+1] - L[i] == 1:
            mStreak += 1
            print("PASSED !")
        print("EXIT ", L[i+1] - L[i], L[i], L[i+1])
        if L[i+1] - L[i] != 1 or i == len(L) - 1 :
            if mStreak > streak:
                streak = mStreak
            print("RESET !")
            mStreak = 0
    return streak

datatest = [2, 3, 4, 5, 12, 13, 14, 25, 26, 27, 28, 29, 30, 31, 32, 33]
datatoast = [2, 3, 4, 5, 12, 13, 14, 25, 26, 27, 28, 29, 30, 31, 32, 33]

def consecutive(L) :

    #conversion en int des élements de la liste
    data = []
    trieur = 0
    counter = 0
    for i in range(L):
        trieur = 0

    hightest = 0
    for i in range(data):
        if i >= hightest:
            hightest = i
    return hightest



#Exercice 8 : Ecrire une fonction,
#qui à partir de deux listes croissantes de taille quelconque, construit une liste croissante.

def exo8(L1,L2):
    L3 = L1 +L2
    low = L3[0]
    counter = 0
    for i in range(L3):
        if low >= L3[counter]:
            low = L3[counter]
        counter += 1
    counter = 0
    return low
print(exo8(datatest,datatoast))

les listes : partie 3
Exercice 1 : Ecrire une fonction, qui à partir d'une liste de nombres entiers, détermine le nombre maximum d’occurrences consécutives strictement supérieures à 10. Proposer deux versions de ce programme l'une avec une gestion des index et une autre sans.

def exercice1_version_avec(L) :
    xF = 0
    xMax = 0
    for i in range(len(L)) :
        if L[i] > 10:
            xMax += 1
        else :
            if xMax > xF:
                xF = xMax
            xMax = 0
    return xF
#OK
def exercice1_version_sans(L) :
    xF = 0
    xMax = 0
    for i in L:
        if i > 10:
            xMax += 1
        else :
            if xMax > xF:
                xF = xMax
            xMax = 0
    return xF
#OK
Exercice 2 : Ecrire une fonction qui à partir d'une liste de nombres entiers, détermine l'écart maximum entre deux valeurs consécutives. Proposer deux versions de ce programme l'une avec une gestion des index et une autre sans.

def exercice2_avec(L) :
        avancement = 0
    for i in range(len(L)-1):
        if abs(L[i+1] - L[i]) > avancement:
            avancement = abs(L[i+1] - L[i])
    return avancement
#OK
def exercice2_sans(L) :
    aac = 0
    furui = L[0]
    for i in L:
        if abs(i - furui) > aac:
            aac = abs(i - furui)
        furui = i
    return aac
#OK
Exercice 3 : Ecrire une fonction, qui à partir d'une liste de nombres entiers, décale les éléments de cette liste d'un élément vers la droite (décalage circulaire, le dernier élément se retrouve alors en premier)

def exercice3(L) :
    last = L[-1]
    for i in range(len(L)- 1, 0, -1):
        L[i] = L[i-1]
    L[0] = last
    return L
#OK    
Exercice 4 : Ecrire une fonction, qui à partir d'une liste de nombres entiers, décale les éléments de cette liste d'un élément vers la gauche (décalage circulaire, le premier élément se retrouve alors en dernier)

def exercice4(L) :
    furui = L[0]
    for i in range(1, len(L)):
        L[i - 1] = L[i]
    L[-1] = furui
    return L
#OK
Exercice 5 : Ecrire une fonction, qui à partir d'une liste de nombres entiers d'une valeur x et d'un index i, insére la valeur x à l'index i sans utiliser la méthode insert().

def exercice5(L, x, i) :
    L.append(0)
    for j in range(len(L)-1, i, -1):
        L[j] = L[j - 1]
        print(L)
    L[i] = x
    return L
#OK
Exercice 6 : Ecrire une fonction, qui à partir d'une liste de nombres entiers, détermine si la liste est croissante. La fonction retourne un booléen.

def exercice6(L) :
    for i in range(len(L) - 1):
        if L[i+1] - L[i] < 0:
            return False
    return True
#OK
Exercice 7 : Ecrire une fonction, qui à partir d'une liste de nombres entiers, détermine la plus longue succession ininterrompue de valeurs rangées dans l’ordre croissant.

def exercice7(L) :
    streak = 0
    mStreak = 0
    print(len(L))
    for i in range(len(L)-1):
        print(i)
        if L[i+1] - L[i] == 1:
            mStreak += 1
        if L[i+1] - L[i] != 1 or i == len(L) -2 :
            if mStreak > streak:
                streak = mStreak
            mStreak = 0
    return streak
#OK
Exercice 8 : Ecrire une fonction, qui à partir de deux listes croissantes de taille quelconque, construit une liste croissante.

def exercice8(L1, L2) :
... (59 lignes restantes)
