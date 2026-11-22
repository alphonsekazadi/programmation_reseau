from datetime import datetime

def journal(message):
    maintenant = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    ligne = f"[{maintenant}] {message}"

    print(ligne)

    with open("log.log", "a", encoding="utf-8") as f:
        f.write(ligne + "\n")

journal("Démarrage de la surveillance")