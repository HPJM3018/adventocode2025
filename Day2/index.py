import sys

def id_invalide(nombre: int) -> bool:
    s = str(nombre)
    if len(s) % 2 != 0:
        return False
    moitie = len(s) // 2
    return s[:moitie] == s[moitie:]

def calculer_somme_ids_invalides(fichier_input: str) -> int:
    try:
        with open(fichier_input, 'r') as f:
            ligne = f.read().strip()
        
        if not ligne:
            return 0
        
        somme_totale = 0
        plages = ligne.split(',')
        
        for plage_str in plages:
            plage_str = plage_str.strip()
            if not plage_str:
                continue
            
            parties = plage_str.split('-')
            if len(parties) != 2:
                continue
            
            try:
                debut = int(parties[0])
                fin = int(parties[1])
            except ValueError:
                continue
            
            if debut > fin:
                continue
            
            for id_num in range(debut, fin + 1):
                if id_invalide(id_num):
                    somme_totale += id_num
        
        return somme_totale
        
    except FileNotFoundError:
        return 0
    except Exception:
        return 0

resultat = calculer_somme_ids_invalides("input.txt")
# print(resultat)


################################" Part 02"###############################################################


def est_id_invalide_v2(nombre: int) -> bool:
    s = str(nombre)
    L = len(s)
    
    if L < 2:
        return False
    
    for segment_len in range(1, L // 2 + 1):
        if L % segment_len != 0:
            continue
        
        motif = s[:segment_len]
        k = L // segment_len  
        
        if s == motif * k:
            return True
    
    return False


def resoudre_partie2(fichier_input: str) -> int:
   
    try:
        with open(fichier_input, 'r') as f:
            donnees = f.read().strip()
        
        if not donnees:
            return 0
        
        somme_totale = 0
        plages = donnees.split(',')
        
        for plage_str in plages:
            plage_str = plage_str.strip()
            if not plage_str:
                continue
            
            parties = plage_str.split('-')
            if len(parties) != 2:
                continue
            
            try:
                debut = int(parties[0])
                fin = int(parties[1])
            except ValueError:
                continue
            
            if debut > fin:
                continue
            
            for id_num in range(debut, fin + 1):
                if est_id_invalide_v2(id_num):
                    somme_totale += id_num
        
        return somme_totale
        
    except FileNotFoundError:
        print(f"Erreur: Fichier '{fichier_input}' non trouvé.")
        return 0
    except Exception as e:
        print(f"Erreur: {e}")
        return 0


def main():
    fichier_input = "input.txt"
    resultat = resoudre_partie2(fichier_input)
    print(resultat)


if __name__ == "__main__":
    main()