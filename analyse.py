import argparse
def lire_notes(chemin):
    eleves = []
    ignorees = 0
    with open(chemin, encoding="utf-8") as fichier:
        next(fichier)
        for ligne in fichier:
            champs = ligne.strip().split(",")
            try:
                note = int(champs[2])
            except ValueError:
                ignorees += 1
                continue
            eleves.append({"nom": champs[0], "matiere": champs[1], "note": note})
    return eleves, ignorees

def moyennes(eleves, cle="nom"):
    totaux = {}
    compteurs = {}
    for ligne in eleves:
        nom = ligne[cle]
        if nom not in totaux:
            totaux[nom] = 0
            compteurs[nom] = 0
        totaux[nom] += ligne["note"]
        compteurs[nom] += 1
    resultat ={}
    for nom in totaux:
        resultat[nom] = totaux[nom]/compteurs[nom]
    return resultat        

def main():
    parser = argparse.ArgumentParser(description="Analyse un fichier de notes CSV")
    parser.add_argument("--fichier", default="notes.csv", help="fichier CSV à analyser")
    parser.add_argument("--par", choices=["nom","matiere"], default="nom", help="regrouper les moyennes par élève (nom) ou par matière")
    args= parser.parse_args()

    try:
        eleves, ignorees = lire_notes(args.fichier)
    except FileNotFoundError:
        parser.error(f"fichier introuvable: {args.fichier}")
    
    for groupe, moyenne in moyennes(eleves, args.par).items():
       print(f"{groupe}: {moyenne:.2f}")

    meilleure = meilleure_note(eleves)
    pire = pire_note(eleves)
    if meilleure is not None:
        print(f"Meilleure note : {meilleure['note']} ({meilleure['nom']}, {meilleure['matiere']})")
        print(f"Pire note : {pire['note']} ({pire['nom']}, {pire['matiere']})")
    if ignorees>0:
        print(f"Attention: {ignorees} ligne(s) ignorée(s)")

def meilleure_note(eleves):
    meilleure = None
    for ligne in eleves:
        if meilleure is None or ligne["note"] > meilleure["note"]:
            meilleure = ligne
    return meilleure

def pire_note(eleves):
    pire = None
    for ligne in eleves:
        if pire is None or ligne["note"] < pire["note"]:
            pire = ligne
    return pire
              
if __name__=="__main__":
    main()
   
            
    