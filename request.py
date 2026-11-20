import requests

requete = requests.get("https://api.github.com", timeout=5)

print(requete.status_code)
print(requete.headers["Content-Type"])
