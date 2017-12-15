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

        :return:
        """
        return self.amorce

    def get_apartirde(self):
        """

        :return:
        """
        return self.apartirde

    def get_prefixe(self):
        """

        :return:
        """
        return self.prefixe

    def get_nomfichier(self):
        """

        :return:
        """
        return self.nomfichier

    def get_postfixe(self):
        """

        :return:
        """
        return self.postfixe

    def get_extension(self):
        """

        :return:
        """
        return self.extension

    def set_amorce(self, amorce):
        """

        :param amorce:
        :return:
        """
        self.amorce = amorce


    def set_apartirde(self, apartirde):
        """

        :param apartirde:
        :return:
        """
        self.apartirde = apartirde


    def set_prefixe(self, prefixe):
        """

        :param prefixe:
        :return:
        """
        self.prefixe = prefixe


    def set_nomfichier(self, nomfichier):
        """

        :param nomfichier:
        :return:
        """
        self.nomfichier = nomfichier


    def set_postfixe(self, postfixe):
        """

        :param postfixe:
        :return:
        """
        self.postfixe = postfixe


    def set_extension(self, extension):
        """

        :param extension:
        :return:
        """
        self.extension = extension

    def __str__(self):
        """

        :return:
        """
        return "{} {} oui  test {} a".format(self.amorce, self.apartirde, self.prefixe)


