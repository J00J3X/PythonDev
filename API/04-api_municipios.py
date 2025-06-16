import requests
from pprint import pprint

url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"
#params = {
#    "localidade":33 #RJ
#}
response = requests.get(url)

try:
    response.raise_for_status()
except requests.HTTPError as e:
        print("Erro no request: {e}")
        resultado = None
else:
      resultado = response.json()
      pprint(resultado)