import hashlib
from Mdp import * 
user = input("Veuillez saisir votre nom d'utilisateur: ")

while True:
    mdp = input("Veuillez saisir votre mot de passe: ")
    
    verif = Mot_de_passe(mdp)
    if verif != "Le mot de passe a bien été confirmé":
        print("Mot de passe invalide, veuillez recommencer!")
        print(verif)
    else:
        hash_mdp = mdp
        print(mdp, "est un mot de passe valide")
        hash = hashlib.sha256(hash_mdp.encode())
        hex_hash = hash.hexdigest()
        print(hex_hash)
        convertir_fichier_à_json(user, hex_hash)
        break