class ListeRegle:

    def __init__(self, regles):
        """
        Initialisation de la classe ListeRegle avec la valeur d'entrée : regles
        :param regles:
        """
        self.regles = regles

    def get_regles(self):
        """
        Creation d'une methode get pour la variable regles
        :return:
        """
        return self.regles

    def set_regles(self, regles):
        """
        Creation d'une methode set pour la variable regles
        :param regles:
        :return:
        """
        self.regles = regles


    def charger(self):
        """
        Charge le contenu du fichier " NOMLOGICIEL.ini'
        :return:
        """
        file = open("NOMLOGICIEL.ini", "r")
        file = file.read()
        return(file)

    def sauvegarder(self):
        """
        Sauvegarde "self.regles" en l'ajoutant dans le fichier NOMLOGICIEL.ini en plus de ce qui à déjà
        :return:
        """
        file = open("NOMLOGICIEL.ini", "a")
        file.write(self.regles)
        file.close()

    def __str__(self):
        """
        Retourne la valeur de "self.regles"
        :return:
        """
        return self.regles