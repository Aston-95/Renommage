class ListeRegle:

    def __init__(self, regles):
        """

        :param regles:
        """
        self.regles = regles

    def get_regles(self):
        """

        :return:
        """
        return self.regles

    def set_regles(self, regles):
        """

        :param regles:
        :return:
        """
        self.regles = regles


    def charger(self):
        file = open("NOMLOGICIEL.ini", "r")
        file = file.read()
        return(file)

    def sauvegarder(self):
        file = open("NOMLOGICIEL.ini", "w")
        file.write(str(self.regles))
        file.close()

    def __str__(self):
        """

        :return:
        """
        return self.regles