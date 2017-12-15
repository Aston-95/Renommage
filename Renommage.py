from Action import *
from os import *

class Renommage(Action):

    def __init__(self, nomdurepertoire, regle):
        """


        """
        Action.__init__(self, nomdurepertoire, regle)

    def renommer(self):
        """

        exemple :
        os.rename("c:\toto.txt", "c:\titi.txt")
        :return:
        """
        i=0
        originaux = os.listdir()
        for original in originaux:
            os.rename(Action.nomdurepertoire+original, Action.nomdurepertoire+self.modifie[i])
            i+=1

    def __str__(self):
        """

        :return:
        """
        return