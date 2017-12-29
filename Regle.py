class Regle:

    def __init__(self, amorce, apartirde, prefixe, nomfichier, postfixe, extension):
        """

        :param amorce:
        :param apartirde:
        :param prefixe:
        :param nomfichier:
        :param postfixe:
        :param extension:
        """
        self.amorce = amorce
        self.apartirde = apartirde
        self.prefixe = prefixe
        self.nomfichier = nomfichier
        self.postfixe = postfixe
        self.extension = extension

    def get_amorce(self):
        """
        Creation d'une methode get pour la variable amorce
        :return:
        """
        return self.amorce

    def get_apartirde(self):
        """
        Creation d'une methode get pour la variable apartirde
        :return:
        """
        return self.apartirde

    def get_prefixe(self):
        """
        Creation d'une methode get pour la variable prefixe
        :return:
        """
        return self.prefixe

    def get_nomfichier(self):
        """
        Creation d'une methode get pour la variable nomfichier
        :return:
        """
        return self.nomfichier

    def get_postfixe(self):
        """
        Creation d'une methode get pour la variable postfixe
        :return:
        """
        return self.postfixe

    def get_extension(self):
        """
        Creation d'une methode get pour la variable extension
        :return:
        """
        return self.extension

    def set_amorce(self, amorce):
        """
        Creation d'une methode set pour la variable amorce
        :param amorce:
        :return:
        """
        self.amorce = amorce


    def set_apartirde(self, apartirde):
        """
        Creation d'une methode set pour la variable apartirde
        :param apartirde:
        :return:
        """
        self.apartirde = apartirde


    def set_prefixe(self, prefixe):
        """
        Creation d'une methode set pour la variable prefixe
        :param prefixe:
        :return:
        """
        self.prefixe = prefixe


    def set_nomfichier(self, nomfichier):
        """
        Creation d'une methode set pour la variable nomfichier
        :param nomfichier:
        :return:
        """
        self.nomfichier = nomfichier


    def set_postfixe(self, postfixe):
        """
        Creation d'une methode set pour la variable postfixe
        :param postfixe:
        :return:
        """
        self.postfixe = postfixe


    def set_extension(self, extension):
        """
        Creation d'une methode set pour la variable extension
        :param extension:
        :return:
        """
        self.extension = extension

    def __str__(self):
        """
        Donne les valeurs sous la forme :
        Amorce : Aucune | Apartirde :  | Prefixe : O | Nomfichier : Python | Postfixe : Q | Extension : .txt
        :return:
        """
        return "Amorce : {} | Apartirde : {} | Prefixe : {] | Nomfichier : {] | Postfixe : {] | Extension : {}".format(self.amorce, self.apartirde, self.prefixe, self.nomfichier, self.postfixe, self.extension)


