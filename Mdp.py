import json
import tkinter
from tkinter import * 

app = tkinter.Tk()
app.title("Utilisateur et son mot de passe")
app.geometry("800x600")

label_welcome = tkinter.Label(app, text="Bienvenue à Vous !!! :)", font=50,bg="black",width=100,height=3, fg="yellow")
label_welcome.pack()
label_accueil = tkinter.Label(app, text="Pour pouvoir vous inscrire ou vous connecter sur le site Neimiane, veuillez remplir le nom d'utilisateur et le mot de passe ci-dessous :")
label_accueil.place(x=5 , y=80)
label_utilisateur = tkinter.Label(app, text="Nom d'utilisateur", font= 25, fg = "red")
label_utilisateur.place(x=25 , y=120)
entry_utilisateur = tkinter.Entry(app, width=50)
entry_utilisateur.place(x=25 , y=150)

label_mdp = tkinter.Label(app, text="Mot de passe", font=25,fg="red")
label_mdp.place(x=25 , y = 200)
entry_mdp = tkinter.Entry(app,width=50, show="*")
entry_mdp.place(x=25 , y=230)

user = entry_mdp.get()
print(user)

def verif_boutton():
    user = entry_utilisateur.get()
    mdp = entry_mdp.get()
    print(user)
    print(mdp)
    Mot_de_passe(mdp)


def Mot_de_passe(nouveau_mdp):

    maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    u = 0
    min = "abcdefghijklmnopqrstuvwxyz"
    l = 0
    chiffre = "0123456789"
    c = 0
    special = "!@#$%^&*"
    s = 0
    
    if len(nouveau_mdp) >= 8 :
        # print("Votre mot de passe ne contient pas assez de caractères, 8 caractères minimums sont nécessaires.")
        
        for i in nouveau_mdp :
            if i in maj :
                
                u+=1
            if i in min :
                
                l+=1
            if i in chiffre :
               
                c+=1
            if i in special :
                
                s+=1
    else:
        print("Votre mot de passe ne contient pas assez de caractères, 8 caractères minimums sont nécessaires.")
        print(Mot_de_passe(nouveau_mdp))
    if  (u >=1 and l >=1 and c >=1 and s>=1) :
        print("Le mot de passe contient bien tout les caractères requis")
        second_saisi = input("Veuillez confirmer votre mot de passe : ")
    else :   
        print("Le mot de passe ne contient pas tout les caractères requis, minimum :1 majuscule, 1 minuscule, 1 chiffre et 1 caractère spécial(!@#$%^&*)")
        print(Mot_de_passe)
    if second_saisi == nouveau_mdp:
        return "Le mot de passe a bien été confirmé"
    else :
        print("Le mot de passe indiqué n'est pas identique à celui que vous avez saisi")  
        print(Mot_de_passe())



# Mot_de_passe()

def convertir_fichier_à_json(user, hex_hash):
    try:
        with open("data.json", "r", encoding='utf-8') as fichier:
            dic = json.load(fichier)
    except:
        dic = {}
    if user in dic:
        if hex_hash not in dic[user]:
            dic[user] += [hex_hash]
    elif user not in dic:
        dic[user] = [hex_hash]
    with open("data.json", "w", encoding='utf-8') as fichier:
        json.dump(dic, fichier, indent=2, separators=(',', ': '), ensure_ascii=False)


boutton = tkinter.Button(app, text="Connexion", width=30, command=verif_boutton).place(x=25 , y = 300)

app.mainloop()