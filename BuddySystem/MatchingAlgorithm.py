class Student:
    """ Classe définissant un étudiant caractérisé par :
        - son prénom
        - son nom
        - ses réponses au questionnaire """

    def __init__(self, prenom, nom, reponses):
        """ Constructeur de notre classe """
        self.prenom = prenom
        self.nom = nom
        self.reponses = reponses


def LoveScore(Romeo,Juliet):
    r1, r2 = Romeo.reponses, Juliet.reponses
    nbReponses = len(r1)
    return len([ 0 for k in range(nbReponses) if r1[k] + r2[k] != 1])
