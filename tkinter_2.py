from Action import *
from Renommage import *
from Regle import *
from ListeRegle import *
from tkinter import *
from tkinter import filedialog
from tkinter_1 import *



class Tkinter2:

    def __init__(self):
        """
        Init de la classe Tkinter2 qui correspond au Tkinter de la création de règles
        Aucun paramètre d'entrée
        Parse le fichier "LOGICIEL.ini" en plusieurs tableaux pour qu'ils lisibles correctement lors de l'appel de la fonction Tk_list
        :param value:
        """
        f = open("NOMLOGICIEL.ini", "r")
        r = f.read()
        self.regles = r.splitlines()
        for i in range(0, len(self.regles)):
            list = self.regles[i].split(",")
            self.regles[i] = list


    def create_regle(self):
        """
        Aucun Param
        Fonction permettant la création de la regle dans le fichier "NOMLOGICIEL.ini"
        1. Regarde d'abord la var 'var_texte_nomfichier' pour si il doit garder la première la valeur dans l'entry ou la value du radiobutton
        2. Réunion de toutes les var de l'interface pour les concatener dans la var 'regle'. Tout cela au format CSV, le plus facile à traiter ensuite
        3. Chargement du contenu actuel et sauvegarde avec la nouvelle règle
        :return:
        """
        # Determination de la valeur du nom de fichier
        if self.var_texte_nomfichier.get() == ("2"):
            self.nomfichier = self.var_texte_entrynom.get()
        else:
            self.nomfichier = "Original"
        
        # Création de la règle. La règle contient : Nom de la règle,AMORCE,APARTIRDE,PREFIXE,NOMFICHIER,POSTFIXE,EXTENSION
        regle = self.var_texte_regle.get() + "," + self.var_texte_amorce.get() + "," \
                + self.var_texte_apartirde.get() + "," + self.var_texte_prefixe.get() + "," \
                + self.nomfichier + "," + self.var_texte_suffixe.get() + "," \
                + self.var_texte_extension.get() + "\n"
        file = ListeRegle(regle).charger()

        ListeRegle(regle).sauvegarder()
        return

    def reglos(self, index):
        """
        Inachevé, devait être ici la fonction permettant l'ajout des variables dans les champs du TKinter.
        Ici permet d'afficher le contenu de la règle selectionner avec le scroll du bouton lister
        :param index:
        :return:
        """
        print(self.regles[index[0]])



    def tk_list(self):
        """
        Petite fenetre Tkinter permettant d'afficher toute les règles du fichier "NOMLOGICIEL.ini" dans une liste.
        Envoi la selection à la méthode "reglos"
        :return:
        """
        master = Tk()

        listbox = Listbox(master)
        listbox.pack()

        for item in self.regles:
            listbox.insert(END, item[0])

        b = Button(master, text="Valider", width=10, height=2, command=lambda: self.reglos(listbox.curselection()))
        b.pack()


        mainloop()


    def tkinter_secondaire(self):
        """
        Interface Tkinter de la création de règles. Contient les éléments de TKinter ainsi que les variables
        Aucun code dans cette fonction, que de l'esthétique.
        :return:
        """

        # Initialisation du Tkinter
        fenetre = Tk()
        fenetre.geometry('600x350')

        # Column 0
        # ---------------------------------------------------------------------------------

        # LISTER REGLE
        bouton_lister = Button(fenetre, text="Lister", width=10, height=2, command=lambda: self.tk_list())
        bouton_lister.grid(row=0, column=0)

        # CREER REGLE
        bouton_creer = Button(fenetre, text="Créer", width=10, height=2,
                              command=lambda: fenetre.destroy() & tkinter_2.Tkinter2().tkinter_secondaire())
        bouton_creer.grid(row=1, column=0)


        text_vide = Label(fenetre, text="\n")
        text_vide.grid(row=4, column=0)


        # CHOISIR AMORCE
        text_amorce = Label(fenetre, text="Amorce")
        text_amorce.grid(row=5, column=0)

        self.var_texte_amorce = StringVar()

        bouton1 = Radiobutton(fenetre, text="Aucune", indicatoron=0, width=10, height=2,
                              variable=self.var_texte_amorce, value="Aucune",)
        bouton1.grid(row=6, column=0)
        bouton2 = Radiobutton(fenetre, text="Lettre", indicatoron=0, width=10, height=2,
                              variable=self.var_texte_amorce, value="Lettre")
        bouton2.grid(row=7, column=0)
        bouton3 = Radiobutton(fenetre, text="Chiffre", indicatoron=0, width=10, height=2,
                              variable=self.var_texte_amorce, value="Chiffre")
        bouton3.grid(row=8, column=0)

        # DEFINIR APARTIRDE
        text_apartirde = Label(fenetre, text="A partir de")
        text_apartirde.grid(row=9, column=0)

        self.var_texte_apartirde = StringVar()
        ligne_texte = Entry(fenetre, textvariable=self.var_texte_apartirde, width=10)
        ligne_texte.grid(row=10, column=0)


        text_vide = Label(fenetre, text="")
        text_vide.grid(row=11, column=0)



        #Column 1
        # ---------------------------------------------------------------------------------

        # Texte pour la règle
        text_nom_repertoire = Label(fenetre, text="Créer une règle  ")
        text_nom_repertoire.grid(row=2, column=1,)

        # DEFINIR PREFIXE
        text_prefixe = Label(fenetre, text="Préfixe")
        text_prefixe.grid(row=5, column=1,)

        self.var_texte_prefixe = StringVar()
        ligne_texte = Entry(fenetre, textvariable=self.var_texte_prefixe, width=10)
        ligne_texte.grid(row=6, column=1)



        #Column 2
        # ---------------------------------------------------------------------------------

        #DEFINIR LE NOM DE LA REGLE
        text_renommer_lot = Label(fenetre, text="Nom de la regle")
        text_renommer_lot.grid(row=1, column=2, columnspan=2, rowspan=1)

        self.var_texte_regle = StringVar()
        ligne_texte = Entry(fenetre, textvariable=self.var_texte_regle, width=10)
        ligne_texte.grid(row=2, column=2)

        #DEFINIR SI NOM DE FICHIER ORIGINAL OU AUTRE
        text_nomdufichier = Label(fenetre, text="Nom du fichier")
        text_nomdufichier.grid(row=5, column=2,)

        self.var_texte_nomfichier = StringVar()

        bouton4 = Radiobutton(fenetre, text="Nom original", indicatoron=0, width=10, height=2, variable=self.var_texte_nomfichier, value=1,)
        bouton4.grid(row=6, column=2)
        bouton5 = Radiobutton(fenetre, text="Autre", indicatoron=0, variable=self.var_texte_nomfichier, value=2, width=10, height=2)
        bouton5.grid(row=7, column=2)



        #Column 3
        # ---------------------------------------------------------------------------------

        # DEFENIR POSTFIXE
        text_postfixe = Label(fenetre, text="Postfixe")
        text_postfixe.grid(row=5, column=3,)

        self.var_texte_suffixe = StringVar()
        ligne_texte = Entry(fenetre, textvariable=self.var_texte_suffixe, width=10)
        ligne_texte.grid(row=6, column=3)

        # VAR Si l'on choisi un autre nom que le nom original
        self.var_texte_entrynom = StringVar()
        ligne_texte = Entry(fenetre, textvariable=self.var_texte_entrynom, width=10)
        ligne_texte.grid(row=7, column=3)



        #Column 4
        # ---------------------------------------------------------------------------------

        #DEFINIR L'EXTENSION QUE L'ON VEUT
        text_extension = Label(fenetre, text="Extension concernée")
        text_extension.grid(row=5, column=4,)

        self.var_texte_extension = StringVar()
        ligne_texte = Entry(fenetre, textvariable=self.var_texte_extension, width=15)
        ligne_texte.grid(row=6, column=4)

        #BOUTON PERMETTANT L'EXECUTION DE LA CREATION DE LA REGLE
        bouton_creer = Button(fenetre, text="Créer", width=10, height=2, command=lambda : self.create_regle())
        bouton_creer.grid(row=8, column=4)

        fenetre.mainloop()

