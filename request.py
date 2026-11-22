import requests

requete = requests.get("https://api.github.com", timeout=5)

print(requete.status_code)

equipement = {
    "Routeur": "Cisco",
    "IP": "192.168.1.1"
}

requete_post = requests.post("https://api.github.com/post", json=equipement, timeout=5)
print(requete_post.status_code)
print(requete_post.json())