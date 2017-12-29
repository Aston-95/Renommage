from Action import *
from Renommage import *
from Regle import *
from ListeRegle import *
import os

from PIL import ImageTk,Image
from tkinter import *
from tkinter import filedialog

import tkinter_2



class Tkinter1:

    def __init__(self):
        """
        Init de la classe Tkinter1 qui correspond au Tkinter du renommage
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

    def load_path(self):
        """
        Toute petite fonction pour avoir une interface dynamique lors de la selection du dossier
        :return:
        """
        Action.nomdurepertoire = filedialog.askdirectory()
        return

    def message_erreur(self):
        """
        Petite fonction ouvrant un TKinter indiquant que une erreur à été comise lors de l'entrée de la variable "apartirde"
        :return:
        """
        master = Tk()

        text_amorce = Label(master, text="Vous n'avez pas entrer une valeur correcte dans Apartirde \n Rappel : Pour chiffre mettez des chiffre entre 0 et 999 et pour Lettre entre A et ZZZ ")
        text_amorce.grid(row=0, column=0)

        bouton_lister = Button(master, text="Quitter", width=10, height=2, command=lambda: sys.exit(0))
        bouton_lister.grid(row=1, column=0)



    def pre_renommage(self):
        """
        Au début un peu de débug


        :return:
        """
        #DEBUG SI JAMAIS QUELQU'UN MET DANS LE APARTIRDE
        if self.var_texte_amorce.get() == "Lettre":

            verif = self.var_texte_apartirde.get()
            h =[]

            for c in verif:
                h.append(ord(c))

                for i in h:
                    if i >= 91 or  i < 65:
                        self.message_erreur()
                        pass

        if self.var_texte_amorce.get() == "Chiffre":

            verif = self.var_texte_apartirde.get()
            h = []


            for c in verif:
                h.append(ord(c))

                for i in h:
                    if i >= 57 or i < 48:
                        self.message_erreur()
                        pass


        #Trie de la variable "nomfichier"
        if self.var_texte_nomfichier.get() == ("2"):
            self.nomfichier=self.var_texte_entrynom.get()
        else:
            self.nomfichier = "Original"

        #La règle contient : 'AMORCE' ; 'APARTIRDE' ; 'PREFIXE' ; ' NOMFICHIER' ; 'POSTFIXE' ; 'EXTENSION'
        regle = []
        regle.append(self.var_texte_amorce.get())
        regle.append(self.var_texte_apartirde.get())
        regle.append(self.var_texte_prefixe.get())
        regle.append(self.nomfichier)
        regle.append(self.var_texte_suffixe.get())
        regle.append(self.var_texte_extension.get())

        Action.regle = regle

        original, final = Action(Action.nomdurepertoire, Action.regle).simule()


        r= Renommage(Action.nomdurepertoire, Action.regle)
        r.original=original
        r.modifie=final
        r.renommer()


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

        b = Button(master, text="Valider", width=10, height=2, command=lambda:  self.reglos(listbox.curselection()))
        b.pack()

        mainloop()


    def tkinter_principal(self):
        """
        Interface Tkinter du renommage. Contient les éléments de TKinter ainsi que les variables
        Aucun code dans cette fonction, que de l'esthétique.
        :return:
        """

        # Initialisation du Tkinter
        fenetre1 = Tk()
        fenetre1.geometry('600x350')

        #Column 0
        # ---------------------------------------------------------------------------------

        #LISTER REGLE
        bouton_lister = Button(fenetre1, text="Lister", width=10, height=2, command=lambda: self.tk_list())
        bouton_lister.grid(row=0, column=0)

        #CREER REGLE
        bouton_creer = Button(fenetre1, text="Créer", width=10, height=2, command=lambda: fenetre1.destroy() & tkinter_2.Tkinter2().tkinter_secondaire())
        bouton_creer.grid(row=1, column=0)


        text_vide = Label(fenetre1, text="\n")
        text_vide.grid(row=4, column=0)


        #CHOISIR AMORCE
        text_amorce = Label(fenetre1, text="Amorce")
        text_amorce.grid(row=5, column=0)

        self.var_texte_amorce = StringVar()

        bouton1 = Radiobutton(fenetre1, text="Aucune", indicatoron=0, width=10, height=2,
                              variable=self.var_texte_amorce, value="Aucune",)
        bouton1.grid(row=6, column=0)
        bouton2 = Radiobutton(fenetre1, text="Lettre", indicatoron=0, width=10, height=2,
                              variable=self.var_texte_amorce, value="Lettre")
        bouton2.grid(row=7, column=0)
        bouton3 = Radiobutton(fenetre1, text="Chiffre", indicatoron=0, width=10, height=2,
                              variable=self.var_texte_amorce, value="Chiffre")
        bouton3.grid(row=8, column=0)

        #DEFINIR APARTIRDE
        text_apartirde = Label(fenetre1, text="A partir de")
        text_apartirde.grid(row=9, column=0)

        self.var_texte_apartirde = StringVar()
        ligne_texte = Entry(fenetre1, textvariable=self.var_texte_apartirde, width=10)
        ligne_texte.grid(row=10, column=0)
        ligne_texte.insert(0, self.var_texte_apartirde.get())

        text_vide = Label(fenetre1, text="")
        text_vide.grid(row=11, column=0)



        #Column 1
        # ---------------------------------------------------------------------------------

        #Texte pour repertoire
        text_nom_repertoire = Label(fenetre1, text="Selectionner repertoire  ")
        text_nom_repertoire.grid(row=2, column=1,)

        #DEFINIR PREFIXE
        text_prefixe = Label(fenetre1, text="Préfixe")
        text_prefixe.grid(row=5, column=1,)

        self.var_texte_prefixe = StringVar()
        ligne_texte = Entry(fenetre1, textvariable=self.var_texte_prefixe, width=10)
        ligne_texte.grid(row=6, column=1)



        #Column 2
        # ---------------------------------------------------------------------------------

        #Texte renommer en lots
        text_renommer_lot = Label(fenetre1, text="Renommer en lots")
        text_renommer_lot.grid(row=1, column=2, columnspan=2, rowspan=1)

        #BOUTON POUR CHOISIR REPERTOIRE
        bouton_lister = Button(fenetre1, text="Chemin", width=10, height=2, command=lambda: self.load_path())
        bouton_lister.grid(row=2, column=2)

        # DEFINIR SI NOM DE FICHIER ORIGINAL OU AUTRE
        text_nomdufichier = Label(fenetre1, text="Nom du fichier")
        text_nomdufichier.grid(row=5, column=2,)

        self.var_texte_nomfichier = StringVar()

        bouton4 = Radiobutton(fenetre1, text="Nom original", indicatoron=0, variable=self.var_texte_nomfichier, value=1,)
        bouton4.grid(row=6, column=2)
        bouton5 = Radiobutton(fenetre1, text="Autre", indicatoron=0, variable=self.var_texte_nomfichier, value=2, width=10, height=2)
        bouton5.grid(row=7, column=2)



        #Column 3
        # ---------------------------------------------------------------------------------

        #DEFENIR POSTFIXE
        text_postfixe = Label(fenetre1, text="Postfixe")
        text_postfixe.grid(row=5, column=3,)

        self.var_texte_suffixe = StringVar()
        ligne_texte = Entry(fenetre1, textvariable=self.var_texte_suffixe, width=10)
        ligne_texte.grid(row=6, column=3)

        #VAR Si l'on choisi un autre nom que le nom original
        self.var_texte_entrynom = StringVar()
        ligne_texte = Entry(fenetre1, textvariable=self.var_texte_entrynom, width=10)
        ligne_texte.grid(row=7, column=3)



        #Column 4
        # ---------------------------------------------------------------------------------

        # DEFINIR L'EXTENSION QUE L'ON VEUT
        text_extension = Label(fenetre1, text="Extension concernée")
        text_extension.grid(row=5, column=4,)

        self.var_texte_extension = StringVar()
        ligne_texte = Entry(fenetre1, textvariable=self.var_texte_extension, width=15)
        ligne_texte.grid(row=6, column=4)

        # BOUTON PERMETTANT L'EXECUTION DU RENOMMAGE
        bouton_renommer = Button(fenetre1, text="Renommer", width=10, height=2, command=lambda: self.pre_renommage())
        bouton_renommer.grid(row=8, column=4)

        fenetre1.mainloop()
        return


