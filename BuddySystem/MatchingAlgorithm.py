from random import *

class Student:
    """ Classe définissant un étudiant caractérisé par :
        - son prénom
        - son nom
        - ses réponses au questionnaire dans un tableau """

    def __init__(self, prenom, nom, reponses):
        """ Constructeur de notre classe """
        self.prenom = prenom
        self.nom = nom
        self.reponses = reponses


def LoveScore(Romeo,Juliet):
    """ Première approche très simpliste du LoveScore """
    r1, r2 = Romeo.reponses, Juliet.reponses
    nbReponses = len(r1)
    return len([ 0 for k in range(nbReponses) if r1[k] + r2[k] != 1])

def MatchingScore(matchingTable,Ei1,Ei2,nbCouples):
    """ Calcul le score total """
    score = 0
    for k in range(nbCouples):
        score += LoveScore(Ei1[k],Ei2[matchingTable[k]])
    return score

def MatchStudents(Ei1,Ei2):
    """ Ei1 et Ei2 sont des arrays de Student de même longueur. Cette fonction renvoie un array contenant une permutation de {0,...,nbCouples-1}"""
    nbCouples = len(Ei1)
    matchingTable = [k for k in range(nbCouples)]
    matchingScore = MatchingScore(matchingTable,Ei1,Ei2,nbCouples)
    while True:
        i,j = randrange(0,nbCouples),randrange(0,nbCouples)
        if LoveScore(Ei1[i],Ei2[matchingTable[j]]) + LoveScore(Ei1[j],Ei2[matchingTable[i]]) >= LoveScore(Ei1[i],Ei2[matchingTable[i]]) + LoveScore(Ei1[j],Ei2[matchingTable[j]]):
            matchingScore = matchingScore - (LoveScore(Ei1[i],Ei2[matchingTable[i]]) + LoveScore(Ei1[j],Ei2[matchingTable[j]])) + LoveScore(Ei1[i],Ei2[matchingTable[j]]) + LoveScore(Ei1[j],Ei2[matchingTable[i]])
            matchingTable[i],matchingTable[j] = matchingTable[j],matchingTable[i]
            goOn = input("Un matching plus performant a été trouvé, le MatchingScore vaut maintenant " + str(matchingScore) + " ! Appuyez sur entrer pour continuer la recherche...")
            if goOn:
                return matchingTable
