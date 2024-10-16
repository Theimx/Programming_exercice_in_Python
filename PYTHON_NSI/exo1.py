moyenneG = 0
coefG = 0 

moyenne_histoire = float(input("Entrez votre moyenne d'Histoire :"))
coef_histoire = 4

moyenneG = moyenneG + moyenne_histoire* coef_histoire
coefG += coef_histoire

moyenne_eps = float(input("Entrez votre moyenne d'eps :"))
coef_eps = 2

moyenneG = moyenneG + moyenne_eps* coef_eps
coefG += coef_eps

moyenne_spé1 = float(input("Entrez votre moyenne de spé1 :"))
coef_spé1 = 8

moyenneG = moyenneG + moyenne_spé1* coef_spé1
coefG += coef_spé1

moyenne_spé2 = float(input("Entrez votre moyenne de spé2 :"))
coef_spé2 = 8

moyenneG = moyenneG + moyenne_spé2* coef_spé2
coefG += coef_spé2

moyenne_philo = float(input("Entrez votre moyenne de philo :"))
coef_philo = 2

moyenneG = moyenneG + moyenne_philo* coef_philo
coefG += coef_philo

moyenne_Grand_Oral = float(input("Entrez votre moyenne du Grand Oral :"))
coef_GO = 12

moyenneG = moyenneG + moyenne_Grand_Oral* coef_GO
coefG += coef_GO

Bac = moyenneG /coefG
print("votre moyenne général est : " ,moyenneG / coefG)

if Bac <= 7.99:
    print("Refusé")
elif Bac >= 8 and Bac <= 9.99 : 
    print("Ratrapage")
elif Bac >= 10 and Bac <= 11.99:
    print("Bac sans mention")
elif Bac >= 12 and Bac <= 13.99:
    print("Mention Assez bien")
elif Bac >= 14 and Bac <= 15.99:
    print("Bien ")
elif Bac >= 16 and Bac <= 17.99:
    print("Très bien")
elif Bac >= 18:
    print("Felicitation")


# 10 11.99 #Sans mention
# 12 13.99 #Mention Assez bien
# 14 15.99 #Bien 
# 16 17.99 #Très bien
# 18 +     #felicitation



