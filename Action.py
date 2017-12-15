from Regle import *
from os import *

class Action:

    def __init__(self, nomdurepertoire, regle):
        """

        :param nomdurepertoire:
        :param regle:
        """
        self.nomdurepertoire = nomdurepertoire
        self.regle = regle



    def get_nomdurepertoire(self):
        """

        :return:
        """
        return self.nomdurepertoire

    def get_regle(self):
        """

        :return:
        """
        return self.regle

    def set_nomdurepertoire(self, nomdurepertoire):
        """

        :param nomdurepertoire:
        :return:
        """
        self.nomdurepertoire = nomdurepertoire

    def set_regle(self, regle):
        """

        :param regle:
        :return:
        """
        self.regle = regle

    def simule(self):
        """
        Simule qui affiche à l’écran le nom du fichier original et celui qu’il aura après renommage
        :return:
        """
        if Regle.get_amorce() == "Aucune":
            a = self.regle.get_nomfichier
            b = Regle.get_amorce() + Regle.get_prefixe() + Regle.get_nomfichier() + Regle.get_postfixe() + Regle.get_extension()

            original = os.listdir(self.nomdurepertoire)
            self.modifie = []

            for file in original:
                filename, extension = os.path.splitext(file)
                newName = "pre" + filename + "suf" + extension
                self.modifie.append(newName)


        return (a,b)

    def __str__(self):
        """

        :return:
        """
        return "{} oui  test {} a".format(self.nomdurepertoire, self.regle)


