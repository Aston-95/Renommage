from Action import *
import os

class Renommage(Action):

    def __init__(self, nomdurepertoire, regle):
        """
        Init de la classe Renommage héritant de la classe Action
        Definition de self.original et self.modifie

        """
        Action.__init__(self, nomdurepertoire, regle)
        self.original=0
        self.modifie=0

    def renommer(self):
        """
        Application du renommage avec le travail fait auparavant dans la méthode "simule"
        exemple :
        os.rename("c:\toto.txt", "c:\titi.txt")
        :return:
        """

        for i in range(0, len(self.original)):
            os.rename(Renommage.nomdurepertoire+"/" +self.original[i],Renommage.nomdurepertoire+"/" + self.modifie[i])


    def __str__(self):
        """

        :return:
        """
        return