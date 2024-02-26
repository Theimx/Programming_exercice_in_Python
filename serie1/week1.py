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
