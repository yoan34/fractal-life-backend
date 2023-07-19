import os
from datetime import datetime
from constants import REPAS


# Initialiser un dictionnaire pour stocker les réponses du formulaire
donnees = {
    "repas_matin": "",
    "repas_midi": "",
    "repas_soir": "",
    "trop_manger": "",
    "sport": "",
    "meditation": "",
    "douche": "",
    "detox": "",
    "hhc": "",
}

# Les questions
questions = {
    "repas_matin": "Qu'ai-je mangé ce matin ?",
    "repas_midi": "Qu'ai mangé à midi ?",
    "repas_soir": "Qu'ai mangé le soir ?",
    "trop_manger": "Quand ai-je trop mangé ?",
    "sport": "Quel sport effectué ?",
    "meditation": "Quelle méditation ?",
    "douche": "Douche Froide, chaude ?",
    "detox": "Ai-je fais une detox ?",
    "hhc": "Quelle quantité HHC ?",
}


def valid_repas_input(reponse: str) -> bool:
    for s in reponse.split(' '):
        quantite, _, repas = s.partition('_')
        if quantite and not quantite.isdigit():
            repas = quantite  # On a pas de quantité, juste le nom du repas
        if not repas:  # Cas où on a pas de underscore
            repas = quantite
        if repas not in REPAS:
            return False
    return True



# La boucle principale
while True:
    os.system('clear')


    print(f"{'Calendar':-^80}")
    print()
    for i, (key, value) in enumerate(donnees.items()):
        print(f"{i+1}. {questions[key]:<26}: {value if value else '...'}")

    formulaire_valide = all(donnees.values())
    print("\nEntrez le numéro de la question, ou Q pour quitter.")
    if formulaire_valide:
        print("Ou tapez V pour valider le formulaire.")

    # Demander à l'utilisateur de choisir une question
    print('-'*80)
    choix = input("Votre choix : ")
    
    if choix.upper() == 'Q':
        print("Vous avez quitté le formulaire.")
        exit()
    elif choix.upper() == 'V' and formulaire_valide:
        print("Le formulaire a été validé !")
        break
    elif choix.isdigit() and 1 <= int(choix) <= len(donnees):
        key = list(donnees.keys())[int(choix) - 1]
        reponse = input(questions[key])
        # Ici, vous pouvez ajouter des vérifications pour les entrées
        # Par exemple, vérifier si la date est correcte :
        if key in ["repas_matin", "repas_midi", "repas_soir"]:
            if not valid_repas_input(reponse):
                print(f"Entré un repas valid.")
                continue
        donnees[key] = reponse

# Ici, vous pouvez continuer à ajouter les données au fichier JSON comme avant
