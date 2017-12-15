
from Action import *
from Renommage import *
from Regle import *
from ListeRegle import *

from tkinter import *
from tkinter import filedialog

import tkinter_2



class Tkinter1:

    def __init__(self):
        """

        :param value:
        """

    def load_file(self):
        Action.nomdurepertoire = filedialog.askdirectory()
        print(Action.nomdurepertoire)
        return

    def tkinter_principal(self):

        fenetre1 = Tk()
        fenetre1.geometry('600x350')

        #Column 0
        bouton_lister = Button(fenetre1, text="Lister", width=10, height=2)
        bouton_lister.grid(row=0, column=0)

        bouton_creer = Button(fenetre1, text="Créer", width=10, height=2, command=lambda: tkinter_2.Tkinter2().tkinter_secondaire())
        bouton_creer.grid(row=1, column=0)


        text_vide = Label(fenetre1, text="\n")
        text_vide.grid(row=4, column=0)

        text_amorce = Label(fenetre1, text="Amorce")
        text_amorce.grid(row=5, column=0)

        value = StringVar()

        bouton1 = Radiobutton(fenetre1, text="Aucune", indicatoron=0, width=10, height=2,
                              command=lambda:Regle.amorce(value),
                              variable=value, value="Aucune",)
        bouton1.grid(row=6, column=0)
        bouton2 = Radiobutton(fenetre1, text="Lettre", indicatoron=0, width=10, height=2,
                              command=lambda:Regle.amorce(value),
                              variable=value, value="Lettre")
        bouton2.grid(row=7, column=0)
        bouton3 = Radiobutton(fenetre1, text="Chiffre", indicatoron=0, width=10, height=2,
                              command=lambda:Regle.amorce(value),
                              variable=value, value="Chiffre")
        bouton3.grid(row=8, column=0)

        text_apartirde = Label(fenetre1, text="A partir de")
        text_apartirde.grid(row=9, column=0)

        var_texte_apartirde = StringVar()
        ligne_texte = Entry(fenetre1, textvariable=var_texte_apartirde, width=10)
        ligne_texte.grid(row=10, column=0)


        text_vide = Label(fenetre1, text="")
        text_vide.grid(row=11, column=0)



        #Column 1

        text_nom_repertoire = Label(fenetre1, text="Selectionner repertoire  ")
        text_nom_repertoire.grid(row=2, column=1,)

        text_prefixe = Label(fenetre1, text="Préfixe")
        text_prefixe.grid(row=5, column=1,)

        var_texte_prefixe = StringVar()
        ligne_texte = Entry(fenetre1, textvariable=var_texte_prefixe, width=10)
        ligne_texte.grid(row=6, column=1)

        #Column 2

        text_renommer_lot = Label(fenetre1, text="Renommer en lots")
        text_renommer_lot.grid(row=1, column=2, columnspan=2, rowspan=1)

        bouton_lister = Button(fenetre1, text="Chemin", width=10, height=2, command=lambda: self.load_file())
        bouton_lister.grid(row=2, column=2)

        text_nomdufichier = Label(fenetre1, text="Nom du fichier")
        text_nomdufichier.grid(row=5, column=2,)

        value2 = StringVar()

        bouton4 = Radiobutton(fenetre1, text="Nom original", width=10, height=2, variable=value2, value=1,)
        bouton4.grid(row=6, column=2)
        bouton5 = Radiobutton(fenetre1, text="Lettre", indicatoron=0, variable=value2, value=2, width=10, height=2)
        bouton5.grid(row=7, column=2)

        #Column 3

        text_postfixe = Label(fenetre1, text="Postfixe")
        text_postfixe.grid(row=5, column=3,)

        var_texte_suffixe = StringVar()
        ligne_texte = Entry(fenetre1, textvariable=var_texte_suffixe, width=10)
        ligne_texte.grid(row=6, column=3)

        #Column 4

        text_extension = Label(fenetre1, text="Extension concernée")
        text_extension.grid(row=5, column=4,)

        var_texte_extension = StringVar()
        ligne_texte = Entry(fenetre1, textvariable=var_texte_extension, width=15)
        ligne_texte.grid(row=6, column=4)

        bouton_renommer = Button(fenetre1, text="Renommer", width=10, height=2, command=lambda: Renommage().renommer(Renommage.nomdurepertoire,Renommage.regle))
        bouton_renommer.grid(row=8, column=4)

        fenetre1.mainloop()
        return


