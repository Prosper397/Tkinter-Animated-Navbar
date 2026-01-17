import tkinter as tk
from tkinter import *
from tkinter import PhotoImage

#from django.utils.termcolors import background

#Dictionnaire de couleurs
couleur = {
    "nero":"#252726",
    "purple":"#800080",
    "white":"#FFFFFF"
}

#Paramètres de la fenêtre
app = tk.Tk()
app.title("Mon Application")
app.config(bg="gray30")
app.geometry("400x600")
app.iconbitmap("logo2.ico")


# Paramétrage Switch
btnEtat = False

#Chargement image Navbar
navIcon = PhotoImage(file='menu.png')
closeIcon = PhotoImage(file="close.png")
imgFond = PhotoImage(file='back_image3.png')

#Définir les fonctions switch
def Switch() :
    global btnEtat      #Pr dire que "btnEtat" est 1e variable gloable
    if btnEtat is True :
    # Créer 1e fermeture animée Navbar
        for x in range(300) :
            navLateral.place(x = -x, y = 0)
            topFrame.update()
        # Reset couleur widgets
        bannerText.config(fg="purple")
        accueilTest.config(bg=couleur["purple"])
        topFrame.config(bg=couleur["purple"])
        app.config(bg="gray30")
        btnEtat = False

    else :
        for x in range(-300, 0) :
            navLateral.place(x = x, y = 0)
            topFrame.update()
            btnEtat = True




# Insérons le background
"""
background_label = Label(app, image=imgFond)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
"""

#Top navigation ou bar
#topFrame est une fenêtre dans la fenetre princiaple(app)
topFrame = tk.Frame(app, bg=couleur["purple"])
topFrame.pack(side="top", fill=tk.X)
#On fait .pack pr dire à la fenêtre là ou elle va s'afficher


#Texte de top Bar
accueilTest = tk.Label(topFrame, text="PYTHON", font="ExtraCondensed 15",bg=couleur["purple"],
       fg = "white", height=2, padx=2, pady=20)
accueilTest.pack(side="right")
#La taille du dont est 15 ici.

#Bannner test et Image de fond
can = Canvas(app, width=400, height=600)
bannerText = tk.Label(app, text="DEVELOPPEMENT \nWEB", font="ExtraCondensed 25",
                      fg="purple")
can.create_image(0, 0, anchor=NW, image=imgFond)

bannerText.place(x=50, y=400)

can.pack()

#NavBar Icon
navbarBtn = tk.Button(topFrame, image = navIcon, bg=couleur["purple"],
                      bd=0, padx=20,
                      activebackground=couleur["purple"],
                      command = Switch)

navbarBtn.place(x = 10, y = 10)

#Paramètre Navbar latéral
navLateral = tk.Frame(app, bg="gray30", width= 300, height= 600)
navLateral.place(x = -300, y = 0)
tk.Label(navLateral, font= "ExtraCondensed 15", bg=couleur["purple"], fg="black",
         width=300, height=2, padx=20).place(x=0, y=0)

y = 80


#Les options de la navBar latéral;
option = ["ACCUEIL", "PAGES", "PROFIL", "PARAMETRES", "AIDE"]
#Positionnement des options dans la navBar
for i in range(5) :
    tk.Button(navLateral, text=option[i], font="ExtraCondensed 15", bg="gray30",
              fg=couleur["white"], activebackground="gray30", bd=0).place(x=25, y=y)
    y += 40
    #"bd" pr dire qu'on ne veut pas d'effet 3D
#Paramétrage Bouton fermeture menu:
fermeBtn = tk.Button(navLateral, image=closeIcon, bg=couleur["purple"],
                     activebackground=couleur["purple"],
                     bd=0, command=Switch)

fermeBtn.place(x=250, y = 10)

app.mainloop()
