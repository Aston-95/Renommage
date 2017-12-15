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

        :param value:
        """



    def load_file(self):
        Action.nomdurepertoire = filedialog.askdirectory()
        print(Action.nomdurepertoire)
        return

    def create_regle(self):
        r = self.var_texte_regle.get() + " [ " + str(self.var_texte_amorce) + " " + str(self.var_texte_apartirde) + " " + str(self.var_texte_prefixe) + " " + self.var_texte_suffixe.get() + " " + str(self.var_texte_extension) + " ]\n"
        file = ListeRegle(r).charger()

        # Regle [ Amorce Apartirde Prefixe Suffixe Extension ]

        nomlogiciel = []
        nomlogiciel.append(r)

        ListeRegle(r).sauvegarder()
        return


    def tkinter_secondaire(self):
        regle1 = Regle("Aucune", "2", "pre", "fichier", "post", "ext")

        fenetre = Tk()
        fenetre.geometry('600x350')

        #Column 0
        bouton_lister = Button(fenetre, text="Lister", width=10, height=2)
        bouton_lister.grid(row=0, column=0)

        bouton_creer = Button(fenetre, text="Créer", width=10, height=2)
        bouton_creer.grid(row=1, column=0)

        bouton_creer = Button(fenetre, text="Fenetre renom", width=10, height=2, command=lambda: Tkinter1.tkinter_principal(""))
        bouton_creer.grid(row=2, column=0)


        text_vide = Label(fenetre, text="\n")
        text_vide.grid(row=4, column=0)

        text_amorce = Label(fenetre, text="Amorce")
        text_amorce.grid(row=5, column=0)

        self.var_texte_amorce = StringVar()

        bouton1 = Radiobutton(fenetre, text="Aucune", indicatoron=0, width=10, height=2,
                              command=lambda:Regle.set_amorce(self.var_texte_amorce),
                              variable=self.var_texte_amorce, value="Aucune",)
        bouton1.grid(row=6, column=0)
        bouton2 = Radiobutton(fenetre, text="Lettre", indicatoron=0, width=10, height=2,
                              command=lambda:Regle.set_amorce(self.var_texte_amorcee),
                              variable=self.var_texte_amorce, value="Lettre")
        bouton2.grid(row=7, column=0)
        bouton3 = Radiobutton(fenetre, text="Chiffre", indicatoron=0, width=10, height=2,
                              command=lambda:Regle.set_amorce(self.var_texte_amorce),
                              variable=self.var_texte_amorce, value="Chiffre")
        bouton3.grid(row=8, column=0)

        text_apartirde = Label(fenetre, text="A partir de")
        text_apartirde.grid(row=9, column=0)

        self.var_texte_apartirde = StringVar()
        ligne_texte = Entry(fenetre, textvariable=self.var_texte_apartirde, width=10)
        ligne_texte.grid(row=10, column=0)


        text_vide = Label(fenetre, text="")
        text_vide.grid(row=11, column=0)



        #Column 1

        self.text_nom_repertoire = Label(fenetre, text="Créer une règle  ")
        self.text_nom_repertoire.grid(row=2, column=1,)

        self.text_prefixe = Label(fenetre, text="Préfixe")
        self.text_prefixe.grid(row=5, column=1,)

        self.var_texte_prefixe = StringVar()
        ligne_texte = Entry(fenetre, textvariable=self.var_texte_prefixe, width=10)
        ligne_texte.grid(row=6, column=1)

        #Column 2

        text_renommer_lot = Label(fenetre, text="Nom de la regle")
        text_renommer_lot.grid(row=1, column=2, columnspan=2, rowspan=1)

        self.var_texte_regle = StringVar()
        ligne_texte = Entry(fenetre, textvariable=self.var_texte_regle, width=10)
        ligne_texte.grid(row=2, column=2)

        text_nomdufichier = Label(fenetre, text="Nom du fichier")
        text_nomdufichier.grid(row=5, column=2,)

        value2 = StringVar()

        bouton4 = Radiobutton(fenetre, text="Nom original", width=10, height=2, variable=value2, value=1,)
        bouton4.grid(row=6, column=2)
        bouton5 = Radiobutton(fenetre, text="Lettre", indicatoron=0, variable=value2, value=2, width=10, height=2)
        bouton5.grid(row=7, column=2)

        #Column 3

        text_postfixe = Label(fenetre, text="Postfixe")
        text_postfixe.grid(row=5, column=3,)

        self.var_texte_suffixe = StringVar()
        ligne_texte = Entry(fenetre, textvariable=self.var_texte_suffixe, width=10)
        ligne_texte.grid(row=6, column=3)

        #Column 4

        text_extension = Label(fenetre, text="Extension concernée")
        text_extension.grid(row=5, column=4,)

        self.var_texte_extension = StringVar()
        ligne_texte = Entry(fenetre, textvariable=self.var_texte_extension, width=15)
        ligne_texte.grid(row=6, column=4)

        bouton_creer = Button(fenetre, text="Créer", width=10, height=2, command=lambda : self.create_regle())
        bouton_creer.grid(row=8, column=4)

        fenetre.mainloop()

