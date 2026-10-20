from analyse import moyennes, lire_notes

def test_moyennes():
    eleves = [
        {"nom": "Marie", "matiere": "Maths", "note": 10},
        {"nom":"Marie", "matiere":"Maths", "note": 20},
        {"nom":"Paul", "matiere":"Maths", "note": 12},
    ]
    assert moyennes(eleves) == {"Marie": 15, "Paul": 12}

def test_moyennes_liste_vide():
    assert moyennes([]) == {}

def test_lire_notes_ignore_les_lignes_invalides():
    eleves, ignorees = lire_notes("invalid.csv")
    assert len(eleves) == 2
    assert ignorees == 1

def test_moyennes_par_matiere():
    eleves = [
        {"nom": "Marie", "matiere": "Maths", "note": 10},
        {"nom":"Paul", "matiere":"Maths", "note": 14},
        {"nom":"Marie", "matiere":"Info", "note": 18},
    ]
    assert moyennes(eleves, "matiere") == {"Maths": 12, "Info": 18}
    
