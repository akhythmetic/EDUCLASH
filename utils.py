import requests

def get_ech_data(url):
    """
    Role: Récupère un echantillon de données d'une API
    Input: url (str) : url de l'API
    Output: response.json() (dict) : données sous forme de dictionnaire
    préconditions: url doit être une url valide et sans variable GET
    """
    response = requests.get(url)
    if response.status_code == 200:
        print("Données récupérées avec succès")
        return response.json()
    else:
        # affiche une erreur si la requête n'a pas abouti
        print("Erreur lors de la récupération des données")

def get_data(url, limit=10):
    """
    Role: Récupère toutes les données d'une API
    Input: url (str) : url de l'API
           limit (int) : nombre de données à récupérer par requête (10 par défaut)
    Output: data (dict) : données sous forme de dictionnaire
    préconditions: url doit être une url valide
    """
    data_brut = get_ech_data(url) # data sortie de l'api avec les meta donnée
    total_count = data_brut['total_count']
    data = data_brut['results'] # data proprement dite avec uniquement ce qui nous intéresse
    offset = 0
    while offset < total_count:
        page = get_ech_data(url + f'?limit={limit}&offset={offset}')['results']
        offset += limit
        data = {**data, **page}
    return data