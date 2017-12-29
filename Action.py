from Regle import *
import os

class Action:

    def __init__(self, nomdurepertoire, regle):
        """
        Initialisation de la Classe Action avec les valeurs d'entrée "nomdurepertoire" et "regle"
        :param nomdurepertoire:
        :param regle:
        """
        self.nomdurepertoire = nomdurepertoire
        self.regle = regle



    def get_nomdurepertoire(self):
        """
        Creation d'une methode get pour la variable nomdurepertoire
        :return:
        """
        return self.nomdurepertoire

    def get_regle(self):
        """
        Creation d'une methode get pour la variable regle
        :return:
        """
        return self.regle

    def set_nomdurepertoire(self, nomdurepertoire):
        """
        Creation d'une methode set pour la variable nomdurepertoire
        :param nomdurepertoire:
        :return:
        """
        self.nomdurepertoire = nomdurepertoire

    def set_regle(self, regle):
        """
        Creation d'une methode set pour la variable regle
        :param regle:
        :return:
        """
        self.regle = regle

    def simule(self):
        """
        Endroit ou va le plus travailler le programme.

        La méthode à pour but de "simuler" avec les paramètres données en entrée ce que va devenir le nom des fichiers.

        1.Listage des fichiers du dossier et mise au propre des valeurs de la valeur Action.regle

        2. Tri des fichiers en fonction de l'extension choisi

        3. En fonction de l'amorce il y'a different façons.
            AMORCE : Aucune
                Nomfichier : Original
            ou  Nomfichier : Autre

            AMORCE : Lettre
            création d'un script permettant l'amorce à partir de lettre
                Nomfichier : Original
            ou  Nomfichier : Autre

            AMORCE : Chiffre
            creation d'un script permmetant l'amorce à partir de chiffre
                Nomfichier : Original
            ou  Nomfichier : Autre

        :return: Liste des fichiers originaux trié & Liste des fichiers modifié. Par un duet (self.original,self.modifie)
        """
        #1
        self.original = os.listdir(self.nomdurepertoire)

        Regle.amorce = Action.regle[0]
        Regle.apartirde = Action.regle[1]
        Regle.prefixe = Action.regle[2]
        Regle.nomfichier = Action.regle[3]
        Regle.postfixe = Action.regle[4]
        Regle.extension = Action.regle[5]

        # 2
        for i in range(len(self.original),0,-1):
            file = self.original[i-1]
            extension = os.path.splitext(file)[1]
            print(file)
            print(extension)
            if extension != Regle.extension:
                del self.original[i-1]
        print(self.original)

        # 3
        self.modifie = []

        # POUR AMORCE = AUCUNE
        # ---------------------------------------------------------------------------------
        if Regle.amorce == "Aucune":
            for file in self.original:


                if Regle.nomfichier == "Original":
                    nom_original = os.path.splitext(file)[0]
                    file_modifie = Regle.prefixe + nom_original + Regle.postfixe + Regle.extension
                    self.modifie.append(file_modifie)
                    print (file_modifie)
                    print (self.modifie)

                if Regle.nomfichier != "Original":
                    file_modifie = Regle.prefixe + Regle.nomfichier + Regle.postfixe + Regle.extension
                    self.modifie.append(file_modifie)
                    print (file_modifie)
                    print (self.modifie)

            print (self.modifie)

        # POUR AMORCE = LETTRE
        # ---------------------------------------------------------------------------------
        if Regle.amorce == "Lettre":
            for file in self.original:

                user = Regle.apartirde

                h = []

                for c in user:
                    h.append(ord(c))

                while (True):

                    out = ""
                    for e in h:
                        out += chr(e)

                    Regle.amorce = out

                    if Regle.nomfichier == "Original":
                        nom_original = os.path.splitext(file)[0]
                        file_modifie = Regle.amorce + Regle.prefixe + nom_original + Regle.postfixe + Regle.extension
                        self.modifie.append(file_modifie)


                    if Regle.nomfichier != "Original":
                        file_modifie = Regle.amorce + Regle.prefixe + Regle.nomfichier + Regle.postfixe + Regle.extension
                        self.modifie.append(file_modifie)


                    if len(h) == 1:

                        h[0] += 1

                        if h[0] >= 91:
                            h = [65, 65]


                    elif len(h) == 2:

                        h[1] += 1

                        if h[1] >= 91:
                            h[0] += 1
                            h[1] = 65

                            if h[0] >= 91:
                                h = [65, 65, 65]

                    elif len(h) == 3:

                        h[2] += 1

                        if h[2] >= 91:
                            h[1] += 1
                            h[2] = 65

                            if h[1] >= 91:
                                h[0] += 1
                                h[1] = 65
                                h[2] = 65

                                if h[0] >= 91:
                                    break

        # POUR AMORCE = CHIFFRE
        # ---------------------------------------------------------------------------------
        if Regle.amorce == "Chiffre":
            for file in self.original:

                e = int(Regle.apartirde)

                while (True):

                    if e < 1000:

                        Regle.amorce = e
                        Regle.amorce = str(Regle.amorce)

                        if Regle.nomfichier == "Original":
                            nom_original = os.path.splitext(file)[0]
                            file_modifie = Regle.amorce + Regle.prefixe + nom_original + Regle.postfixe + Regle.extension
                            self.modifie.append(file_modifie)


                        if Regle.nomfichier != "Original":
                            file_modifie = Regle.amorce + Regle.prefixe + Regle.nomfichier + Regle.postfixe + Regle.extension
                            self.modifie.append(file_modifie)
                        e=e+1
                    else:
                        break


        return (self.original,self.modifie)

    def __str__(self):
        """

        :return:
        """
        return "Nomdurepertoire : {}    Regle : {} ".format(self.nomdurepertoire, self.regle)


