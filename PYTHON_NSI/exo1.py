moyenneG = 0
coefG = 0 

moyenne_histoire = int(input("Entrez votre moyenne d'Histoire :"))
coef_histoire = 4

moyenneG = moyenneG + moyenne_histoire* coef_histoire
coefG += coef_histoire

moyenne_eps = int(input("Entrez votre moyenne d'eps :"))
coef_eps = 2

moyenneG = moyenneG + moyenne_eps* coef_eps
coefG += coef_eps

moyenne_spé1 = int(input("Entrez votre moyenne de spé1 :"))
coef_spé1 = 8

moyenneG = moyenneG + moyenne_spé1* coef_spé1
coefG += coef_spé1

moyenne_spé2 = int(input("Entrez votre moyenne de spé2 :"))
coef_spé2 = 8

moyenneG = moyenneG + moyenne_spé2* coef_spé2
coefG += coef_spé2

moyenne_philo = int(input("Entrez votre moyenne de philo :"))
coef_philo = 2

moyenneG = moyenneG + moyenne_philo* coef_philo
coefG += coef_philo

moyenne_Grand_Oral = int(input("Entrez votre moyenne du Grand Oral :"))
coef_GO = 12

moyenneG = moyenneG + moyenne_Grand_Oral* coef_GO
coefG += coef_GO

Bac = moyenneG /coefG
print("votre moyenne général est : " ,moyenneG / coefG)

if Bac <= 10:
    print("vous n'avez pas votre bac")
if Bac >= 11: 
    print("vous avez le bac")
