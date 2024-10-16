
def moyenne_Bac(note1,note2,note3,note4,note5,note6,note7,coef1,coef2,coef3,coef4,coef5,coef6,coef7):

    moyenneG = 0
    coefG = 0 
    moyenneG = moyenneG + note1 * coef1
    coefG += coef1
    moyenneG = moyenneG + note2 * coef2 
    coefG += coef2 
    moyenneG = moyenneG + note3 * coef3 
    coefG += coef3 
    moyenneG = moyenneG + note4 * coef4 
    coefG += coef4 
    moyenneG = moyenneG + note5 * coef5 
    coefG += coef5 
    moyenneG = moyenneG + note6 * coef6 
    coefG += coef6
    moyenneG = moyenneG + note7 * coef7
    coefG += coef7

    Bac = moyenneG /coefG
    return Bac

print(moyenne_Bac(20,20,20,0,0,0,0,8,8,3,2,3,2,2))